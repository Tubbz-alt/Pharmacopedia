#!/bin/bash

# Runs Pharmacy Counting script with default input
python ./src/ArthurDysartMain.py ./input/itcont.txt ./output/top_cost_drug.txt True

# Leaves terminal window open to display script responses
read -n 1 -s -r -p $'\n(Press any key to exit)\n'