import pandas as pd

# Read the CSV files
df1 = pd.read_csv('total_benign.csv')
df2 = pd.read_csv('total_selfish.csv')

# Merge the datasets
merged_df = pd.concat([df1, df2], ignore_index=True)

# Save the merged dataset
merged_df.to_csv('dataset.csv', index=False)

