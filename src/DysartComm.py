# -*- coding: utf-8 -*-
"""
Pharmacopedia.Py v1.0
Pharmacy Counting Project
Arhur D. Dysart


DESCRIPTION

Analyzes and organizes medical pharmacy data. Using data from the Centers for
Medicare & Medicaid Services, this script calculates: (1) total number of
prescribers and (2) total prescriber expenditure for all listed drugs. Exports
analyzed data to text file with drugs organized by decreasing cost and, where
required, alphanumeric order. Created on 13:34:50 Wednesday, July 11, 2018.

Ths module contains communication functions used during parsing data or in
degub mode.

Script metadata available at end of module.


MIT LICENSE

Copyright (c) 2018 Arthur D. Dysart

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


## REQUIRED MODULES

# Checks file existence in input and export paths
import os
# Enables display of warnings in terminal
import warnings as wn


## PRIMARY FUNCTIONS

def check_paths(import_path, export_path):
    """
    Inspects for file errors in import and export paths.

    Args:
        import_path (string): path to input file.
        export_path (string): path to output file.

    Returns:
        None.

    Raises:
        FileNotFoundError: file does not exist on input path.
        FileExistsError: file exists on output path.
    """
    # If input file cannot be found, raises file error
    if not os.path.isfile(import_path):
        # Raises error for non-existent input file
        raise FileNotFoundError(
            "File not found in \"input\" directory.\n"
            "Please confirm and run again."
        )
    # If output file already exists, raises file error
    if os.path.isfile(export_path):
        # Raises error for existing output file
        raise FileExistsError(
            "File already exists in \"output\" directory."
            "\nPlease back up, remove, and run again."
        )
    # Completes quality check for import path and export path
    return None

def parse_warn(*args, **kwargs):
    """
    Reports unsafe data entries to user via terminal.

    Args:
        parsed_line (list of strings): contains strings parsed from data entry.
        line (string): original data entry as single string.
        safe_char (list of strings): contains all safe characters.

    Returns:
        None.

    Raises:
        Warning: Unsafe character found in prescriber last name.
        Warning: Unsafe character found in prescriber first name.
        Warning: Unsafe character found in drug name.
    """
    # Sets prescriber first name (index 1), last name (2), and drug name (3)
    last_name, first_name, drug_name = args[1],args[2], args[3]
    # Sets raw data entry line
    line = kwargs['line']
    # Sets safe characters list
    safe_char = kwargs['ch']
    # If unsafe character in prescriber last name, warn in terminal
    if any(char for char in last_name.upper() if char not in safe_char):
        # Raises warning for unsafe character in prescriber last name
        wn.warn("(last_name):: {}".format(line))
    # If unsafe character in prescriber first name, warn in terminal
    elif any(char for char in first_name.upper() if char not in safe_char):
        # Raises warning for unsafe character in prescriber first name
        wn.warn("(first_name):: {}".format(line))
    # If unsafe character in drug name, warn in terminal
    elif any(char for char in drug_name.upper() if char not in safe_char):
        # Raises warning for unsafe character in drug name
        wn.warn("(drug_name):: {}".format(line))
    # Passes parse character test
    return None

def parse_warn_quotes(prescriber_id):
    """
    Returns statement to terminal stating presence of unpaired double-quotation
    mark. Suggests typographic error with insignificant double-quotation mark
    character.

    Args:
        prescriber_id (string): contains index-0 string parsed from data entry.

    Returns:
        None.

    Raises:
        Warning: Unsignificant double-quotation mark may jeopardize parsing
            integrity.
    """
    # Raises warning for uneven number of double-quotation mark characters
    # suggesting unpaired quotation mark
    wn.warn(
        "Entry with ID {} has an unpaired double-quotation mark, and likely "
        "to be incorrectly parsed. Check for typographic errors and run "
        "again.".format(prescriber_id)
    )
    # Completes warning procedure
    return None


## SECONDARY FUNCTIONS

def parse_error(parsed_line, **kwargs):
    """
    Investigates imported data integrity. Required by import_data() function.
    Requires alpha_only() and numbers_only() functions. Depreciated in module
    version 1.0.0. Use for DEBUG only.

    Args:
        parsed_line (list of strings): contains strings parsed from data entry.

    Returns:
        None.
    """
    # Sets safe characters list
    safe_char = kwargs['safe_char']
    # If parsed entry does not have 5 elements, raises index error
    if len(parsed_line) != 5:
        # Raises error for more than 5 entry elements
        print(parsed_line)
        raise IndexError(
            "Entry with ID {} split incorrectly with {} elements."
            "\nCheck then run again.".format(parsed_line[0], len(parsed_line))
        )
    # If prescriber ID has alphabetic characters, raises type error
    if not numbers_only(parsed_line[0], safe_char):
        print(parsed_line)
        #  Raises error that prescriber ID has alphabetic characters
        raise TypeError(
            "Entry with ID {} has prescriber ID which contains alphabetical "
            "characters.\nCheck then run again.".format(parsed_line[0])
        )
    # If prescriber last name has numeric characters, raises type error
    if not alpha_only(parsed_line[1], safe_char):
        print(parsed_line)
        #  Raises error that prescriber last name has numeric characters
        raise TypeError(
            "Entry with ID {} has prescriber last name \"{}\" which contains "
            "numerical characters.\nCheck then run "
            "again.".format(parsed_line[0], parsed_line[1])
        )
    # If prescriber first name has numeric characters, raises type errror
    if not alpha_only(parsed_line[2], safe_char):
        print(parsed_line)
        # Raises error that prescriber first name has numeric characters
        raise TypeError(
            "Entry with ID {} has prescriber first name \"{}\" which contains "
            "non-numeric characters.\nCheck then run "
            "again.".format(parsed_line[0], parsed_line[2])
        )
    # If drug cost has alphabetic characters, raises type error
    if not numbers_only(parsed_line[4], safe_char):
        print(parsed_line)
        # Raises error that drug cost has alphabetic characters
        raise TypeError(
            "Entry with ID {} has cost \"{}\" which contains non-numeric "
            "charaacters.\nCheck then run "
            "again.".format(parsed_line[0], parsed_line[4])
        )
    # Completes quality check for parsed data entry
    return None

def alpha_only(target_string, safe_char):
    """
    Returns True if string contains all alphabetic and no numeric characters.
    Does not consider special characters. Checks quality of parsed prescriber
    first and last names. Depreciated in module version 1.0.0.
    Use for DEBUG only.

    Args:
        target_string (string): string checked for alphabetic characters.
        safe_char (list of strings): string to be considered for sorting.

    Returns:
        (boolean): if True, only alphabetic or special characters in string.
    """
    # Returns True if string contains only alphabetic characters
    return all(ch.isalpha() for ch in target_string if ch not in safe_char)

def numbers_only(target_string, safe_char):
    """
    Returns True if string contains all numeric and no alphabetic characters.
    Does not consider special characters. Checks quality of parsed
    prescriber ID and drug cost. Depreciated in module version 1.0.0.
    Use for DEBUG only.

    Args:
        target_string (string): string checked for numeric characters.
        safe_char (list of strings): string to be considered for sorting.

    Returns:
        True (boolean): if only numeric or special characters in string.
    """
    # Returns True if string contains ony numeric characters
    return all(ch.isdigit() for ch in target_string if ch not in safe_char)


## MODULE METADATA

__author__ = 'Arthur D. Dysart'
__copyright__ = 'Copyright 2018, Pharmacopedia.Py'
__credits__ = ['Arthur D. Dysart']
__license__ = 'MIT License'
__version__ = '1.0.0'
__maintainer__ = 'Arthur D. Dysart'
__email__ = 'hi@arthurdys.art'
__status__ = 'closed'


## END OF MODULE