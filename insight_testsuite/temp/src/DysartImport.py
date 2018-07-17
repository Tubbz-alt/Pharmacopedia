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

Ths module contains functions required for import of raw data.

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


## REQUIRED LIBRARIES

# Enables warning and error communication via terminal
# Source: (home)/src/DysartComm.py
import DysartComm as adc


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
        alpha_sort (boolean): if True, sorting by alphanumeric characters
            and ignores special characters.

    Raises:
        IndexError: number of terminal arguments are unknown.
    """
    # Identifies number of arguments from terminal
    num_args = len(terminal_args) - 1
    # Prints number of arguments to terminal
    print(
        "{} arguments identified.\nDrugs are sorted "
        "by total cost.".format(num_args)
    )
    # If three arguments, sets import and export paths
    if num_args == 2:
        # Sets import path
        import_path = terminal_args[1]
        # Sets export path
        export_path = terminal_args[2]
        # Sets secondary sorting method
        alpha_sort = False
        # Prints secondary sorting method to terminal
        print(
            "If necessary, drugs names are sorted "
            "according to alphanumeric and special characters.\n"
        )
    # If four arguments, sets import path, export path, and secondary sorting
    # method
    elif num_args == 3:
        # Sets import path
        import_path = terminal_args[1]
        # Sets export path
        export_path = terminal_args[2]
        # If fourth argument matches, sets secondary sorting method to not
        # consider special characters
        if terminal_args[3].lower() in ["true", "1", "t", "y", "yes", "alpha"]:
            # Sets secondary sorting method to only alphanumeric characters
            alpha_sort = True
            # Prints secondary sorting method to terminal
            print(
                "If necessary, drugs names are sorted "
                "according to alphanumeric characters only.\n"
            )
        # Else, sets secondary sorting method to consider both alphanumeric
        # and special characters
        else:
            # Sets secondary sorting method to all characters
            alpha_sort = False
            # Prints secondary sorting method to terminal
            print(
                "If necessary, drugs names are sorted "
                "according to alphanumeric and special characters.\n"
            )
    # If not three or four arguments, raises index error
    else:
        # Raises error for incorrect number of arguments
        raise IndexError(
            "Incorrect argument specification. See "
            "instructions in \"Read Me\" then run again."
        )
    # Prints input path to terminal
    print("\nImport file:\t{}\n".format(import_path))
    # Checks integrity of input and export paths
    adc.check_paths(import_path, export_path)
    # Returns import path, export path, and sorting method to terminal
    return import_path, export_path, alpha_sort

def import_data(import_path, warn=False, **kwargs):
    """
    Collects, parses, and organizes data from imported file. For each data
    entry or line, removes new line character and splits raw string according
    to comma delimiter. If "prescriber_last_name" is index 1 element, entry
    is identified as header row and skipped. Parsed entries are checked for
    unsafe characters using the parse_line_custom() function. Parsed data
    entries are assigned aliases. Import data is stored in nested dictionary.
    Prescriber first and last name are stored as tuple and implemented as
    dictionary key for corresponding drug cost. Primary key is drug name,
    secondary key is prescriber name. See "Read Me" for more information.

    Args:
        import_path (string): path to input file.
        warn (boolean): if True, displays data entries with unsafe characters
            to the user terminal as warning.
        char (list of strings): contains all string characters considered safe.

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
            # If True, data entry is empty line
            if line.count(',') < 1:
                # Skips import of empty lines
                continue
            # Parses line intelligently to account for non-active commas
            parsed_line = parse_line_custom(line)
            # If True, data entry is file header
            if "prescriber_last_name" in parsed_line[1].lower():
                # Skips import of file header
                continue
            # If True, prints data entries with unsafe characters to terminal
            if warn:
                # Warns for data entries with unsafe characters 
                adc.parse_warn(*parsed_line, line=line, ch=kwargs['ch'])
            # Sets prescriber id (index 0), last name (1), and first name (2)
            prescriber_id, last_name, first_name = parsed_line[:3]
            # Sets drug name (index 3) and drug cost (4)
            drug_name, drug_cost = parsed_line[-2:]
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

def parse_line_custom(line):
    """
    Separates and splits data entry line based on comma delimiters and the
    presence of double-quation marks. In test data, double-quotation marks
    represent entry elements which contain at least one non-delimiting comma.
    After nondiscriminatory comma delimiting, over-delimited elements are 
    reconstructed according to the appearance of double-quotation marks.

    Args:
        line (string): single string of raw data from entry import.

    Returns:
        parsed_line (list of strings): contains correctly parsed line entry.
    """
    # Removes end line break
    line = line.replace("\n", "")
    # Splits line first by comma delimiter
    comma_split = line.split(",")
    # Counts number of double-quotation mark characters
    num_quotes = line.count("\"")
    # If number of double-quotation mark characters is not even, raise warning
    if num_quotes % 2 != 0:
        # Raises warning for uneven number of double-quotation mark characters
        # which suggests presence of unpaired double-quotation mark
        adc.parse_warn_quotes(comma_split[0])
    # If no double-quotation mark characters, splits line by comma delimiter
    if num_quotes == 0:
        # Splits line by comma delimiter only
        parsed_line = comma_split
    # If more than one double-quotation mark character, splits line according
    # to comma delimiter; when commas are enclosed by double-quotation mark
    # characters, merges enclosed comma-separated elements into single element
    else:
        # Sets length of comma-separated line vector
        i_range = range(0, len(comma_split))
        # Collects indicies of comma-separated line vector that contain only
        # one double-quotation mark character
        quote_indices = [i for i in i_range if comma_split[i].count("\"") == 1]
        # Sets number of double-quotation mark pairs
        num_quotes = range(0, len(quote_indices) // 2)
        # Collects all indicies with opening double-quotation mark characters
        open_quotes = quote_indices[0::2]
        # Collects all indicies with closing double-quotation mark characters
        close_quotes = quote_indices[1::2]
        # Pairs indicies with double-quotation mark characters according to
        # opening and closing positions
        quote_pairs = [(open_quotes[j], close_quotes[j]+1) for j in num_quotes]
        # Iterates over quote pairs in reverse order to perform reconstruction
        for p in reversed(quote_pairs):
            # Initalizes collection for reconstruction pieces
            line_parts = []
            # Sets index range for reconstruction
            cut_range = range(p[0], p[1])
            # Iterates over reconstruction range in reverse order
            for k in reversed(cut_range):
                # Removes specified element from comma-delimited list 
                cut_part = comma_split.pop(k)
                # Saves removed element into reconstruction list
                line_parts.append(cut_part)
            # Reverses elements of inverted reconstruction list
            reverse_recon = list(reversed(line_parts))
            # Concatenates collected parts for reconstruction
            fixed_split = ",".join(reverse_recon)
            # Inserts reconstructed part into original position in the comma-
            # delimited list
            comma_split.insert(p[0], fixed_split)
        # Sets final line split as reconstructed comma-delimited split
        parsed_line = comma_split
    # Returns final split 
    return parsed_line


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