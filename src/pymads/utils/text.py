# src/pymads/utils/text.py


def skip_spaces(text: str, position: int) -> int:
    """
    Skip spaces in the input string starting from the given position.

    Original Pascal function: omin_spacje

    Args:
        text: The input string to process
        position: The starting position (0-based index)

    Returns:
        The new position after skipping spaces
    """
    text_length = len(text)

    # Skip spaces, tabs, and other whitespace
    while position < text_length and text[position].isspace():
        position += 1

    return position


def __inc(text: str, position: int) -> int:
    """
    Increment position in string, equivalent to Pascal's __inc procedure.

    Args:
        text: The input string
        position: Current position

    Returns:
        New incremented position
    """
    if position < len(text):
        return position + 1
    return position


def tab2space(text: str, spaces: int = 8) -> str:
    """
    Convert tabs to spaces in a string.

    Original Pascal function: Tab2Space

    Args:
        text: Input string with possible tabs
        spaces: Number of spaces per tab (default: 8)

    Returns:
        String with tabs replaced by spaces
    """
    return text.replace("\t", " " * spaces)


def ansi_upper_case(text: str) -> str:
    """
    Convert string to uppercase.

    Original Pascal function: AnsiUpperCase

    Args:
        text: Input string

    Returns:
        Uppercase version of the input string
    """
    return text.upper()


def up_cas_(char: str) -> str:
    """
    Convert a single character to uppercase.

    Original Pascal function: UpCas_

    Args:
        char: Input character (single-character string)

    Returns:
        Uppercase version of the input character
    """
    if len(char) != 1:
        raise ValueError("Input must be a single character")
    return char.upper()


def int_to_str(value: int) -> str:
    """
    Convert integer to string.

    Original Pascal function: IntToStr

    Args:
        value: Integer value

    Returns:
        String representation of the integer
    """
    if not isinstance(value, int):
        raise ValueError("Input must be an integer")
    if isinstance(value, bool):
        raise ValueError("Input must not be a boolean")
    return str(value)


def str_to_int(text: str) -> int:
    """
    Convert string to integer.

    Original Pascal function: StrToInt

    Args:
        text: String representation of an integer

    Returns:
        Integer value

    Raises:
        ValueError: If the string cannot be converted to an integer
    """
    try:
        return int(text)
    except Exception as e:
        raise ValueError(f"Cannot convert '{text}' to integer: {e}") from e
