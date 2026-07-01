from src.farewell import farewell


def test_farewell_returns_message():
    assert farewell("World") == "Goodbye, World!"
