# -*- coding: utf-8 -*-
"""
Date:   Wed Jul 11 13:34:50 2018
"""


""" REQUIRED MODULES """
# Retrive arguments from "run.sh" shell script
import sys


""" FUNCTION DEFINITIONS """
# Fnctions for data import from:    "./src/DysartImportFunctions.py"
import DysartImportFunctions as ad1
# Functions for data analysis from:    "./src/DysartAnalysisFunctions.py"
import DysartAnalysisFunctions as ad2
# Functions for data export from:    "./src/DysartExportFunctions.py"
import DysartExportFunctions as ad3


""" VARIABLE DEFINITIONS """
# Get input variables from terminal
terminal_args = sys.argv
# Set traceback errors off
sys.tracebacklimit = None


""" MAIN MODULE """
if __name__ == "__main__":
    ## START SCRIPT
    # Display script header text in terminal
    print("Pharmacy Counting v1.0\n========================\n")

    ## IMPORT DATA
    # Get script arguments from terminal
    import_path, export_path, is_alpha_sort = ad1.get_args(terminal_args)
    # Check import and export paths
    ad1.check_paths(import_path, export_path)
    # Parse and organize data by drug (1* key), prescriber (1* value, 2* key), then cost (2* value)
    all_data = ad1.import_data(import_path)

    ## ANALYZE DATA
    # For each drug (1* key), prepare list with number of prescribers (index 0) and cost (index 1)
    processed_data = ad2.analyze_data(all_data)
    # Sort all drug names by 1: decreasing cost, then 2: drug name
    all_drugs_sorted = ad2.sort_drugs(processed_data, is_alpha_sort)
    
    ## EXPORT DATA
    # Save data in srted order to new text file at export path
    ad3.export_data(processed_data, all_drugs_sorted, export_path)

    ## END SCRIPT
    # Display finalization text in terminal
    print("\nPharmacy counting complete.\n")
    # Display output file path
    print("Export file:\t{}\n".format(export_path))


""" END OF MODULE """

