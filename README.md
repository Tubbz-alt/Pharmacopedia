![Pharmacopedia: The medical prescription database](https://s3.amazonaws.com/arthur-dysart-github-media/pharmacopedia/pharmapy_logo.png)
Pharmacopedia: The medical prescription database

Navigation
1. [QUICK START](README.md#Quick-start-guide)
2. [MECHANISMS](README.md#Mechanisms)
3. [REMARKS](README.md#Remarks)
4. [REQUIREMENTS](README.md#Requirements)
5. [CREDITS](README.md#Credits)

Pharmacopedia.Py (PharmaPy) enables online pharmacies to catalog prescriptions and analyze medical data. PharmaPy is compatible with comma-delimited text data from the Centers for Medicare & Medicaid Services. For each unique drug in its database, PharmaPy reports ***total cost*** and ***number of unique prescribers***. Analysis reports are organized by drug name in sequence of ***decreasing total cost*** and ***alphanumeric order***.

# Quick start guide

PharmaPy is built on Python 3.6 and requires the `os`, `sys`, and `warning` modules.

## Installation and setup
Download Github repository. Install Python version 3.6 and Git Bash; ensure Python and Bash are available on the operating system path. Put the input data file in the `input/` directory. Note PharmaPy only analyzes comma-delimited plaintext data which follow formatting guidelines of the Centers for Medicare & Medicaid Services.

PharmaPy analysis is executed using command line or shell script.

## Command line interface
Execute the following command:

```
python3    [main path]    [import path]    [export path]    [sorting option]
```

- **`python3`** indicates script execution using Python 3 interpreter.
- **`main path`** indicates main script location. From the home directory, the main path is `./src/Pharmacopedia.Py`.
- **`import path`** indicates input file location. Using sample data, the import path is `./input/itcont.txt`.
- **`export path`** indicates output file location. Using sample data, the export path is `./output/top_cost_drug.txt`.
- **`sorting option`** indicates handling of non-alphanumerics in sorting method. By default, it is set as `False`: non-alphanumerics in drug names are taken into account during sorting.

PharmaPy communicates with the user through the terminal.  Before analysis, the terminal indicates the number of terminal arguments, the primary and secondary sorting methods, and import path. After analysis, the terminal displays the export path and ends the script. 

![Pharmacopedia can be executed via command line](https://s3.amazonaws.com/arthur-dysart-github-media/pharmacopedia/cli_0.png)

## Shell script
Ensure source file exists in `input/` directory, and target file does not exist in `output/` directory. Execute `run.sh` in the home directory to import, analyze, and sort data. The preconfigured `run.sh` script analyzes sample data from `input/itcont.txt` source file and exports analysis results to `output/top_cost_drug.txt` target file.

![Pharmacopedia can be executed via shell script](https://s3.amazonaws.com/arthur-dysart-github-media/pharmacopedia/bash_0.png)

To analyze custom data, update import and export paths in `run.sh` using a text editor. Ensure data is comma-delimited plaintext and follows formatting guidelines of the Centers for Medicare & Medicaid Services. The shell script can also be executed in command line with command `bash run.sh` while in the home directory.

## Additional settings
In the advanced settings section of the `src/Pharmacopedia.py` main module, performance and behaviors can be controlled. During analysis, the terminal display can data entries containing non-alphanumeric ***unrecognized or unapproved characters***. By default, data warnings are hidden: warnings can be turned on by setting **`warning_display`** Boolean variable to `True`. The ***`cost_usd`*** setting controls precision of total drug cost: if 'True', final costs are rounded to nearest dollar instead of cent. The accepted alphanumeric, special, and escape characters – that is, characters that do not trigger data warning during parsing – can be modified by adding or removing characters to the **`safe_char`** list. Note that during drug sorting, all alphabetic characters are considered as their uppercase equivalents.

***Theses settings can be configured to "clean" data sets by ignoring un-approved characters.***

# Mechanisms

PharmaPy manages, processes, and displays data for all drugs in its knowledge base using Python’s built-in data analysis functions. Compatible input data is organized by prescriber: his or her information (viz., identification number, ID; first name; and last name) is associated with each prescription name and cost. PharmaPy exports data organized by drug: for each unique drug name, ***number of unique prescribers*** and ***total cost*** are reported in order of ***decreasing cost*** and ***alphanumeric order***. See Remarks section for technical detail about regex-free parsing, data integrity checking, and dictionary-based storage.

Before importing data, PharmaPy assesses performance settings. Arguments are retrieved from the user via terminal. The script inspects import and export paths: if either import or export path is invalid, `file not found` and `file already exists` errors are respectively raised and script execution is terminated.

Data is imported using Python’s built-in **`open()`** function and **`with… as`** statement, and parsed line-by-line according to comma delimiters. Each data component (viz., prescriber ID, last name, first name; drug name, cost) is split and identified by string position. Strings that contains non-delimiting commas will be excessively parsed by the **`str.split()`** function. However, PharmaPy automatically rectifies over-parsed strings by identifying surrounding double quotation marks (i.e., the character `"` ).

Imported data is stored in a nested-dictionary. The primary dictionary key is drug name, the secondary key is prescriber full name, and the secondary value is drug cost. Prescriber full name is represented as a two-element tuple containing the prescriber last name (index 0) and first name (index 1). To account for possibility of multiple costs for same drug by the same prescriber, drug costs are stored in lists.

Analysis of each drug calculates number of unique prescribers and gross cost. The number of prescribers is determined using set comprehensions for uniqueness and counting. The gross drug cost – that is, over all prescribers – is determined using list comprehension for net costs – that is, for each prescriber – and **`sum()`** function over all net costs.

In the analysis report, entries are ordered by decreasing cost. If more than one drug features the same cost, drugs are then sorted by name in alphanumeric order. Drug names, the keys of the analyzed data dictionary, are ranked using the **`sorted()`** function according to sorting keys of total cost and drug name. While sorting criteria may be modified, the original total cost and drug name values are unchanged between initial entry and final data output. The secondary sorting method – that is, whether to ignore or consider characters which do not appear in the **`safe_char`** list – is determined from the terminal arguments.

Data export is performed using Python’s built-in **`write()`** function. In correctly sorted order, analysis data is queried, formatted, and written to the new output text file. After writing all processed data, the file is automatically closed and the script run is complete.

# Remarks

PharmaPy is designed for robust data engineering without use of external libraries. The design of this script makes the following assumptions:
- Drug name should appear and be sorted exactly as shown in input data set
- Lowercase alphabetic characters are treated as uppercase characters only for sorting
- Prescribers with same last and first name are considered the same person
- For given drug and prescriber, drug cost can appear more than once
- All double quotation characters `"` are significant and cannot be typographical errors
- All input file entries containing less than 1 comma are considered empty lines 

A description of particular design strateigies is given below.

## Parsing and reconstruction
Survey of the sample data shows some alphanumeric strings are surrounded by double-quotation marks `"`. The consistent appearance of this character marks significance: the enclosed substring comprises an entire entry. If double-quotation marks surround a substring, then the substring contains comma characters `,` which are not intended to be delimiters.

Conventional string parsing by comma delimiters `,` fails in strings containing double-quotation marks `"`. This is because the ***`str.split()`*** function does not natively descriminate whether specified delimiters are active or inactive. To address this, PharmaPy rectifies and reconstructs substrings with incorrectly delimited comma characters using the ***`parse_line_custom()`*** function. This function analyzes strings containing double-quotation marks and pairs sequential elements which contain a single double-quotation mark. Elements between these target elements, inclusive of the targets themselves, are concatenated with a comma character `,` using the ***`str.join()`*** function. Similar approaches can be realized through the use of regular expressions to differentiate between delimiter-active and inactive comma characters [1, 2].

![Schematic of parsing and reconstruction functions](https://s3.amazonaws.com/arthur-dysart-github-media/pharmacopedia/reconstruction_schematic.png)

The ***`parse_warn()`*** function gives real-time information regarding data cleanliness and parsing quality. This function determines whether a data entry contains unapproved characters by comparsion with the specified ***`safe_char`*** list. A warning message, with the full data string, is displayed in the terminal if un-approved characters are found in the string. This feature is disabled if the ***`warning_display`*** advanced setting is set to `False`.

## Data entry and retrieval
PharmaPy's primary data structure is the nested dictionary. Dictionaries afford speed in storage and retrieval for big data analysis that does not require deep nesting [3]. The speed of key-based dictionary queries is at most of order 1 `O(1)` due to hashing data storage [4]. In comparison, lists require sequential iteration over its elements by index until query conditions are met. This results in speed of list queries to be proportional to the number of elements `O(n)` [4]. Individual prescriber costs are the secondary value of the imported data dictionary. These values are stored in lists to account for multiple costs for a given drug and prescriber.

To count unique prescribers, the total prescribers is queried with set comprehension. Collection of prescribers as a set rather than a list ensures duplicate entries, if existing, are ignored [4]. The hashing philosophy of sets also provide performance benefits [4].

## Dual sorting criteria
PharmaPy handles sorting using the ***`sorted()`*** function. This function enables conditional ordering based on specified key-determining functions [5]. For each drug, PharmaPy's key function calculates (1) negative of the total cost and (2) the safe-character corrected equivalent of drug name. Drug names, as the keys of the processed data dictionary, are sorted by these criteria and returned in the required order.

# Requirements

PharmaPy requires Python 3.6 and the `os`, `sys`, and `warning` modules. The script can be executed via Bash shell script or command line interface.

PharmaPy consists of four modules which must be located in the `src/` directory. The `src/Pharmacopedia.Py` module is the main script that controls data import, analysis, sorting, and export. The `src/DysartImport.Py` module contains all functions related to data import and parsing. The `src/DysartAnalysis.Py` module contains all functions related to data processing and sorting. The `src/DysartExport.Py` module contains all functions related to data formatting and exporting. The `src/DysartComm.Py` module contains all functions related to terminal display and communication, including error and warning reports.

# Credits

Pharmacopedia is a portmanteau of “pharmacopoeia,” a repository for pharmaceuticals, and “encyclopedia,” a reservoir for knowledge. This project was created by Arthur Dysart as part of the “Pharmacy Counting” coding project. Scripts developed using Spyder IDE.

During development, sample data was obtained from the Centers for Medicare & Medicaid Services. The pre-cleaned data includes medical physician names, unique identification numbers, prescribed drugs, and total drug cost.

# References

1. <a href="https://stackoverflow.com/questions/11456850">https://stackoverflow.com/questions/11456850</a>
2.  <a href="https://stackoverflow.com/questions/25501622">https://stackoverflow.com/questions/25501622</a>
3. <a href="https://stackoverflow.com/questions/3489071">https://stackoverflow.com/questions/3489071</a>
4. <a href="https://stackoverflow.com/questions/513882">https://stackoverflow.com/questions/513882</a>
5. <a href="https://docs.python.org/3/howto/sorting.html">https://docs.python.org/3/howto/sorting.html</a>
