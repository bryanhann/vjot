# content of conftest.py
import pytest
import pathlib

class Namespace: pass

@pytest.fixture(scope="module")
def paths():
    ret=Namespace()
    ret.root = pathlib.Path(__file__).parent.parent
    ret.sample = ret.root/'sample'
    return ret


@pytest.fixture(scope="module")
def SAMPLE_STAMPS():
    """An ordered list of the sample timestamps"""
    return """
        20200923T193234
        20200923T193330
        20200923T195246
        20200923T195906
        20200924T190944
        20200924T191456
        20200924T191636
        20200924T191802
        20200924T192626
        """.split()
