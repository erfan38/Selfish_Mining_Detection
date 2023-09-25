import pandas as pd

# Load the CSV files
labels_df = pd.read_csv('test_labels.csv')
data_df = pd.read_csv('test_data.csv')

# Merge the two dataframes
merged_df = pd.concat([data_df, labels_df], axis=1)

# Save the merged dataframe to a new CSV file
merged_df.to_csv('merged_test_data.csv', index=False)

