from pathlib import Path

import modal

image = (
    modal.Image.debian_slim()
    .pip_install_from_requirements(Path(__file__).parent.parent / "requirements.txt")
    .pip_install_from_requirements(
        Path(__file__).parent.parent / "requirements-dev.txt"
    )
    .copy_local_file(Path(__file__).parent.parent / "pytest.ini", "/root/pytest.ini")
    .copy_local_dir(Path(__file__).parent.parent / "tests", "/root/tests")
)
app = modal.App("ci-testing", image=image)


@app.function(gpu="a100")
def pytest():
    import subprocess

    subprocess.run(["pytest", "-vs", "-m", "modal"], check=True)


@app.local_entrypoint()
def main():
    pytest.remote()
