def run_code(code):
    """
    Executes a given piece of code.
    
    Parameters:
    code (str): A string containing valid Python code.
    
    Returns:
    None
    """
    try:
        exec(code)
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
code_to_run = """
print('Hello, World!')
x = 5
y = 10
print('Sum:', x + y)
"""

run_code(code_to_run)
