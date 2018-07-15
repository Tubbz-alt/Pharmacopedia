# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 16:49:30 2018

@author: arthur
"""



""" REQUIRED MODULES """
# Check input and ouput paths from terminal arguments
import os


""" FUNCTION DEFINITIONS """


def get_args(terminal_args):
    """
    Interprets terminal arguments as import path, export path, and sorting method.

    Args:
        terminal_args (list of strings): From sys, contains terminal input.

    Returns:
        import_path (string): path to input file.
        export_path (string): path to output file.
        is_alpha_sort (boolean): True if will sort by alphabetical characters only.

    Raises:
        OSError: number of terminal arguments are unknown.
    """
    # Identify number of arguments in terminal
    num_args = len(terminal_args)
    print("{} arguments identified.\n".format(num_args))
    print( "Drugs are sorted by total cost." )
    # Check if two arguments specified in terminal
    if num_args == 3:
        # Initialze "import_path"
        import_path = terminal_args[1]
        # Initialze "export_path"
        export_path = terminal_args[2]
        # Initialize "is_alpha_sort"
        is_alpha_sort = False
        # Print acknowledgement in terminal
        print( "If necessary, drugs names are sorted according to all characters.\n" )
    # Check if three arguments specified in terminal
    elif num_args == 4:
        # Initialze "import_path"
        import_path = terminal_args[1]
        # Initialze "export_path"
        export_path = terminal_args[2]
        # Check "is_alpha_sort"
        if terminal_args[3].lower() in ["true", "1", "t", "y", "yes", "alpha"]:
            # Drug names will be sorted by alphanumeric characters only
            is_alpha_sort = True
            # Print acknowledgement in terminal
            print( "If necessary, drugs names are sorted according to alphanumeric characters only.\n" )
        # No matched "is_alpha_sort"
        else:
            # Drug names will be sorted by alphanumeric and other characters
            is_alpha_sort = False
            # Print acknowledgement in terminal
            print( "If necessary, drugs names are sorted according to all characters.\n" )

    # Unknown arguments from terminal
    else:
        raise OSError("Incorrect terminal specification. See \"Read Me\" for instructions then run again.")

    # Display input path in terminal
    print("\nImport file:\t{}\n".format(import_path))
    # Deliver values required from terminal input
    return import_path, export_path, is_alpha_sort


def check_paths(import_path, export_path):
    """
    Inspect quality of target path, then return target path on passed inspection.

    Args:
        is_input_path (boolean): determines path integrity check to perform.

    Returns:
        None

    Raises:
        OSError: input path length is too long or input file not found.
        OSError: output path length is too long or output file exists.
    """
    # For input file, ensure path exists
    if not os.path.isfile(import_path):
        raise OSError("Input file not found in \"input\" directory.\nPlease confirm run and again.")

    # For output file, ensure path does not exist
    if os.path.isfile(export_path):
        raise OSError("Output file already exists in \"output\" directory.\nPlease back up, remove, and run again.")

    ## Import and export paths pass integrity test
    return None


def import_data(import_path):
    """
    Import input file as strings. Wraps "parse_check" function.

    Args:
        import_path (string): path of input file with source data.

    Returns:
        all_data (dictionary): dictionary containing all read and parsed data.
    """
    # Initialize dictionary for imported data
    all_data = {}
    # Safely open and close text file
    with open(import_path, 'r') as target_file:
        # Iterate over whole file
        for line in target_file:

            # Remove line break character
            strip_line = line.strip("\n")
            # Split string by delimiter ","
            parsed_line = strip_line.split(",")
            # Check for header line
            if "id" in parsed_line[0]:
                # Skip header line
                continue
            # Check integrity of parsed line
            parse_check(parsed_line)

            # Assign elements of parsed line
            _id, last_name, first_name, drug_name, drug_cost = parsed_line
            # Assign tuple for patient identification
            patient_name = ( last_name, first_name )
            # Check if drug exists in dictionary; If not, add drug to dictionary
            if drug_name not in all_data:
                # For each new drug, initialize patient sub-dictionary
                 all_data[drug_name] = {}
            # Check if drug already purchased by patient; If not, add to drug's patient dictionary
            if patient_name not in all_data[drug_name]:
                # For each new patient for this drug, initialize list of purchases
                all_data[drug_name][patient_name] = []
            # Add cost to this patient's list of drug purchases
            all_data[drug_name][patient_name].append(float(drug_cost))

    # Deliver dictionary of patient name (1* key), drug name (1* value, 2* key), and cost (2* value)
    return all_data


"""
SUPPORTING FUNCTIONS
"""

def parse_check(parsed_line):
    """
    Investigate integrity of imported data. Wrapped by "import_data" function.

    Args:
        parsed_line (list): List of parsed data to be investigated.

    Returns:
        None
    """
    # Determine if correct parsing of data entry
    if len(parsed_line) != 5:
        # Data entry contains more than 5 elements
        raise IndexError("Entry {} split incorrectly with {} elements.\nCheck then run again.".format(parsed_line[0], len(parsed_line)))
    # Determine if entry ID contains only numeric characters
    if not numbers_only(parsed_line[0]):
        # Entry ID contains alphabetical characters
        raise TypeError("Entry {} has ID which contains non-numeric characters.\nCheck then run again.".format(parsed_line[0]))
    # Determine if user last name contains only alphabetical characters
    if not alpha_only(parsed_line[1]):
        # Prescriber last name contains numeric characters
        raise TypeError("Entry {} has prescriber last name \"{}\" which contains non-alpha characters.\nCheck then run again.".format(parsed_line[0], parsed_line[1]))
    # Determine if user first name contains only alphabetical characters
    if not alpha_only(parsed_line[2]):
        # Prescriber first name contains alphabetical characters
        raise TypeError("Entry {} has prescriber first name \"{}\" which contains non-numeric characters.\nCheck then run again.".format(parsed_line[0], parsed_line[2]))
    # Determine if drug cost contains only numeric characters
    if not numbers_only(parsed_line[4]):
        # Drug cost contains alphabetical characters
        raise TypeError("Entry {} has cost \"{}\" which contains non-numeric charaacters.\nCheck then run again.".format(parsed_line[0], parsed_line[4]))
    # Data entry passes integrity test
    return None


def alpha_only(target_string):
    """
    Investigate integrity of entry from imported data.

    Args:
        target_string (string): input string to be checked for numeric characters.

    Returns:
        (boolean): True if numeric characters found in name strings.
    """
    # Check for non-alphabetical characters in given string
    return all( char.isalpha() for char in target_string if char not in [".","\'"," ","-"] )


def numbers_only(target_string):
    """
    Investigate integrity of entry from imported data.

    Args:
        target_string (string): input string to be checked for numeric characters.

    Returns:
        (boolean): True if numeric or "." characters found in name strings.
    """
    # Check for non-alphabetical characters in given string
    return all( char.isdigit() for char in target_string if char not in [".","\'"," ","-"] )