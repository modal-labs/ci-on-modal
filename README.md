# Run Continuous Integration (CI) Tests on Modal

[This example repo](https://github.com/modal-labs/ci-on-modal)
is a demonstration of one pattern for running tests on Modal:
bring your existing package and test suite (here `my_pkg` and `tests`)
and add a Modal App (`my_pkg.ci`)
that mounts your tests
and a Function (`pytest`) runs `pytest`.

That's as straightforward as

```python
# my_pkg/ci.py
tests = modal.Mount.from_local_dir("path/to/tests", remote_path="/root/tests")


@app.function(gpu="any", mounts=[tests])
def pytest():
    import subprocess

    subprocess.run(["pytest", "-vs"], check=True, cwd="/root")
```

## Setup

- Create a Python virtual environment
- `pip install modal`
- That's it 😎

## Usage

All commands below are run from the root of the repository.

### Run tests remotely on Modal

```bash
modal run my_pkg.ci
```

On the first execution, the [container image](https://modal.com/docs/guide/custom-container)
for your application will be built.

This image will be cached on Modal and only rebuilt if one of its dependencies,
like the `requirements.txt` file, changes.

### Run tests on Modal from GitHub Actions

The same command can be executed from inside a CI runner on another platform.
We provide a sample GitHub Actions workflow in `.github/workflows/ci.yml`.

To run these tests on GitHub Actions, fork this repo and
[create a new GitHub Actions secret](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions)
that contains your `MODAL_TOKEN_ID` and `MODAL_TOKEN_SECRET`.
You can find this info in the `.modal.toml` file in your home directory.

Now you can [manually trigger the tests to run on GitHub Actions](https://docs.github.com/en/actions/using-workflows/manually-running-a-workflow)
or trigger them by making a change on our fork and pushing to `main` or making a pull request.

### Debug tests running remotely

To debug the tests, you can open a shell
in the exact same environment that the tests are run in:

```bash
modal shell my_pkg.ci
```

We used the `shell` feature heavily while developing this pattern!

_Note_: On the Modal worker, the `pytest` command is run from the home directory, `/root`,
which contains the `tests` folder, but the `modal shell` command will
drop you at the top of the filesystem, `/`.
