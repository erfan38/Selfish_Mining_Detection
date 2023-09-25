import pandas as pd


file_path = 'merged_each.csv'
data = pd.read_csv(file_path)

# List of columns to remove
columns_to_remove = [
    'EXT_INV Received Bytes', 'EXT_INV Sent Bytes',
    'EXT_GET_HEADERS Received Bytes', 'EXT_GET_HEADERS Sent Bytes',
    'EXT_HEADERS Received Bytes', 'EXT_HEADERS Sent Bytes',
    'EXT_GET_DATA Received Bytes', 'EXT_GET_DATA Sent Bytes',
    'Chunk Received Bytes', 'Chunk Sent Bytes'
]

# Drop the columns
data = data.drop(columns=columns_to_remove)

# Save the modified dataset to a new CSV file
modified_file_path = 'modified_merged_each.csv'  # Replace with your desired file path
data.to_csv(modified_file_path, index=False)
