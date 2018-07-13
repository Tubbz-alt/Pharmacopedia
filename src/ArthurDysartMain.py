# -*- coding: utf-8 -*-
"""
Date:   Wed Jul 11 13:34:50 2018
"""

""" REQUIRED MODULES """
# Retrive arguments from "run.sh" shell script
import sys


""" FUNCTION DEFINITIONS """
# Functions from "./src/arthur_dysart_functions.py"
import ArthurDysartFunctions as ad


""" MAIN MODULE """
if __name__ == "__main__":
    # Set traceback errors off
    sys.tracebacklimit = None
    # Initialze input variables from terminal
    import_path = sys.argv[1]
    export_path = sys.argv[-1]
    # Start script
    print("Pharmacy Counting v1.0\n========================\n\nImporting file:\t{}\n".format(import_path))

    # Check import and export paths
    ad.check_path(import_path, is_input_path=True)
    ad.check_path(export_path, is_input_path=False)

    # Import and parse data into dictionary with "id" keys
    all_data = ad.import_data(import_path)

    # Get all UNIQUE drug names from each entry "e" in dictionary "all_data"
    all_drugs = { e['drug_name'].upper() for e in all_data }

    # Initialize new dictionary with analyzed data
    processed_data = {}
    # Iterate over each unique drug
    for drug in all_drugs:
        # For each drug, update "processed_data" with TOTAL cost and UNIQUE patient count
        ad.analyze_data(drug, all_data, processed_data)

    # Sort all drug names by 1: decreasing cost, then 2: alphabetical name (as key list)
    all_drugs_sorted = ad.sort_drugs(processed_data)

    ## Export data to new text file at "export_path"
    ad.export_data(all_drugs_sorted, processed_data, export_path)
    
    ## End script
    print("Pharmacy counting complete\n\nExported file:\t{}\n".format(export_path))

""" END OF MODULE """




















