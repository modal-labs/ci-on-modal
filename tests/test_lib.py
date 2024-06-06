from pathlib import Path

import modal
import pytest

import lib

image = (
    modal.Image.debian_slim()
    .pip_install_from_requirements(Path(__file__).parent / "requirements.txt")
    .pip_install_from_requirements(Path(__file__).parent / "requirements-dev.txt")
    .copy_local_file(Path(__file__).parent / "pytest.ini")
)
app = modal.App("ci-testing", image=image)


@app.function(gpu="any")
def run_pytest():
    import subprocess

    subprocess.run(["pytest", "-vs", "-m", "modal"], check=True)


@pytest.mark.modal
def test_torch_cuda():
    assert lib.has_gpu()


def test_torch_no_cuda():
    assert not lib.has_gpu()


@app.local_entrypoint()
def main():
    run_pytest.remote()
