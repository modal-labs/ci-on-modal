import pytest

import lib


@pytest.mark.modal
def test_torch_cuda():
    assert lib.has_gpu()


def test_torch_no_cuda():
    assert not lib.has_gpu()
