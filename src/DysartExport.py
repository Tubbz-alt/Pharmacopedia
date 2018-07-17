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
required, alphanumeric order. Created on 16:58:34 Sunday, July 15, 2018.

Ths module contains functions required for export of analyzed medical pharmacy
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

def export_data(processed_data, all_drugs_sorted, export_path):
    """
    Formats and writes all entries to export file.

    Args:
        processed_data (dictionary): contains all analyzed data. Primary key
            is drug name (string), and primary value is tuple containing
            number of prescribers (integer, index 0) and total cost (float,
            index 1).
        all_drugs_sorted (list of strings): contains all drug names in
            sequential list sorted by drug cost and alphanumeric name.
        export_path (string): path to output file.

    Returns:
        None.
    """
    # Safely opens and closes file for writing
    with open(export_path, 'w') as target_file:
        # Creates header for output file
        target_file.write("drug_name,num_prescriber,total_cost\n")
        # Iterates over whole drug name list
        for drug in all_drugs_sorted:
            # Sets number of prescribers
            num_prescriber = "{}".format(processed_data[drug][0])
            # Sets total drug cost
            total_cost = "{:.2f}".format(processed_data[drug][1])
            # Creates final export string for given drug
            export_text = ",".join([drug,num_prescriber,total_cost])
            # Adds line break to final export string
            export_text = "".join([export_text,"\n"])
            # Writes data entry to output file
            target_file.write(export_text)
    # Completes analyzed data export during file writing
    return None


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