import pandas as pd

original_dataset = pd.read_csv('dataset_copy.csv')

# Shuffle the dataset using the sample function
shuffled_dataset = original_dataset.sample(frac=1).reset_index(drop=True)

# Save the shuffled dataset to a new CSV file named 'shuffle_dataset.csv'
shuffled_dataset.to_csv('shuffle_dataset_copy.csv', index=False)

print("Dataset shuffled and saved as 'shuffle_dataset.csv'")

