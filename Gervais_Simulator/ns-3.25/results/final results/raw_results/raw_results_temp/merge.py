import pandas as pd

benign_eachnode = pd.read_csv('each_benign.csv')
benign_total = pd.read_csv('total_benign.csv')
selfish_eachnode = pd.read_csv('each_selfish.csv')
selfish_total = pd.read_csv('total_selfish.csv')

iterations = 100
nodes_per_iteration = 16

# Create a new 'Iteration' column for each dataset
benign_eachnode['Iteration'] = [i // nodes_per_iteration for i in range(len(benign_eachnode))]
benign_total['Iteration'] = [i for i in range(iterations)]

selfish_eachnode['Iteration'] = [i // nodes_per_iteration for i in range(len(selfish_eachnode))]
selfish_total['Iteration'] = [i for i in range(iterations)]

# Merge benign_eachnode and benign_total
benign_each_total = pd.merge(benign_eachnode, benign_total, on='Iteration')

# Merge selfish_eachnode and selfish_total
selfish_each_total = pd.merge(selfish_eachnode, selfish_total, on='Iteration')

# Add labels for benign and selfish data
benign_each_total['Label'] = 0
selfish_each_total['Label'] = 1

# Concatenate benign and selfish data
dataset = pd.concat([benign_each_total, selfish_each_total])

# Save the merged dataset to 'dataset.csv'
dataset.to_csv('dataset.csv', index=False)
