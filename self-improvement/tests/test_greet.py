import pytest

from src.greet import greet


def test_greet_returns_message():
    assert greet("World") == "Hello, World!"


@pytest.mark.parametrize("invalid_name", ["", "   ", None, 123])
def test_greet_raises_on_invalid_name(invalid_name):
    with pytest.raises(ValueError):
        greet(invalid_name)
