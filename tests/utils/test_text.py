# tests/utils/test_text.py

import pytest
from pymads.utils.text import skip_spaces, __inc, Tab2Space


def test_skip_spaces_basic():
    """Test basic space skipping functionality."""
    # Test with spaces at the beginning
    assert skip_spaces("   abc", 0) == 3
    
    # Test with no spaces
    assert skip_spaces("abc", 0) == 0
    
    # Test with spaces in the middle
    assert skip_spaces("abc   def", 3) == 6
    
    # Test with spaces at the end
    assert skip_spaces("abc   ", 3) == 6


def test_skip_spaces_different_whitespace():
    """Test skipping different types of whitespace."""
    # Test with tabs, newlines, and spaces
    assert skip_spaces("\t\n abc", 0) == 3
    
    # Test with mixed whitespace
    assert skip_spaces("abc \t \n def", 3) == 8


def test_omin_spacje_empty_string():
    """Test with empty string."""
    assert skip_spaces("", 0) == 0


def test_omin_spacje_position_beyond_length():
    """Test with position beyond string length."""
    assert skip_spaces("abc", 5) == 5


def test__inc_basic():
    """Test basic increment functionality."""
    # Test with normal position
    assert __inc("abc", 1) == 2
    
    # Test with position at the end of the string
    assert __inc("abc", 3) == 3
    
    # Test with position beyond the string length
    assert __inc("abc", 4) == 4


def test_Tab2Space_basic():
    """Test basic Tab2Space functionality."""
    # Test with a string containing tabs
    assert Tab2Space("abc\tdef") == "abc        def"
    
    # Test with a string without tabs
    assert Tab2Space("abcdef") == "abcdef"
    
    # Test with multiple tabs
    assert Tab2Space("abc\t\tdef") == "abc                def"
    
    # Test with spaces and tabs
    assert Tab2Space("abc \t def") == "abc          def"

def test_Tab2Space_custom_spaces():
    """Test Tab2Space with custom number of spaces."""
    # Test with a string containing tabs and custom spaces
    assert Tab2Space("abc\tdef", 4) == "abc    def"
    
    # Test with a string without tabs
    assert Tab2Space("abcdef", 4) == "abcdef"
    
    # Test with multiple tabs and custom spaces
    assert Tab2Space("abc\t\tdef", 4) == "abc        def"
    
    # Test with spaces and tabs and custom spaces
    assert Tab2Space("abc \t def", 4) == "abc      def"


def test_Tab2Space_empty_string():
    """Test Tab2Space with empty string."""
    assert Tab2Space("") == ""
    
    # Test with empty string and custom spaces
    assert Tab2Space("", 4) == ""
    
    # Test with empty string and default spaces
    assert Tab2Space("", 8) == ""


def test_Tab2Space_no_tabs():
    """Test Tab2Space with no tabs."""
    # Test with a string without tabs
    assert Tab2Space("abcdef") == "abcdef"
    
    # Test with a string without tabs and custom spaces
    assert Tab2Space("abcdef", 4) == "abcdef"
    
    # Test with a string without tabs and default spaces
    assert Tab2Space("abcdef", 8) == "abcdef"