import pandas as pd

# Read the CSV files
each_benign_1 = pd.read_csv("each_benign_1.csv")
total_benign = pd.read_csv("total_benign.csv")

# Merge the dataframes
merged_benign = pd.concat([each_benign_1, total_benign], axis=1)

# Save the merged dataframe to a new CSV file
merged_benign.to_csv("merged_benign.csv", index=False)

print("Merged CSV file created: merged_benign.csv")

