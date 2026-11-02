import pytest

from cleaner import average, clean_name, remove_duplicates


def test_remove_duplicates_keeps_order():
    assert remove_duplicates([3, 1, 3, 2, 1]) == [3, 1, 2]


def test_remove_duplicates_empty_list():
    assert remove_duplicates([]) == []


def test_clean_name_trims_and_capitalizes():
    assert clean_name("  aLiCe   smith ") == "Alice Smith"


def test_clean_name_empty_string():
    assert clean_name("   ") == ""


def test_average_of_numbers():
    assert average([80, 90, 100]) == 90


def test_average_with_decimals():
    assert average([1, 2]) == 1.5


def test_average_empty_list_raises_error():
    with pytest.raises(ValueError):
        average([])
