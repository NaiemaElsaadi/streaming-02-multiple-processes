"""
======================= INSTRUCTOR-GENERATED FILE =======================

This is an auxiliary script to assist with debugging and understanding
your Python environment and system setup. It is NOT part of the main project tasks.

You do NOT need to understand all the details or modify this file. 

Run this script before beginning your project. 
It will print information to the terminal and save it in a file named `about.txt`.
If you face issues, review this file and share its contents to help with debugging.

This script uses ONLY modules included in the Python standard library.
No additional installations are required.

To use, simply execute this script: `python about.py`

@Author: Denise Case
@Updated: 2023-08

==========================================================================

"""

# Import from Python Standard Library

import datetime
import os
import platform
import shutil
import sys

# Declare program constants (typically constants are named with ALL_CAPS)

DIVIDER = "=" * 70  # A string divider for cleaner output formatting
OUTPUT_FILENAME = "about.txt"  # File name for saving the debug information

# Retrieve additional system information using platform and os modules

build_date, compiler = platform.python_build()
implementation = platform.python_implementation()
architecture = platform.architecture()[0]
user_home = os.path.expanduser("~")


# Define program functions (bits of reusable code)


def get_terminal_info():
    """Determine the terminal and environment."""
    term_program = os.environ.get("TERM_PROGRAM", "")
    term_program_version = os.environ.get("TERM_PROGRAM_VERSION", "").lower()

    if term_program == "vscode":
        environment = "VS Code"
        if "powershell" in term_program_version:
            current_shell = "powershell"
        else:
            # Fallback approach for VS Code
            current_shell = (
                os.environ.get("SHELL", os.environ.get("ComSpec", ""))
                .split(os.sep)[-1]
                .lower()
            )
    else:
        environment = "Native Terminal"
        current_shell = (
            os.environ.get("SHELL", os.environ.get("ComSpec", ""))
            .split(os.sep)[-1]
            .lower()
        )

    return environment, current_shell


def get_source_directory_path():
    """
    Returns the absolute path to the directory containing this script.
    """
    dir = os.path.dirname(os.path.abspath(__file__))
    return dir


def is_git_in_path():
    """
    Checks if git is available in the PATH.

    Returns:
    - bool: True if git is in the PATH, otherwise False.
    """
    return shutil.which("git") is not None


def print_info_to_file(filename, content):
    """
    Print the provided content to a specified file.

    Args:
    - filename (str): Name of the file to save the content in.
    - content (str): The content to save.
    """
    with open(filename, "w") as f:
        f.write(content)


def get_header(fn):
    """
    Constructs a formatted string that provides helpful information.

    Args:
    - fn (str): Path to the file for which the information should be generated.

    Returns:
    - str: Formatted debug information.
    """

    environment, current_shell = get_terminal_info()

    return f"""
{DIVIDER}
{DIVIDER}
 Welcome to the Python Debugging Information Utility ABOUT.PY
 Date and Time: {datetime.date.today()} at {datetime.datetime.now().strftime("%I:%M %p")}
 Operating System: {os.name} {platform.system()} {platform.release()}
 System Architecture: {architecture}
 Number of CPUs: {os.cpu_count()}
 Machine Type: {platform.machine()}
 Python Version: {platform.python_version()}
 Python Build Date and Compiler: {build_date} with {compiler}
 Python Implementation: {implementation}
 Active pip environment: {os.environ.get('PIP_DEFAULT_ENV', 'None')}
 Path to Interpreter:         {sys.executable}
 Path to virtual environment: {sys.prefix}
 Current Working Directory:   {os.getcwd()}
 Path to source directory:    {get_source_directory_path()}
 Path to script file:         {fn}
 User's Home Directory:       {user_home}
 Terminal Environment:        {environment}
 Terminal Type:               {current_shell}
 Git available in PATH:       {is_git_in_path()} 
{DIVIDER}
{DIVIDER}
"""


# ---------------------------------------------------------------------------
# If this is the script we are running, then call some functions and execute code!
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    # We are using the get_header function and providing it with the path to this script.
    # This will generate the debug information for the current script.
    debug_info = get_header(__file__)

    # Print the debug information to the console.
    print(debug_info)

    # Print the debug information to a file named by the value in OUTPUT_FILENAME.
    print_info_to_file(OUTPUT_FILENAME, debug_info)
