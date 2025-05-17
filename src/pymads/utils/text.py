# src/pymads/utils/text.py

def omin_spacje(text: str, position: int) -> int:
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
