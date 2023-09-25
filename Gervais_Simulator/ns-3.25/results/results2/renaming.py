import os

# Path to the directory containing your CSV files
directory = '/home/erfan/workspace/selfish-project/selfish_mining/ns-3.25/results2'

#  List all files in the directory
files = os.listdir(directory)

# Filter out only the CSV files
csv_files = [file for file in files if file.endswith('.csv')]

# Sort the CSV files
csv_files.sort()

# Rename the CSV files with ordered names
for index, csv_file in enumerate(csv_files, start=1):
    old_path = os.path.join(directory, csv_file)
    new_name = 'benign_eachnode{}.csv'.format(index)
    new_path = os.path.join(directory, new_name)
    os.rename(old_path, new_path)
    print('Renamed: {} -> {}'.format(csv_file, new_name))

