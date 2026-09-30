import pytest
from calculator import add, multiply
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(2, 0) == 0