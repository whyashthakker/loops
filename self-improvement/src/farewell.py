def farewell(name):
    """Build a farewell message for the given name.

    Args:
        name: The name to bid farewell to. Must be a non-empty string.

    Returns:
        A farewell string of the form "Goodbye, {name}!".

    Raises:
        ValueError: If name is not a non-empty string.
    """
    if not isinstance(name, str) or not name.strip():
        raise ValueError("name must be a non-empty string")
    return f"Goodbye, {name}!"
