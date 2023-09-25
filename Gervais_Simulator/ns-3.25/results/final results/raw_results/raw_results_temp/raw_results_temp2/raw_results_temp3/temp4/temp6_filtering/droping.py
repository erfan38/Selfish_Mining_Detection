import pandas as pd

# Read the CSV file into a DataFrame
csv_file_path = 'shuffle_mereged_final.csv'
data_frame = pd.read_csv(csv_file_path)

# List the columns you want to drop
columns_to_drop = ['Stale Blocks']

# Drop the specified columns
data_frame.drop(columns=columns_to_drop, inplace=True)

# Save the modified DataFrame back to a CSV file
modified_csv_file_path = 'path/to/save/modified_file.csv'
data_frame.to_csv(modified_csv_file_path, index=False)

