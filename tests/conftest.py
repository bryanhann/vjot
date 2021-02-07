# content of conftest.py
import pytest
import pathlib

__root = pathlib.Path(__file__).parent.parent
__tests = __root/'tests'
__sample = __tests/'sample'
__stamps = __sample/'stamps'

class Namespace: pass

@pytest.fixture(scope="module")
def paths():
    ret=Namespace()
    ret.root = pathlib.Path(__file__).parent.parent
    ret.sample = ret.root/'tests/sample'
    return ret


@pytest.fixture(scope="module")
def SAMPLE_STAMPS(paths):
    """An ordered list of the sample timestamps"""
    return __stamps.read_text().split()


