#!/bin/bash

# Runs Pharmacopedia.Py script with default input
python ./src/Pharmacopedia.py ./input/itcont.txt ./output/top_cost_drug.txt False

# Leaves terminal window open to display script responses. Remove comment tag to ENABLE this feature
# read -n 1 -s -r -p $'\n(Press any key to exit)\n'