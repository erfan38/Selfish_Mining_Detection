import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('training.csv')

# Create separate DataFrames for each class
class_0 = df[df['Label'] == 0]
class_1 = df[df['Label'] == 1]

# Plot histograms for each class
plt.figure(figsize=(10, 6))

plt.hist(class_0['Mean Block Receive Time_x'], bins=15, alpha=0.5, label='Class 0', color='blue')
plt.hist(class_1['Mean Block Receive Time_x'], bins=15, alpha=0.5, label='Class 1', color='red')

plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()
plt.title('Histograms for Classes 0 and 1')
plt.show()

