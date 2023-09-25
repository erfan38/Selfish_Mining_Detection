import pandas as pd

# Load the CSV file into a DataFrame
file_path = 'each_selfish.csv'
df = pd.read_csv(file_path)

# Keep rows with Node ID equal to 15
filtered_df = df[df['Node ID'] == 15]

# Write the filtered DataFrame to a new CSV file
output_file_path = 'each_selfish_1.csv'
filtered_df.to_csv(output_file_path, index=False)

print(f"Filtered data has been saved to {output_file_path}")

