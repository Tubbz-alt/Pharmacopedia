#!/bin/bash

# Open "pharmacy counting" script with default input
python ./src/ArthurDysartMain.py ./input/itcont.txt ./output/top_cost_drug.txt

# Leave terminal window open to allow user to view script responses
read -n 1 -s -r -p $'\n(Press any key to close terminal)'