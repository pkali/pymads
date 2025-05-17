# tests/utils/test_text.py

import pytest
from pymads.utils.text import skip_spaces, __inc, tab2space, ansi_upper_case, up_cas_


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


def test_tab2space_basic():
    """Test basic tab2space functionality."""
    # Test with a string containing tabs
    assert tab2space("abc\tdef") == "abc        def"
    
    # Test with a string without tabs
    assert tab2space("abcdef") == "abcdef"
    
    # Test with multiple tabs
    assert tab2space("abc\t\tdef") == "abc                def"
    
    # Test with spaces and tabs
    assert tab2space("abc \t def") == "abc          def"

def test_tab2space_custom_spaces():
    """Test tab2space with custom number of spaces."""
    # Test with a string containing tabs and custom spaces
    assert tab2space("abc\tdef", 4) == "abc    def"
    
    # Test with a string without tabs
    assert tab2space("abcdef", 4) == "abcdef"
    
    # Test with multiple tabs and custom spaces
    assert tab2space("abc\t\tdef", 4) == "abc        def"
    
    # Test with spaces and tabs and custom spaces
    assert tab2space("abc \t def", 4) == "abc      def"


def test_tab2space_empty_string():
    """Test tab2space with empty string."""
    assert tab2space("") == ""
    
    # Test with empty string and custom spaces
    assert tab2space("", 4) == ""
    
    # Test with empty string and default spaces
    assert tab2space("", 8) == ""


def test_tab2space_no_tabs():
    """Test tab2space with no tabs."""
    # Test with a string without tabs
    assert tab2space("abcdef") == "abcdef"
    
    # Test with a string without tabs and custom spaces
    assert tab2space("abcdef", 4) == "abcdef"
    
    # Test with a string without tabs and default spaces
    assert tab2space("abcdef", 8) == "abcdef"


def test_ansi_upper_case_basic():
    """Test basic ANSI upper case functionality."""
    # Test with lowercase letters
    assert ansi_upper_case("abc") == "ABC"
    
    # Test with uppercase letters
    assert ansi_upper_case("ABC") == "ABC"
    
    # Test with mixed case
    assert ansi_upper_case("aBc") == "ABC"
    
    # Test with numbers and special characters
    assert ansi_upper_case("abc123!@#") == "ABC123!@#"


def test_ansi_upper_case_empty_string():
    """Test ANSI upper case with empty string."""
    assert ansi_upper_case("") == ""
    
    # Test with empty string and custom spaces
    assert ansi_upper_case("  ") == "  "
    
    # Test with empty string and default spaces
    assert ansi_upper_case("\n \t") == "\n \t"


def test_ansi_upper_case_no_change():
    """Test ANSI upper case with no change."""
    # Test with a string that is already uppercase
    assert ansi_upper_case("ABC") == "ABC"
    
    # Test with a string that is already uppercase and custom spaces
    assert ansi_upper_case("A\nB\tC") == "A\nB\tC"
    
    # Test with a string that is already uppercase and default spaces
    assert ansi_upper_case(" A B C ") == " A B C "


def test_up_cas__basic():
    """Test basic up_cas_ functionality."""
    # Test with lowercase character
    assert up_cas_("a") == "A"
    
    # Test with uppercase character
    assert up_cas_("A") == "A"
   
    # Test with non-alphabetic character
    assert up_cas_("1") == "1"
    
    # Test with special character
    assert up_cas_("!") == "!"


def test_up_cas__empty_string():
    """Test up_cas_ with empty string."""
    with pytest.raises(ValueError):
        up_cas_("")
    

def test_up_cas__multiple_characters():
    """Test up_cas_ with multiple characters."""
    with pytest.raises(ValueError):
        up_cas_("abc")
    
    # Test with multiple characters and custom spaces
    with pytest.raises(ValueError):
        up_cas_("\nabc")
    
    # Test with multiple characters and default spaces
    with pytest.raises(ValueError):
        up_cas_("  ")


def test_up_cas__non_alphabetic():
    """Test up_cas_ with non-alphabetic character."""
    # Test with non-alphabetic character
    assert up_cas_("@") == "@"
    
    # Test with special character
    assert up_cas_("$") == "$"
    
    # Test with non-alphabetic character and custom spaces
    assert up_cas_("%") == "%"
    
    # Test with special character and default spaces
    assert up_cas_("^") == "^"
