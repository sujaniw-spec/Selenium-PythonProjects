import pytest
import sys


@pytest.mark.skip(reason="Not included in the build")
def test_demo1():
    assert True


def test_demo2():
    assert True


@pytest.mark.skipif(sys.version_info > (3, 6), reason="Require version 3.5 or higher")
def test_demo3():
    assert True


@pytest.mark.windows
def test_demo4():
    assert True


@pytest.mark.mac
def test_demo5():
    assert True
