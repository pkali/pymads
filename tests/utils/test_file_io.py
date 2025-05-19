from pymads.utils.file_io import (
    get_file_path,
    get_file_name,
)

import os

import pytest


@pytest.mark.parametrize(
    "path, expected",
    [
        ("C:/Users/John/Documents/file.txt", "C:/Users/John/Documents"),
        ("/home/user/file.txt", "/home/user"),
        ("file.txt", ""),
        ("C:/file.txt", "C:"),
        ("C:/file", "C:"),
        ("C:/file/", "C:/file"),
        ("C:/file//", "C:/file"),
        ("C:/file///", "C:/file"),
        ("", ""),  # empty path
        ("/", "/"),  # root directory
        ("C:/", "C:"),  # Windows root
        ("folder/subfolder/", "folder/subfolder"),
        ("folder//subfolder//file.txt", "folder//subfolder"),
    ],
)
def test_get_file_path(path, expected):
    """
    Test the get_file_path function.
    """
    assert get_file_path(path) == expected


@pytest.mark.parametrize(
    "path, expected",
    [
        ("C:/Users/John/Documents/file.txt", "file.txt"),
        ("/home/user/file.txt", "file.txt"),
        ("file.txt", "file.txt"),
        ("C:/file.txt", "file.txt"),
        ("C:/file", "file"),
        ("C:/file/", ""),  # trailing slash, no file
        ("C:/file//", ""),  # multiple trailing slashes, no file
        ("C:/file///", ""),  # multiple trailing slashes, no file
        ("", ""),  # empty path
        ("/", ""),  # root directory, no file
        ("folder/subfolder/", ""),  # trailing slash, no file
        ("folder//subfolder//file.txt", "file.txt"),
    ],
)
def test_get_file_name(path, expected):
    """
    Test the get_file_name function.
    """
    assert get_file_name(path) == expected