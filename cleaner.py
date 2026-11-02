"""Small helper functions for cleaning data."""


def remove_duplicates(items):
    """Return a new list without duplicates. Keeps the first-seen order."""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def clean_name(name):
    """Trim spaces, join extra spaces, and capitalize each word.

    Example: "  aLiCe   smith " -> "Alice Smith"
    """
    words = name.split()
    return " ".join(word.capitalize() for word in words)


def average(numbers):
    """Return the average of a list of numbers.

    Raises ValueError if the list is empty.
    """
    if not numbers:
        raise ValueError("average() needs at least one number")
    return sum(numbers) / len(numbers)
