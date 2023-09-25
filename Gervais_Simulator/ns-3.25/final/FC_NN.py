import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt
import time



data = pd.read_csv('shuffle_6f.csv')

X = data.drop('Label', axis=1)
y = data['Label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Sequential model
model = keras.Sequential()

for _ in range(12):
    model.add(keras.layers.Dense(12, activation='relu'))

model.add(keras.layers.Dense(1, activation='sigmoid'))


model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
start_time_train = time.time()
history = model.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_test, y_test))
end_time_train = time.time()

start_time_test = time.time()
y_pred = (model.predict(X_test) > 0.5).astype(int)
end_time_test = time.time()

computation_time_test = end_time_test - start_time_test
computation_time_train = end_time_train - start_time_train
# Calculate evaluation metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

# Create a table of results
data = [['Accuracy', accuracy],
        ['Precision', precision],
        ['Recall', recall],
        ['F1 Score', f1],
        ['Computation time of train', computation_time_train],
        ['Computation time of test ', computation_time_test]]

# Display the results in a table
fig, ax = plt.subplots(figsize=(8, 5))
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=data, colLabels=['Metric', 'Score'], cellLoc='center', loc='center')

# Formatting the table
table.auto_set_font_size(False)
table.set_fontsize(14)
table.scale(1.2, 1.2)

plt.savefig('D2_FC_NN.png')  # Save the figure as an image
plt.show()

print("Time Complexity (sec):", computation_time_train, computation_time_test)
