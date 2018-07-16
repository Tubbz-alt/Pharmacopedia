# -*- coding: utf-8 -*-
"""
Pharmacy Counting.Py

DESCRIPTION

Analyzes and organizes medical pharmacy data. Using data from the Centers for
Medicare & Medicaid Services, this script calculates: (1) total number of
prescribers and (2) total prescriber expenditure for all listed drugs. Exports
analyzed data to text file with drugs organized by decreasing cost and, where
required, alphanumeric order. Created on 13:34:50 Wednesday, July 11, 2018.

Ths module contains functions required for import of raw medical pharmacy data.

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


## PRIMARY FUNCTIONS

def get_args(terminal_args):
    """
    Interprets terminal arguments as import path, export path, and sorting
    method.

    Args:
        terminal_args (list of strings): List of terminal arguments.

    Returns:
        import_path (string): path to input file.
        export_path (string): path to output file.
        is_alpha_sort (boolean): if True, sorting by alphanumeric characters
            and ignores special characters.

    Raises:
        IndexError: number of terminal arguments are unknown.
    """
    # Identifies number of arguments from terminal
    num_args = len(terminal_args) - 1
    # Prints number of arguments to terminal
    print("{} arguments identified.\nDrugs are sorted by total cost.".format(num_args))
    # If three arguments, sets import and export paths
    if num_args == 3:
        # Sets import path
        import_path = terminal_args[1]
        # Sets export path
        export_path = terminal_args[2]
        # Sets secondary sorting method
        is_alpha_sort = False
        # Prints secondary sorting method to terminal
        print("If necessary, drugs names are sorted according to alphanumeric and special characters.\n")
    # If four arguments, sets import path, export path, and secondary sorting
    # method
    elif num_args == 4:
        # Sets import path
        import_path = terminal_args[1]
        # Sets export path
        export_path = terminal_args[2]
        # If fourth argument matches, sets secondary sorting method to not
        # consider special characters
        if terminal_args[3].lower() in ["true", "1", "t", "y", "yes", "alpha"]:
            # Sets secondary sorting method to only alphanumeric characters
            is_alpha_sort = True
            # Prints secondary sorting method to terminal
            print("If necessary, drugs names are sorted according to alphanumeric characters only.\n")
        # Else, sets secondary sorting method to consider both alphanumeric
        # and special characters
        else:
            # Sets secondary sorting method to all characters
            is_alpha_sort = False
            # Prints secondary sorting method to terminal
            print("If necessary, drugs names are sorted according to alphanumeric and special characters.\n")
    # If not three or four arguments, raises index error
    else:
        # Raises error for incorrect number of arguments
        raise IndexError("Incorrect argument specification. See instructions in \"Read Me\" then run again.")
    # Prints input path to terminal
    print("\nImport file:\t{}\n".format(import_path))
    # Returns import path, export path, and secondary sorting method to script
    return import_path, export_path, is_alpha_sort

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
        raise FileNotFoundError("File not found in \"input\" directory.\nPlease confirm and run again.")
    # If output file already exists, raises file error
    if os.path.isfile(export_path):
        # Raises error for existing output file
        raise FileExistsError("File already exists in \"output\" directory.\nPlease back up, remove, and run again.")
    # Completes quality check for import path and export path
    return None

def import_data(import_path):
    """
    Collects, parses, and organizes data from imported file. See "Read Me" for
    more information.
    
    For each data
    entry or line, removes new line character and splits raw string according
    to comma delimiter. If "prescriber_last_name" is index 1 element, entry
    is identified as header row and skipped. Parsed entries are checked for
    incorrect parsing using the parse_check() function. Parsed data entries
    are assigned aliases. Collected data is stored in nested dictionary.
    Prescriber first and last name are stored as tuple and implemented as
    dictionary key for corresponding drug cost. Primary key is drug name,
    secondary key is prescriber name.

    Args:
        import_path (string): path to input file.

    Returns:
        all_data (nested dictionary): contains all collected, parsed, and
            organized data. Primary key is drug name (string), and primary
            value is sub-dictionary of prescribers (tuple of strings).
            Secondary key is prescriber name (string) and secondary value is
            drug cost (list of floats).
    """
    # Sets empty dictionary for import data
    all_data = {}
    # Safely opens and closes file for reading
    with open(import_path, 'r') as target_file:
        # Iterates over all data entries or lines
        for line in target_file:
            # Removes line breaks
            strip_line = line.strip("\n")
            # Splits by comma delimiter
            parsed_line = strip_line.split(",")
            # If True, data entry is file header
            if "prescriber_last_name" in parsed_line[1].lower():
                # Skips import of file header
                continue
            # Checks quality of parsed entry
            parse_check(parsed_line)
            # Sets prescriber last name (index 1) and first name (2),
            # drug name (3), and drug cost (4)
            prescriber_id, last_name, first_name, drug_name, drug_cost = parsed_line 
            # Sets tuple of prescriber full name
            prescriber_name = (last_name, first_name)
            # If drug does not exist in dictionary, adds new drug name
            if drug_name not in all_data:
                # For each new drug, creates initial prescriber sub-dictionary
                 all_data[drug_name] = {}
            # If prescriber is not assigned to drug, adds known prescriber
            if prescriber_name not in all_data[drug_name]:
                # For each new prescriber, creates initial cost list
                all_data[drug_name][prescriber_name] = []
            # Adds cost to drug's known prescribers
            all_data[drug_name][prescriber_name].append(float(drug_cost))
    # Returns all data as nested dictionary with prescriber name (1* key),
    # drug name (2* key), and drug cost (2* value) to script
    return all_data


## SECONDARY FUNCTIONS

def parse_check(parsed_line):
    """
    Investigates imported data integrity. Required by import_data() function.
    Requires alpha_only() and numbers_only() functions.

    Args:
        parsed_line (list of strings): contains strings parsed from data entry.

    Returns:
        None.
    """
    # If parsed entry does not have 5 elements, raises index error
    if len(parsed_line) != 5:
        # Raises error for more than 5 entry elements
        raise IndexError("Entry {} split incorrectly with {} elements.\nCheck then run again.".format(parsed_line[0], len(parsed_line)))
    # If prescriber ID has alphabetic characters, raises type error
    if not numbers_only(parsed_line[0]):
        #  Raises error that prescriber ID has alphabetic characters
        raise TypeError("Entry {} has prescriber ID which contains alphabetical characters.\nCheck then run again.".format(parsed_line[0]))
    # If prescriber last name has numeric characters, raises type error
    if not alpha_only(parsed_line[1]):
        #  Raises error that prescriber last name has numeric characters
        raise TypeError("Entry {} has prescriber last name \"{}\" which contains numerical characters.\nCheck then run again.".format(parsed_line[0], parsed_line[1]))
    # If prescriber first name has numeric characters, raises type errror
    if not alpha_only(parsed_line[2]):
        # Raises error that prescriber first name has numeric characters
        raise TypeError("Entry {} has prescriber first name \"{}\" which contains non-numeric characters.\nCheck then run again.".format(parsed_line[0], parsed_line[2]))
    # If drug cost has alphabetic characters, raises type error
    if not numbers_only(parsed_line[4]):
        # Raises error that drug cost has alphabetic characters
        raise TypeError("Entry {} has cost \"{}\" which contains non-numeric charaacters.\nCheck then run again.".format(parsed_line[0], parsed_line[4]))
    # Completes quality check for parsed data entry
    return None

def alpha_only(target_string):
    """
    Returns True if string contains all alphabetic and no numeric characters.
    Does not consider special characters. Checks quality of parsed prescriber
    first and last names.

    Args:
        target_string (string): string checked for alphabetic characters.

    Returns:
        (boolean): if True, only alphabetic or special characters in string.
    """
    # Returns True if string contains only alphabetic characters
    return all(char.isalpha() for char in target_string if char not in [".","\'"," ","-"])

def numbers_only(target_string):
    """
    Returns True if string contains all numeric and no alphabetic characters.
    Does not consider special characters. Checks quality of parsed
    prescriber ID and drug cost.

    Args:
        target_string (string): string checked for numeric characters.

    Returns:
        True (boolean): if only numeric or special characters in string.
    """
    # Returns True if string contains ony numeric characters
    return all(char.isdigit() for char in target_string if char not in [".","\'"," ","-"])


## MODULE METADATA

__author__ = 'Arthur D. Dysart'
__copyright__ = 'Copyright 2018, Pharmacy Counting'
__credits__ = ['Arthur D. Dysart']
__license__ = 'MIT License'
__version__ = '0.0.5'
__maintainer__ = 'Arthur D. Dysart'
__email__ = 'hi@arthurdys.art'
__status__ = 'closed'


## END OF MODULE