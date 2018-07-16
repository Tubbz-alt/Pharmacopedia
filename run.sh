#!/bin/bash

# Runs Pharmacy Counting script with default input
python ./src/ArthurDysartMain.py ./input/de_cc_data_7.txt ./output/de_cc_data_7_add.txt False

# Leaves terminal window open to display script responses
read -n 1 -s -r -p $'\n(Press any key to exit)\n'