# tests/utils/test_text.py

import pytest
from pymads.utils.text import omin_spacje

def test_omin_spacje_basic():
    """Test basic space skipping functionality."""
    # Test with spaces at the beginning
    assert omin_spacje("   abc", 0) == 3
    
    # Test with no spaces
    assert omin_spacje("abc", 0) == 0
    
    # Test with spaces in the middle
    assert omin_spacje("abc   def", 3) == 6
    
    # Test with spaces at the end
    assert omin_spacje("abc   ", 3) == 6
    
def test_omin_spacje_different_whitespace():
    """Test skipping different types of whitespace."""
    # Test with tabs, newlines, and spaces
    assert omin_spacje("\t\n abc", 0) == 3
    
    # Test with mixed whitespace
    assert omin_spacje("abc \t \n def", 3) == 7
    
def test_omin_spacje_empty_string():
    """Test with empty string."""
    assert omin_spacje("", 0) == 0
    
def test_omin_spacje_position_beyond_length():
    """Test with position beyond string length."""
    assert omin_spacje("abc", 5) == 5
