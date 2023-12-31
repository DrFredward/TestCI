import pytest
from my_source import add_func


def test_add_one():
    assert add_func(2, 5) == 7


@pytest.mark.xfail  # markiert pytest, dass ein Fehler erwartet wird
def test_add_fail():
    assert add_func(5, 5) == 9


def test_add_two():
    assert add_func(4,4) == 8