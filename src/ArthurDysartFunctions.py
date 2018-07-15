# -*- coding: utf-8 -*-
"""
Date:   Wed Jul 11 13:34:50 2018
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


def parse_check(parsed_line):
    """
    Investigate integrity of imported data. Wrapped by "import_data" function.

    Args:
        parsed_line (list): List of parsed data to be investigated.

    Returns:
        None
    """

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


def analyze_data(all_data):
    """
    For each drug, calculate total cost and patient count.

    Args:
        drug (string): name of drug to query.

    Kwargs:
        all_data (dictionary): all raw data by primary key "id".
        processed_data (dictionary): all processed data by primary key "drug_name".

    Returns:
        None
    """
    # Initialize new dictionary for analyzed data
    processed_data = {}

    # Get all unique drug names
    all_drugs = { drug for drug in all_data.keys() }

    # Iterate over all unique drug names
    for drug in all_drugs:
        # For each drug, create list of all prescribers 
        all_prescribers = { prescriber for prescriber in all_data[drug].keys() }
        # For each drug, calculate number of prescribers
        num_prescribers = sum( [ 1 for prescriber in all_prescribers ] )

        # For each prescriber, sum his or her prescription costs
        prescriber_costs = [ sum(all_data[drug][prescriber]) for prescriber in all_prescribers ]
        # For each drug, calculate the sum of all prescribers' prescription costs
        total_cost = sum( prescriber_costs )

        # For each drug, save number of prescribers [0] and total cost [1] as tuple
        processed_data[drug] = ( num_prescribers, total_cost )

    # Deliver 1: dictionary of analyzed data and 2: set of all drug names
    return processed_data


def sort_drugs(processed_data, is_alpha_only):
    """
    For "all_drugs" dictionary, returns sorted keys as list of drug names.

    Args:
        all_drugs (dictionary): dictionary to be sorted by specified criteria.

    Returns:
        all_drugs_sorted (list of strings): drug names sorted by decreasing cost then name.
    """

    def sort_criteria(drug):
        """
        Sort "all_drugs" by keys cost and name. Wrapped by parent function "sort_drugs".

        Args:
            key_id (string): name of drug.

        Returns:
            (tuple): criteria of cost and name for sorting
        """
        # First, sort by cost in DECREASING order
        cost_criteria = - processed_data[drug][1]
        # Second, sort by drug name, or given key, in ALPHABETICAL order
        name_criteria = str(drug).upper()
        # Determine whether to ignore special characters
        if is_alpha_only == True:
            name_criteria = name_criteria.replace(" ","")
            name_criteria = name_criteria.replace("-","")
            name_criteria = name_criteria.replace("\'","")
        # Return primary and secondary sorting criteria
        return ( cost_criteria, name_criteria )

    # Sort keys of dictionary 'all_drugs' first by DESCREASING cost then alphabetically
    all_drugs_sorted = sorted(processed_data, key=sort_criteria)

    # Delivers list of sorted keys
    return all_drugs_sorted


def export_data(processed_data, all_drugs_sorted, export_path):
    """
    Write all entries to output file.

    Args:
        data_export (list of strings): list of all entries to be written to output file.
        target_path (string): path to output text file.

    Returns:
        None: output file written during procedure
    """
    # Safely open and close text file
    with open(export_path, 'w') as target_file:
        target_file.write("drug_name,num_prescriber,total_cost\n")
        # Iterate over whole export list
        for drug in all_drugs_sorted:
            # Extract "num_prescriber"
            num_prescriber = str( processed_data[drug][0] )
            total_cost = "{:.2f}".format( processed_data[drug][1] )
            # Create string of final values
            export_text = ",".join( [ str(drug), num_prescriber, total_cost ] )
            # Add line break to export string
            export_text = "".join( [ export_text, "\n" ] )
            # Write entire line to export
            target_file.write(export_text)

    # Target file already written during procedure
    return None


""" END OF MODULE """