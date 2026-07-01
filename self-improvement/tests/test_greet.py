from src.greet import greet


def test_greet_returns_message():
    assert greet("World") == "Hello, World!"
