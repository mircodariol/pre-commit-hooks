"""
erase_vendor_code.py

This script is designed to parse Envelope project files and ensure that no
vendor code secrets are present.
The function looks for and erases the following tags:
- BATCH_CODE
- PATH_VENDOR_CODE
- VENDOR_CODE

Functions:
    _fix_file(filepath: str) -> bool:
        Parses an Envelope project file, and ensures that no vendor code
        secrets are present in the file itself.
        Erases the contents of BATCH_CODE, PATH_VENDOR_CODE, and VENDOR_CODE
        tags if they are found.
        Saves the modified Envelope project content back to the file if any
        changes were made.

    main(argv: Sequence[str] | None = None) -> int:
        The entry point of the script. Parses command-line arguments to get a
        list of filenames, processes each file using _fix_file, and prints a
        message if any file was modified.

Usage:
    To use this script, run it from the command line with a list of Envelope
    project filenames as arguments.
    The script will process each file and print a message if any modifications
    were made.

    Example:
        python erase_vendor_code.py file1.prjx file2.prjx

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
    Parses an Envelope project file, and ensure that no vendor code secrets are
    present in the file.
    The function looks for:
    - vendor code name (BATCH_CODE tag)
    - vendor code path (PATH_VENDOR_CODE tag)
    - vendor code (VENDOR_CODE tag)

    Args:
        filepath (str): The path to the Envelope project file to be processed.

    Returns:
        bool: Returns True if at least one secret has been erased,
        otherwise False.
    """
    # Read the file content
    with open(filepath, encoding='utf-8') as file:
        content = file.read()
    fixed = False

    # Declare an array of patterns to search for
    patterns = [
        r'(<BATCH_CODE>)(.+?)(</BATCH_CODE>)',
        r'(<PATH_VENDOR_CODE>)(.+?)(</PATH_VENDOR_CODE>)',
        r'(<VENDOR_CODE>)(.+?)(</VENDOR_CODE>)',
    ]

    for pattern in patterns:
        match = re.search(pattern, content)
        if match:
            fixed = True

            # Define the replacement string
            replacement = r'\g<1>\g<3>'

            # Replace all occurrences of the pattern
            content = re.sub(pattern, replacement, content)

    if fixed:
        # Write updated content to the file
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(content)

    return fixed


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
        'filenames', nargs='*', help='Envelope project filenames to check.',
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
                f"{filename}: Failed to remove vendor code secrets from "
                f"project. Error: ({exc})",
            )
            return_code = 1
    return return_code


if __name__ == '__main__':
    raise SystemExit(main())
