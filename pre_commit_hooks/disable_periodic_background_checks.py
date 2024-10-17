"""
disable_periodic_background_checks.py

This script is designed to parse Envelope project files and disable periodic
background checks by setting the value of all BACKGROUND_CHECK nodes to '0'.

Functions:
    _fix_file(filepath: str) -> bool:
        Parses an Envelope project file, looks for all BACKGROUND_CHECK nodes,
        and sets their values to '0' if they are not already '0'.
        Saves the modified Envelope project content back to the file if any
        changes were made.

    main(argv: Sequence[str] | None = None) -> int:
        The entry point of the script. Parses command-line arguments to get a
        list of filenames, processes each file using _fix_file, and prints a
        message if any file was modified.

Usage:
    To use this script, run it from the command line with a list of Envelope
    project filenames as arguments. The script will process each file and
    print a message if any modifications were made.

    Example:
        python disable_periodic_background_checks.py file1.prjx file2.prjx

Author:
    Mirco Dariol

Copyright:
    © 2024 Mirco Dariol. All rights reserved.
"""
from __future__ import annotations

import argparse
import re
from collections.abc import Sequence


def _fix_file(filepath: str) -> bool:
    """
    Parses an Envelope project file, looks for all BACKGROUND_CHECK nodes, and
    sets their values to '0' if they are not already '0'.
    Saves the modified Envelope project content back to the file if any
    changes were made.

    Args:
        filepath (str): The path to the Envelope project file to be processed.

    Returns:
        bool: Returns True if any BACKGROUND_CHECK nodes were modified,
        otherwise False.
    """
    pattern = r'(<BACKGROUND_CHECK>)(\b(?!0\b)\d+\b)(</BACKGROUND_CHECK>)'

    # Read the file content
    with open(filepath, encoding='utf-8') as file:
        content = file.read()

    match = re.search(pattern, content)
    if match:
        # Define the replacement string
        replacement = r'\g<1>0\g<3>'

        # Replace all occurrences of the pattern
        modified_content = re.sub(pattern, replacement, content)

        # Write updated content to the file
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(modified_content)

        return True
    return False


def main(argv: Sequence[str] | None = None) -> int:
    """
    The entry point of the script. Parses command-line arguments to get a list
    of filenames, processes each file using _fix_file, and prints a message if
    any file was modified.

    Args:
        argv (Sequence[str] | None): A list of command-line arguments.
                                     If None, sys.argv is used.

    Returns:
        int: Returns non-zero exit code in case of error or rule violations.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'filenames',
        nargs='*',
        help='Envelope project filenames to check.',
    )
    args = parser.parse_args(argv)

    return_code = 0
    for filename in args.filenames:
        try:
            if _fix_file(filename):
                print(f"Fixing {filename}")
                return_code = 1
        except Exception as exc:
            print(
                f"{filename}: Failed to disable periodic background checks. "
                f"Error: ({exc})",
            )
            return_code = 1
    return return_code


if __name__ == '__main__':
    raise SystemExit(main())
