# src/pymads/utils/text.py

def skip_spaces(text: str, position: int) -> int:
    """
    Skip spaces in the input string starting from the given position.
    
    This is a Python implementation of the Pascal 'omin_spacje' function
    from the original MADS assembler.
    
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


def Tab2Space(text: str, spaces: int = 8) -> str:
    """
    Convert tabs to spaces in a string.
    
    Args:
        text: Input string with possible tabs
        spaces: Number of spaces per tab (default: 8)
        
    Returns:
        String with tabs replaced by spaces
    """
    return text.replace('\t', ' ' * spaces)