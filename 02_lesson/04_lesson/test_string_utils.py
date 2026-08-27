import pytest
from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("   skypro   ", "skypro   "),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.parametrize("invalid_input", [
    None,
    ("", ""),
    ("   ", ""),
])
def test_trim_negative(invalid_input):
    with pytest.raises(AttributeError):
        assert string_utils.trim(invalid_input)


@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "P", True),
    ("", "A", False),
])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.parametrize("invalid_str, invalid_symbol, expected", [
    (None, "S", AttributeError),
    ("Skypro", None, TypeError),
    (123, "k", AttributeError),
])
def test_contains_negative(invalid_str, invalid_symbol, expected):
    with pytest.raises(expected):
        assert string_utils.contains(invalid_str, invalid_symbol)


@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("SkyPro", "U", "SkyPro"),
    ("SkyPro", "SkyPro", ""),
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.parametrize("invalid_str, invalid_symbol, expected", [
    (None, "k", AttributeError),
    ("", None, TypeError),
])
def test_delete_symbol_negative(invalid_str, invalid_symbol, expected):
    with pytest.raises(expected):
        assert string_utils.delete_symbol(invalid_str, invalid_symbol)
