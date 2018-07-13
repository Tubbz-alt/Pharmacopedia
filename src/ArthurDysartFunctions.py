# -*- coding: utf-8 -*-
"""
Date:   Wed Jul 11 13:34:50 2018
"""

""" REQUIRED MODULES """
# Check input and ouput paths from "run.sh" shell script
import os


""" FUNCTION DEFINITIONS """

def check_path(target_path, is_input_path=True):
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
    ## Check input path
    if is_input_path:
        # For input file, check path length
        if len(target_path) > 100:
            raise OSError("Input path is too long.\nShorten path and run again.")
        # For input file, ensure path exists
        if not os.path.isfile(target_path):
            raise OSError("Input file not found in \"input\" directory.\nPlease confirm run and again.")
    ## Check output path
    else:
        # For output file, check path length
        if len(target_path) > 100:
            raise OSError("Output path is too long.\nShorten path and run again.")
        # For output file, ensure path does not exist
        if os.path.isfile(target_path):
            raise OSError("Output file already exists in \"output\" directory.\nPlease back up, remove, and run again.")
        

    ## "target_path" passes integrity test
    return None


def parse_check(parsed_line):
    """
    Investigate integrity of imported data. Wrapped by "import_data" function.

    Args:
        parsed_line (list): List of parsed data to be investigated.

    Returns:
        None
    """

    def alphanumeric(target_string):
        """
        Investigate integrity of entry from imported data.
    
        Args:
            target_string (string): input string to be checked for numeric characters.
    
        Returns:
            (boolean): True if numeric characters found in name strings.
        """
        # Check for non-alphabetical characters in given string
        return any(char.isdigit() for char in target_string)

    def numeric(target_string):
        """
        Investigate integrity of entry from imported data.
    
        Args:
            target_string (string): input string to be checked for numeric characters.
    
        Returns:
            (boolean): True if numeric characters found in name strings.
        """
        # Check for non-alphabetical characters in given string
        return all(char.isdigit() for char in target_string)

    # Determine if correct parsing of data entry
    if len(parsed_line) != 5:
        # Data entry contains more than 5 elements
        raise IndexError("Entry {} split incorrectly.\nCheck then run again.".format(parsed_line[0]))
    # Determine if entry ID contains only numeric characters
    if not numeric(parsed_line[0]):
        # Entry ID contains alphabetical characters
        raise TypeError("Entry {} has ID which contains non-numeric charaacters.\nCheck then run again.".format(parsed_line[0]))
    # Determine if user last name contains only alphabetical characters
    if alphanumeric(parsed_line[1]):
        # User last name contains numeric characters
        raise TypeError("Entry {} has user last name which contains numbers.\nCheck then run again.".format(parsed_line[0]))
    # Determine if user first name contains only alphabetical characters
    if alphanumeric(parsed_line[2]):
        # User first name contains alphabetical characters
        raise TypeError("Entry {} has user first name which contains numbers.\nCheck then run again.".format(parsed_line[0]))
    # Determine if drug cost contains only numeric characters
    if not numeric(parsed_line[4]):
        # Drug cost contains alphabetical characters
        raise TypeError("Entry {} has cost which contains non-numeric charaacters.\nCheck then run again.".format(parsed_line[0]))
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
    imported_data = {}
    # Safely open and close text file
    with open(import_path, 'r', encoding="utf-8") as target_file:
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
            drug_id, last_name, first_name, drug_name, cost = parsed_line
            # Save parsed line into imported data
            imported_data[drug_id] = { "drug_name":drug_name, "last_name":last_name, "first_name":first_name, "cost":cost }

    # Wrap all data entries, as dictonary values from "imported_data", as "all_data"
    all_data = imported_data.values()
    # Return imported data as dictionary of parsed entries
    return all_data


def analyze_data(drug, all_data, processed_data):
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
    # Convert drug name to uppercase
    drug_name = drug.upper()

    # For each drug, find all unique users
    all_prescribers = { ( e['last_name'], e['first_name'] ) for e in all_data if e['drug_name'] == drug_name }
    # For each drug, calculate total patients
    num_prescriber = sum( [ 1 for prescriber in all_prescribers ] )

    # For each drug, find all costs
    all_costs = [ int(e['cost']) for e in all_data if e['drug_name'] == drug_name ]
    # For each drug, calculate total cost
    total_cost = sum( all_costs )

    # Update analyzed data dictionary with new drug data.
    processed_data[drug_name] = { 'total_cost':total_cost, 'num_prescriber':num_prescriber }

    # Output dictionary already updated during process
    return None


def sort_drugs(processed_data):
    """
    For "all_drugs" dictionary, returns sorted keys as list of drug names.

    Args:
        all_drugs (dictionary): dictionary to be sorted by specified criteria.

    Returns:
        drug_names_sorted (list of strings): drug names sorted by decreasing cost then name.
    """

    def sort_criteria(key_id):
        """
        Sort "all_drugs" by keys cost and name. Wrapped by parent function "sort_drugs".

        Args:
            key_id (string): name of drug.

        Returns:
            (tuple): criteria of cost and name for sorting
        """
        # First, sort by cost in DECREASING order
        cost_criteria = - processed_data[key_id]['total_cost']
        # Second, sort by drug name, or given key, in ALPHABETICAL order
        name_criteria = str(key_id)
        # Return primary and secondary sorting criteria
        return ( cost_criteria, name_criteria )

    # Sort keys of dictionary 'all_drugs' first by DESCREASING cost then alphabetically
    drug_names_sorted = sorted(processed_data, key=sort_criteria)

    # Delivers list of sorted keys
    return drug_names_sorted


def export_data(all_drugs_sorted, processed_data, export_path):
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
            num_prescriber = str( processed_data[drug]["num_prescriber"] )
            total_cost = str( processed_data[drug]["total_cost"] )
            # Create string of final values
            export_text = ",".join( [ drug, num_prescriber, total_cost ] )
            # Add line break to export string
            export_text = "".join( [ export_text, "\n" ] )
            # Write entire line to export
            target_file.write(export_text)

    # Target file already written during procedure
    return None


""" END OF MODULE """