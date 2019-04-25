#!/usr/bin/env python3
import pandas as pd

desired_cols = [
    2, 5, 45, 62, 64, 65, 68, 71, 74, 75, 88, 91, 92, 105, 106, 110, 116, 120,
    154
]

# Read specific columns of CSV file from ZIP file in resources directory
data = pd.read_csv(
    "./resources/dataset.zip",
    sep=',',
    header=None,
    compression='zip',
    usecols=desired_cols)

col_names = []

with open('./resources/col_names.txt', 'r') as cols_fp:
    for line_num, name in enumerate(cols_fp):
        if line_num in desired_cols:
            col_names.append(name.rstrip())

# Set the column headers to the names from the Wireshark frame
data.columns = col_names

# Output the minimized dataset to a CSV file (with no index column added)
data.to_csv("./resources/min_dataset.csv", sep=',', index=False)
