import pandas as pd

# Load the datasets
benign_each = pd.read_csv('each_benign.csv')
selfish_each = pd.read_csv('each_selfish.csv')

# Add a label column to each dataset
benign_each['label'] = 0  # 0 for benign
selfish_each['label'] = 1  # 1 for selfish

# Concatenate the datasets
merged_data = pd.concat([benign_each, selfish_each], ignore_index=True)

# Save the merged dataset to a new CSV file
merged_data.to_csv('merged_each.csv', index=False)
