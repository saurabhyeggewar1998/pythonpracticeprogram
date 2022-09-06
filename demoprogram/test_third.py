import pytest as pytest


def test_sqrt():
    x=10
    y=20
    z=x+y
    print(z)
    assert z==30
@pytest.mark.abc
def test_sub():
    x=100
    y=30
    z=x-y
    print(z)
    assert z==70

@pytest.fixture
def input_value():
   input = 39
   return input
@pytest.mark.divisible
def test_divisible_by_3(input_value):
   assert input_value % 3 == 0
