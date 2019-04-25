from pathlib import Path

import numpy as np
import pandas as pd

# Create a path to the 'resources' directory in our repository
resource_dir = Path('./', 'resources')

# Create a list of columns that want to keep in our analysis (from Dr. Chung's webpage)
desired_cols = [2, 5, 45, 62, 64, 65, 68, 71, 74,
                75, 88, 91, 92, 105, 106, 110, 116, 120, 154]

# Specifically read in our desired columns from the reduced AWID dataset
data = pd.read_csv(
    Path(resource_dir, 'full_dataset.zip'),
    sep=',',
    compression='zip',
    usecols=desired_cols)

col_names = []

# Iterate over the text file containing the column names,
# if the line number matches one of our desired columns, add that name to a list
with open(Path(resource_dir, 'col_names.txt')) as cols:
    for line_num, col_name in enumerate(cols):
        if line_num in desired_cols:
            col_names.append(col_name.rstrip())

# Set the column headers to the names from the Wireshark frame
data.columns = col_names

# Replace the '?' string in the Pandas DataFrame with a NumPy NaN value
data.replace('?', np.nan, inplace=True)

# If over 60% of the values in a column is NaN, remove that column
# because it is not useful for our analysis
prev_num_cols = len(data.columns)
data.dropna(axis='columns', thresh=len(data.index) * 0.40, inplace=True)
print("Removed " + str(prev_num_cols - len(data.columns)) +
      " columns with all NaN values.")

# If there are no values or only one unique value in a column,
# remove that column because it is not useful for
# distinguishing between normal and attack type
cols_to_drop = []

for col in data:
    if not data[col].nunique() > 1:
        cols_to_drop.append(col)

data.drop(columns=cols_to_drop, inplace=True)
print("Removed " + str(len(cols_to_drop)) +
      " columns with no variation in its values.")

# Drop the rows that have at least one NaN value in it
old_num_rows = data.shape[0]
data.dropna(inplace=True)
print("Removed " + str(old_num_rows -
                       data.shape[0]) + " rows with at least one NaN value in it.")

# Export the pandas DataFrame as a CSV file
data.to_csv(
    Path(resource_dir, 'preproc_dataset.csv'),
    index=False,
    sep=',')
