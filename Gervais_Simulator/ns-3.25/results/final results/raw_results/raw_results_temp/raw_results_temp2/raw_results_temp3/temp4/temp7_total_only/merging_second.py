import pandas as pd

# Load the two CSV files into dataframes
df_selfish = pd.read_csv('total_selfish.csv')
df_benign = pd.read_csv('total_benign.csv')

# Concatenate the dataframes vertically
merged_df = pd.concat([df_selfish, df_benign], ignore_index=True)

# Save the merged dataframe to a new CSV file
merged_df.to_csv('merged_total_final.csv', index=False)

