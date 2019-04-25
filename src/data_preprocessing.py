#!/usr/bin/env python3
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

resource_dir = Path("./", "resources")

# Read in the full CSV file from ZIP file in 'resources' directory
data = pd.read_csv(
    Path(resource_dir, 'full_dataset.zip'),
    sep=',',
    header=None,
    compression='zip')

col_names = []

with open(Path(resource_dir, 'col_names.txt')) as cols_fp:
    for line_num, name in enumerate(cols_fp):
        col_names.append(name.rstrip())

# Set the column headers to the names from the Wireshark frame
data.columns = col_names

### Preprocess our minimized dataset ###

# Remove NULL values from our dataset

# Replace the '?' string in the DataFrame with a NumPy NaN value
data = data.replace('?', np.nan)

# If over 60% of the values in a column is null, remove it
prev_num_cols = len(data.columns)
data.dropna(axis='columns', thresh=len(data.index) * 0.40, inplace=True)
print("Removed " + str(prev_num_cols - len(data.columns)) +
      " columns with all NaN values.")

# Remove columns with no variation (zero values or only one unique value in it)
cols_to_drop = []

for col in data:
    if not data[col].nunique() > 1:
        cols_to_drop.append(col)

data.drop(columns=cols_to_drop, inplace=True)
print("Removed " + str(len(cols_to_drop)) +
      " columns with no variation in its values.")
print("DataFrame's current shape: " + str(data.shape))

# Clear the list of columns to drop for the accurate logging
cols_to_drop.clear()

for col in data:
    if data[col].nunique() >= (len(data.index) * 0.50):
        cols_to_drop.append(col)

data.drop(columns=cols_to_drop, inplace=True)
print("Removed " + str(len(cols_to_drop)) +
      " columns with over 50% variation in its values")

# Output the minimized and preprocessed dataset to a ZIP file (with no index column added)
data.to_csv(
    Path(resource_dir, 'preproc_dataset.zip'),
    sep=',',
    index=False,
    compression='zip')
