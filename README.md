# Problem

Imagine you are a data engineer working for an online pharmacy. You are asked to generate a list of all drugs, the total number of UNIQUE individuals who prescribed the medication, and the total drug cost, which must be listed in descending order based on the total drug cost and if there is a tie, drug name. 

Disclosure: The projects that Insight Data Engineering Fellows work on during the program are much more complicated and interesting than this coding challenge. This challenge only tests you on the basics. 

# Input Dataset

The original dataset was obtained from the Centers for Medicare & Medicaid Services but has been cleaned and simplified to match the scope of the coding challenge. It provides information on prescription drugs prescribed by individual physicians and other health care providers. The dataset identifies prescribers by their ID, last name, and first name.  It also describes the specific prescriptions that were dispensed at their direction, listed by drug name and the cost of the medication. 

# Instructions

We designed this coding challenge to assess your coding skills and your understanding of computer science fundamentals. They are both prerequisites of becoming a data engineer. To solve this challenge you might pick a programing language of your choice (preferably Python, Scala, Java, or C/C++ because they are commonly used and will help us better assess you), but you are only allowed to use the default data structures that come with that programming language (you might use I/O libraries). For example, you can code in Python, but you should not use Pandas or any other external libraries. 

***The objective here is to see if you can implement the solution using basic data structure building blocks and software engineering best practices (by writing clean, modular, and well-tested code).*** 

# Output 

Your program needs to create the output file, `top_cost_drug.txt`, that contains comma (`,`) separated fields in each line.

Each line of this file should contain these fields:
* drug_name: the exact drug name as shown in the input dataset
* num_prescriber: the number of unique prescribers who prescribed the drug. For the purposes of this challenge, a prescriber is considered the same person if two lines share the same prescriber first and last names
* total_cost: total cost of the drug across all prescribers

For example

If your input data, **`itcont.txt`**, is
```
id,prescriber_last_name,prescriber_first_name,drug_name,drug_cost
1000000001,Smith,James,AMBIEN,100
1000000002,Garcia,Maria,AMBIEN,200
1000000003,Johnson,James,CHLORPROMAZINE,1000
1000000004,Rodriguez,Maria,CHLORPROMAZINE,2000
1000000005,Smith,David,BENZTROPINE MESYLATE,1500
```

then your output file, **`top_cost_drug.txt`**, would contain the following lines
```
drug_name,num_prescriber,total_cost
CHLORPROMAZINE,2,3000
BENZTROPINE MESYLATE,1,1500
AMBIEN,2,300
```

These files are provided in the `insight_testsuite/tests/test_1/input` and `insight_testsuite/tests/test_1/output` folders, respectively.


# Tips on getting an interview

## Writing clean, scalable and well-tested code

As a data engineer, it’s important that you write clean, well-documented code that scales for a large amount of data. For this reason, it’s important to ensure that your solution works well for a large number of records, rather than just the above example.

<a href="https://drive.google.com/file/d/1fxtTLR_Z5fTO-Y91BnKOQd6J0VC9gPO3/view?usp=sharing">Here</a> you can find a large dataset containing over 24 million records. Note, we will use it to test the full functionality of your code, along with other tests.

It's also important to use software engineering best practices like unit tests, especially since data is not always clean and predictable.

Before submitting your solution you should summarize your approach and run instructions (if any) in your `README`.

You may write your solution in any mainstream programming language, such as C, C++, C#, Go, Java, Python, Ruby, or Scala. Once completed, submit a link of your Github or Bitbucket repo with your source code.

In addition to the source code, the top-most directory of your repo must include the `input` and `output` directories, and a shell script named `run.sh` that compiles and runs the program(s) that implement(s) the required features.

If your solution requires additional libraries, environments, or dependencies, you must specify these in your `README` documentation. See the figure below for the required structure of the top-most directory in your repo, or simply clone this repo.

## Repo directory structure

The directory structure for your repo should look like this:

    ├── README.md 
    ├── run.sh
    ├── src
    │   └── pharmacy-counting.py
    ├── input
    │   └── itcont.txt
    ├── output
    |   └── top_cost_drug.txt
    ├── insight_testsuite
        └── run_tests.sh
        └── tests
            └── test_1
            |   ├── input
            |   │   └── itcont.txt
            |   |__ output
            |   │   └── top_cost_drug.txt
            ├── your-own-test_1
                ├── input
                │   └── your-own-input-for-itcont.txt
                |── output
                    └── top_cost_drug.txt

**Don't fork this repo** and don't use this `README` instead of your own. The content of `src` does not need to be a single file called `pharmacy-counting.py`, which is only an example. Instead, you should include your own source files and give them expressive names.

## Testing your directory structure and output format

To make sure that your code has the correct directory structure and the format of the output files are correct, we have included a test script called `run_tests.sh` in the `insight_testsuite` folder.

The tests are stored simply as text files under the `insight_testsuite/tests` folder. Each test should have a separate folder with an `input` folder for `itcont.txt` and an `output` folder for `top_cost_drug.txt`.

You can run the test with the following command from within the `insight_testsuite` folder:

    insight_testsuite~$ ./run_tests.sh 

On a failed test, the output of `run_tests.sh` should look like:

    [FAIL]: test_1
    [Thu Mar 30 16:28:01 PDT 2017] 0 of 1 tests passed

On success:

    [PASS]: test_1
    [Thu Mar 30 16:25:57 PDT 2017] 1 of 1 tests passed



One test has been provided as a way to check your formatting and simulate how we will be running tests when you submit your solution. We urge you to write your own additional tests. `test_1` is only intended to alert you if the directory structure or the output for this test is incorrect.

Your submission must pass at least the provided test in order to pass the coding challenge.

For a limited time we also are making available a <a href="http://ec2-18-210-131-67.compute-1.amazonaws.com/test-my-repo-link">website</a> that will allow you to simulate the environment in which we will test your code. It has been primarily tested on Python code but could be used for Java and C++ repos. Keep in mind that if you need to compile your code (e.g., javac, make), that compilation needs to happen in the `run.sh` file of your code repository. For Python programmers, you are able to use Python2 or Python3 but if you use the later, specify `python3` in your `run.sh` script.

# Instructions to submit your solution
* To submit your entry please use the link you received in your coding challenge invite email
* You will only be able to submit through the link one time 
* Do NOT attach a file - we will not admit solutions which are attached files 
* Use the submission box to enter the link to your GitHub or Bitbucket repo ONLY
* Link to the specific repo for this project, not your general profile
* Put any comments in the README inside your project repo, not in the submission box
* We are unable to accept coding challenges that are emailed to us 

# Questions?
Email us at cc@insightdataengineering.com












 
Pharmacopedia: The medical prescription database

Navigation
1. [QUICK START](README.md#problem)
2. [MECHANISMS](README.md#input-dataset)
3. [REMARKS](README.md#instructions)
4. [REQUIREMENTS](README.md#output)
5. [CREDITS](README.md#tips-on-getting-an-interview)

Pharmacopedia.Py (PharmaPy) enables online pharmacies to catalog prescriptions and analyze medical data. PharmaPy is compatible with comma-delimited text data from the Centers for Medicare & Medicaid Services. For each unique drug in its database, PharmaPy reports total drug cost and number of unique prescribers. Analysis reports are organized by drug name in sequence of decreasing total cost and alphanumeric order.

PharmaPy is built on Python 3.6 and requires the “OS”, “SYS”, and “WARNING” modules.

# Quick start guide

## Installation and setup
Download Github repository. Install Python version 3.6 and Git Bash; ensure Python and Bash are available on the OS system path. Put the input data file in the “input/” directory. Note PharmaPy only analyzes comma-delimited plaintext data which follow formatting guidelines of the Centers for Medicare & Medicaid Services.

PharmaPy analysis is executed using command line or shell script.

 
## Command line interface
Execute the following command:

python3	[main path]	[import path]	[export path] [optional: sorting method]
	
“python3” indicates script execution using Python 3 interpreter.
“main path” indicates main script location. From the “home” directory, the main path is “./src/Pharmacopedia.Py”.
“import path” indicates input file location. Using sample data, the import path is “./input/itcont.txt”.
“export path” indicates output file location. Using sample data, the export path is “./output/top_cost_drug.txt”.
“sorting method” indicates handling of non-alphanumerics in the sorting method. By default, non-alphanumerics in drug names are not ignored during sorting.

PharmaPy communicates with the user through the terminal.  Before analysis, the terminal indicates the number of terminal arguments, the primary and secondary sorting methods, and import path. During analysis, the terminal displays data entries containing unrecognized or questionable non-alphanumeric characters. After analysis, the terminal displays the export path and ends the script. 

 
## Shell script
Ensure source file exists in “input” directory, and target file does not exist in “output” directory. Execute “run.sh” in the home directory to import, analyze, and sort data. The preconfigured “run.sh” script analyzes sample data from “input/itcont.txt” source file and exports analysis results to “output/top_cost_drug.txt” target file.

To analyze custom data, update import and export paths in “run.sh” using a text editor. Ensure data is comma-delimited plaintext and follows formatting guidelines of the Centers for Medicare & Medicaid Services. The shell script can also be executed in command line with command “bash run.sh” while in the “home” directory.

## Additional settings
In the advanced settings section of the “./src/Pharmacopedia.py” main module, performance and behaviors can be controlled. Data warnings can be turned off by setting “warning_display” Boolean variable to “False”. The accepted alphanumeric, special, and escape characters – that is, characters that do not trigger data warning during parsing – can be modified by adding or removing characters to the “safe_char” list. Note that during drug sorting, all alphabetic characters are considered as their uppercase equivalents.

 
# Mechanisms
Using Python’s built-in data analysis functions, PharmaPy manages, processes, and displays data for all drugs in its knowledgebase. Compatible input data is organized by prescriber: his or her information (viz., identification number, ID; first name; and last name) is associated with each prescription name and cost. PharmaPy exports data organized by drug: for each unique drug name, number of unique prescribers and total cost are reported in order of decreasing cost and alphanumeric order. See “Remarks” for technical detail about regex-free parsing, data integrity checking, and dictionary-based storage.

Before importing data, PharmaPy assesses performance settings. Arguments are retrieved from the user via terminal. The script inspects import and export paths: if either import or export path is invalid, “file not found” and “file already exists” errors are respectively raised and script execution is terminated.

Data is imported using Python’s built-in “open()” function and “with… as” statement, and parsed line-by-line according to comma delimiters. Each data component (viz., prescriber ID, last name, first name; drug name, cost) is split and identified by string position. Strings that contains non-delimiting commas will be excessively parsed by the “str.split()” function. However, PharmaPy automatically rectifies over-parsed strings by identifying surrounding double quotation marks (i.e., the character " ).

Imported data is stored in a nested-dictionary. The primary dictionary key is drug name, the secondary key is prescriber full name, and the secondary value is drug cost. Prescriber full name is represented as a two-element tuple containing the prescriber last name (index 0) and first name (index 1). To account for possibility of multiple costs for same drug by the same prescriber, drug costs are stored in lists.

Analysis of each drug calculates number of unique prescribers and gross cost. The number of prescribers is determined using set comprehensions for uniqueness and counting. The gross drug cost – that is, over all prescribers – is determined using list comprehension for net costs – that is, for each prescriber – and “sum()” function over all net costs.

In the analysis report, entries are ordered by decreasing cost. If more than one drug features the same cost, drugs are then sorted by name in alphanumeric order. Drug names, the keys of the analyzed data dictionary, are ranked using the “sorted()” function according to sorting keys of total cost and drug name. While sorting criteria may be modified, the original total cost and drug name values are unchanged between initial entry and final data output. The secondary sorting method – that is, whether to ignore or consider characters which do not appear in the “safe_char” list – is determined from the terminal arguments.

Data export is performed using Python’s built-in “write()” function. In correctly sorted order, analysis data is queried, formatted, and written to the new output text file. After writing all processed data, the file is automatically closed and the script run is complete.

# Remarks
DICTIONARY DATA STRUCTURE.

INTELLIGENT PARSING.

CHARACTER CHECKING.

KEY-MODIFIED SORTING. PharmaPy handles sorting by 
 

# Requirements
PharmaPy requires Python 3.6 and the “OS”, “SYS”, and “WARNING” modules. The script can be executed via Bash shell script or command line interface.

The design of this script makes the following assumptions:
•	Drug name should appear and be sorted exactly as shown in input data set
•	Prescribers with same last and first name are considered to be the same person
•	For given drug and prescriber, drug cost can appear more than once

PharmaPy consists of four modules. The “./src/Pharmacopedia.Py” module is the main script that controls data import, analysis, sorting, and export. The “./src/DysartImport.Py” module contains all functions related to data import and parsing. The “./src/DysartAnalysis.Py” module contains all functions related to data processing and sorting. The “./src/DysartExport.Py” module contains all functions related to data formatting and exporting. The “./src/DysartComm.Py” module contains all functions related to terminal display and communication, including error and warning reports.

# Credits
Pharmacopedia is a portmanteau of “pharmacopoeia,” a repository for pharmaceuticals, and “encyclopedia,” a reservoir for knowledge. This project was created by Arthur Dysart as part of the “Pharmacy Counting” coding project. Scripts developed using Spyder IDE.

During development, sample data was obtained from the Centers for Medicare & Medicaid Services. The pre-cleaned data includes medical physician names, unique identification numbers, prescribed drugs, and total drug cost.

# References
https://stackoverflow.com/questions/11456850
https://stackoverflow.com/questions/25501622
