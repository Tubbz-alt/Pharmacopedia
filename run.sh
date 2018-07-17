#!/bin/bash

# Runs Pharmacopedia.Py script with default input
python3 ./src/Pharmacopedia.py ./input/itcont.txt ./output/top_cost_drug.txt False

# Leaves terminal window open to display script responses
read -n 1 -s -r -p $'\n(Press any key to exit)\n'