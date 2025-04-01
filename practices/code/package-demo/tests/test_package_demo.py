from package_demo import some_stuff
from package_demo.submodule import get_random_number

def test_some_stuff():
    result = some_stuff()
    assert result == 42

def test_get_random_number():
    result = get_random_number()
    assert isinstance(result, int)
    assert 1 <= result <= 100
