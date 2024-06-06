# CI On Modal

This repo is a demonstration of one pattern for running tests on Modal:
bring your existing test suite and wrap it in a Modal App (`ci_on_modal.run`) and function (`.pytest`) that

1. imports the code you want to test
2. mounts your tests
3. runs `pytest`, optionally with pytest marks to separate local and remote tests.

## Setup

- Create Python virtual environment
- `pip install -r requirements.txt -r requirements-dev.txt`

## Usage

All commands below are run from the root of the repository.

### Run tests remotely on Modal

```bash
modal run ci_on_modal
```

### Debug remote testing environment

```bash
modal shell ci_on_modal
```

I used the `shell` feature heavily while developing this pattern!

_Note_: On the Modal worker, the `pytest` command is run from the home directory, `/root`, which contains `lib.py` and the `tests` folder.

### Locally run all tests not tagged with `modal` marker

For running in other testing environments.

```bash
pytest -vs -m "not modal"
```
