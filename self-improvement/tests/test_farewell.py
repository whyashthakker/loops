import pytest

from src.farewell import farewell


def test_farewell_returns_message():
    assert farewell("World") == "Goodbye, World!"


@pytest.mark.parametrize("invalid_name", ["", "   ", None, 123])
def test_farewell_raises_on_invalid_name(invalid_name):
    with pytest.raises(ValueError):
        farewell(invalid_name)
