import os


def get_file_path(path: str) -> str:
    """
    Extract directory path from a file path.
    
    Original Pascal function: GetFilePath
    
    Args:
        path: Full file path
        
    Returns:
        Directory portion of the path
    """
    return os.path.dirname(path)


def get_file_name(path: str) -> str:
    """
    Extract filename from a file path.
    
    Original Pascal function: GetFileName
    
    Args:
        path: Full file path
        
    Returns:
        Filename portion of the path
    """
    return os.path.basename(path)
