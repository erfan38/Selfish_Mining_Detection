import os
import pandas as pd

# Path to the directory containing your CSV files
directory = '/home/erfan/workspace/selfish-project/selfish_mining/ns-3.25/benign_total'

files = os.listdir(directory)

# Filter out only the CSV files
csv_files = [file for file in files if file.endswith('.csv')]

# Sort the CSV files
csv_files.sort()
i=0
for csvfile in csv_files:
    i+=1
    print(i, csvfile,  len(pd.read_csv(os.path.join(directory, csvfile))))
# Read and merge CSV files
dataframes = [pd.read_csv(os.path.join(directory, csv_file)) for csv_file in csv_files]
merged_dataframe = pd.concat(dataframes, ignore_index=True)

# Path for the merged CSV file
merged_filename = 'merged.csv'
merged_filepath = os.path.join(directory, merged_filename)

# Write the merged DataFrame to a CSV file
merged_dataframe.to_csv(merged_filepath, index=False)

print('Merged CSV files into {}'.format(merged_filename))
