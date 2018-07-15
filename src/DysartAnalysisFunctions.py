# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 16:54:06 2018

@author: arthur
"""

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


""" END OF MODULE """