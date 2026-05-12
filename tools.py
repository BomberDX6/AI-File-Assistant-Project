import os

def read_file(filepath: str) -> str:
    """Reads the entire content of a local file."""
    if not os.path.exists(filepath):
        return f"Error: The file '{filepath}' does not exist."
    
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        return f"Error reading file '{filepath}': {str(e)}"

def search_file(filepath: str, keyword: str) -> str:
    """Searches for a specific keyword in a file and returns matching lines."""
    if not os.path.exists(filepath):
        return f"Error: The file '{filepath}' does not exist."
    
    matches = []
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            for line_num, line in enumerate(file, 1):
                if keyword.lower() in line.lower():
                    matches.append(f"Line {line_num}: {line.strip()}")
        
        if not matches:
            return f"No matches found for '{keyword}' in {filepath}."
        return "\n".join(matches)
    except Exception as e:
        return f"Error searching file '{filepath}': {str(e)}"