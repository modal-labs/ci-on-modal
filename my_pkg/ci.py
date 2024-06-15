from pathlib import Path

import modal

ROOT_PATH = Path(__file__).parent.parent

image = (
    modal.Image.debian_slim()
    .pip_install("pytest")
    .pip_install_from_requirements(ROOT_PATH / "requirements.txt")
)

app = modal.App("ci-testing", image=image)

# mount: add local files to the remote container
tests = modal.Mount.from_local_dir(ROOT_PATH / "tests", remote_path="/root/tests")


@app.function(gpu="any", mounts=[tests])
def pytest():
    import subprocess

    subprocess.run(["pytest", "-vs"], check=True, cwd="/root")
