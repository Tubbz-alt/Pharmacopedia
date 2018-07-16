# -*- coding: utf-8 -*-
"""
Pharmacy Counting.Py

DESCRIPTION

Analyzes and organizes medical pharmacy data. Using data from the Centers for
Medicare & Medicaid Services, this script calculates: (1) total number of
prescribers and (2) total prescriber expenditure for all listed drugs. Exports
analyzed data to text file with drugs organized by decreasing cost and, where
required, alphanumeric order. Created on 16:54:06 Sunday, July 15, 2018.

Ths module contains functions required for analysis of raw medical pharmacy
data.

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


## PRIMARY FUNCTIONS

def analyze_data(all_data):
    """
    Calculates total cost and number of prescribers for each drug. All unique
    drugs (set of strings) determined using set comprehension. For each drug,
    number of prescribers (integer) determined by list comprehension wrapped
    with sum() function. For each prescriber, gross drug cost (list of floats)
    determined by list comprehension. Net drug cost, accounting for net
    prescriber costs for given drug, determined using prescriber drug costs
    wrapped by sum() function. Processed data saved in dictionary.

    Args:
        all_data (nested dictionary): contains all collected, parsed, and
            organized data. Primary key is drug name (string), and primary
            value is sub-dictionary of prescribers (tuple of strings).
            Secondary key is prescriber name (string) and secondary value is
            drug cost (list of floats).

    Returns:
        processed_data (dictionary): contains all analyzed data. Primary key
            is drug name (string), and primary value is tuple containing
            number of prescribers (integer, index 0) and total cost (float,
            index 1).
    """
    # Sets initial dictionary for analysis data
    processed_data = {}
    # Determines all unique drug names
    all_drugs = {drug for drug in all_data.keys()}
    # Iterates over all unique drug names
    for drug in all_drugs:
        # Creates set of all prescribers for given drug
        all_prescribers = {prescriber for prescriber in all_data[drug].keys()}
        # Calculates total number of prescribers
        num_prescribers = sum([ 1 for prescriber in all_prescribers ])
        # Calculates prescriber net drug cost
        prescriber_costs = [
            sum(all_data[drug][prescriber]) for prescriber in all_prescribers
        ]
        # Calculate gross prescriber cost for given drug
        total_cost = sum(prescriber_costs)
        # Sets tuple of number of prescribers (index 0) and total cost (1)
        processed_data[drug] = (num_prescribers, total_cost)
    # Returns dictionary of analyzed data
    return processed_data

def sort_drugs(processed_data, alpha_sort, **kwargs):
    """
    Sorts all drug names, as primary keys of processed data dictionary. Sorting
    is governed by primary criteria of decreasing cost, then secondary criteria
    of alphabetical order. Secondary criteria considers only alphanumeric
    characters if "alpha_sort" is True, or both alphanumeric and special
    characters if False. Requires sort_criteria() inner function.

    Args:
        processed_data (dictionary): contains all analyzed data. Primary key
            is drug name (string), and primary value is tuple containing
            number of prescribers (integer, index 0) and total cost (float,
            index 1).
        alpha_sort (boolean): if True, special characters are not considered
            during sorting. If False, special characters are considered during
            sorting.

    Returns:
        all_drugs_sorted (list of strings): contains all drug names in
            sequential list sorted by drug cost and alphanumeric name.
    """

    def sort_criteria(drug):
        """
        Determines mapped sorting value of cost and alphanumeric name for
        all drugs, as keys of processed data dictionary. Required by
        sort_drugs() outer function.

        Args:
            drug (string): drug name.

        Returns:
            (tuple): ordered and mapped sorting criteria of cost and name.
        """
        # Sets first criteria of decreasing drug cost
        cost_criteria = - processed_data[drug][1]
        # Sets second criteria of alphanumeric drug name
        name_criteria = drug.upper()
        # If True, does not consider special characters in alphanumeric order
        if alpha_sort:
            # Iterates over all characters in drug name
            for char in drug:
                # If character is not in safe list, remove from name criteria
                if char not in safe_char:
                    # Removes special characters
                    name_criteria = name_criteria.replace(char,"")
        # Returns primary and secondary sorting criteria
        return (cost_criteria, name_criteria)

    # Sets safe characters for evaluation of name criteria
    safe_char = kwargs['ch']
    # Sorts drug names by decreasing cost then alphanumeric order
    all_drugs_sorted = sorted(processed_data, key=sort_criteria)
    # Returns list of sorted drug names
    return all_drugs_sorted


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