import pytest
from pymads.cli import main

def test_cli_help(monkeypatch, capsys):
    """Test that the CLI help message is displayed correctly."""
    # Mock sys.argv
    monkeypatch.setattr('sys.argv', ['pymads', '--help'])
    
    # Catch SystemExit
    with pytest.raises(SystemExit):
        main()
    
    # Check output
    captured = capsys.readouterr()
    assert "PyMADS CLI" in captured.out
    assert "Usage:" in captured.out
