# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 16:58:34 2018

@author: arthur
"""

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