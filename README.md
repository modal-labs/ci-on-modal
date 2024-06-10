# CI On Modal

This repo is a demonstration of one pattern for running tests on Modal:
bring your existing test suite and package (e.g. `my_pkg`), and add a Modal App (`my_pkg.ci`) and function (`.pytest`) that

1. imports the code you want to test
2. mounts your tests
3. runs `pytest`

## Setup

- Create Python virtual environment
- `pip install modal`

## Usage

All commands below are run from the root of the repository.

### Run tests remotely on Modal

This can be executed from inside another, cheaper CI runner, e.g. on GitHub Actions.

```bash
modal run my_pkg.ci
```

### Debug remote testing environment

```bash
modal shell my_pkg.ci
```

I used the `shell` feature heavily while developing this pattern!

_Note_: On the Modal worker, the `pytest` command is run from the home directory, `/root`, which contains the `tests` folder.
