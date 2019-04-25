from pathlib import Path

import numpy as np
import pandas as pd

# Create a path to the 'resources' directory in our repository
resource_dir = Path('./', 'resources')

# Read in the minimized dataset
data = pd.read_csv(
    Path(resource_dir, 'dataset-headers-reduced.zip'), sep=',', compression='zip')

# Replace the '?' string in the DataFrame with a NumPy NaN value
data.replace('?', np.nan, inplace=True)

# If over 60% of the values in a column is null, remove it
prev_num_cols = len(data.columns)
data.dropna(axis='columns', thresh=len(data.index) * 0.40, inplace=True)
print("Removed " + str(prev_num_cols - len(data.columns)) +
      " columns with all NaN values.")

# Drop the rows that have at least one NaN value in it
old_num_rows = data.shape[0]
data.dropna(inplace=True)
print("Removed " + str(old_num_rows -
                       data.shape[0]) + " rows with at least one NaN value in it.")

# Export the pandas DataFrame as a CSV file
data.to_csv(Path(resource_dir,
                 'dataset-headers-reduced-removed-null.csv'), index=False, sep=',')
