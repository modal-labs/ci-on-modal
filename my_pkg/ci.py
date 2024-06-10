from pathlib import Path

import modal

ROOT_PATH = Path(__file__).parent.parent

image = (
    modal.Image.debian_slim()
    .pip_install("pytest")
    .pip_install_from_requirements(ROOT_PATH / "requirements.txt")
)
app = modal.App("ci-testing", image=image)


@app.function(
    gpu="a100", 
    mounts=[modal.Mount.from_local_dir(ROOT_PATH / "tests", remote_path="/root/tests")],
)
def pytest():
    import subprocess

    subprocess.run(["pytest", "-vs"], check=True, cwd = "/root/tests")