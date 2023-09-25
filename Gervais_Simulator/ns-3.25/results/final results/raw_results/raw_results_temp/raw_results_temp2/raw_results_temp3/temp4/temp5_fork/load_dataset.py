import numpy as np

# Specify the path to the .npy file
dataset_path = '/home/erfan/Downloads/ForkDec_SM_Detection/data/data_set/test_labels_0.49_.npy'

# Load the dataset using np.load()
dataset = np.load(dataset_path)

# Specify the path to save the CSV file
csv_path = '/home/erfan/Downloads/ForkDec_SM_Detection/data/data_set/test_labels_0.49_.csv'

# Save the dataset as a CSV file
np.savetxt(csv_path, dataset, delimiter=',')

# Print a message to indicate that the CSV file has been saved
print('Dataset saved as CSV successfully.')

