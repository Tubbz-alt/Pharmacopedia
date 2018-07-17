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

This is the main module which handles import, analysis, sorting, and export
of medical drug data.

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


## REQUIRED MODULES

# Retrives arguments from shell script
import sys


## REQUIRED LIBRARIES

# Retrives functions for data import
# Source: (home)/src/DysartImport.py
import DysartImport as ad1
# Retrives functions for data analysis
# Source: (home)/src/DysartAnalysis.py
import DysartAnalysis as ad2
# Retrives functions for data export
# Source: (home)/src/DysartExport.py
import DysartExport as ad3


## SCRIPT SETTINGS

# If None, sets traceback errors off (PRODUCTION mode)
sys.tracebacklimit = None
# If False, sets terminal warning display to off
warning_display = False
# If True, sets final cost display in dollars only
# If False, sets final cost display in dollars and cents
cost_usd = True
# Sets safe characters, which do not trigger warning, during parse check.
# Note all alphabetic characters are automatically converted into uppercase
# for sorting and parse check
safe_char = [
    "A","B","C","D","E","F","G","H","I","J","K","L","M",
    "N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
    "0","1","2","3","4","5","6","7","8","9",
    " ","-",".","%","&","/","(",")",",","#","\"","\'","\\",
]


## MAIN MODULE

if __name__ == "__main__":
    ## START SCRIPT
    # Displays script header in terminal
    print(
        "\nPharmacy Counting v1.0\n"
        "========================\n"
    )

    ## IMPORT DATA
    # Retrives and checks arguments from terminal
    import_path, export_path, alpha_sort = ad1.get_args(sys.argv)
    # Organizes data in nested dictionary according to drug (1* key),
    # prescriber (2* key), and cost (2* value). Also sets warnings 
    all_data = ad1.import_data(import_path, warn=warning_display, ch=safe_char)

    ## ANALYZE DATA
    # Calculates prescriber count (index 0) and cost (index 1) for each drug
    processed_data = ad2.analyze_data(all_data)
    # Sorts drugs by decreasing cost and alphanumeric order
    all_drugs_sorted = ad2.sort_drugs(processed_data, alpha_sort, ch=safe_char)

    ## EXPORT DATA
    # Writes ordered data to new file at export path
    ad3.export_data(processed_data, all_drugs_sorted, export_path, cost_usd)

    ## END SCRIPT
    # Displays script footer in terminal
    print("\nPharmacy counting complete.\n")
    # Displays file export path
    print("Export file:\t{}\n".format(export_path))


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