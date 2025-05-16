from pathlib import Path

import modal

ROOT_PATH = Path(__file__).parent.parent

image = (
    modal.Image.debian_slim()
    .run_commands(f"uname")
    .run_commands(f"find / -type d -name ci-on-modal")
    .run_commands(f"pwd && ls -l {ROOT_PATH}")
    .pip_install("pytest")
    .pip_install_from_requirements(ROOT_PATH / "requirements.txt")
    .add_local_dir(ROOT_PATH / "tests", remote_path="/root/tests")
)

app = modal.App("ci-testing", image=image)


@app.function(gpu="any")
def pytest():
    import subprocess

    subprocess.run(["pytest", "-vs"], check=True, cwd="/root")
