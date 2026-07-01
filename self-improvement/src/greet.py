def greet(name):
    """Build a greeting message for the given name.

    Args:
        name: The name to greet. Must be a non-empty string.

    Returns:
        A greeting string of the form "Hello, {name}!".

    Raises:
        ValueError: If name is not a non-empty string.
    """
    if not isinstance(name, str) or not name.strip():
        raise ValueError("name must be a non-empty string")
    return f"Hello, {name}!"
