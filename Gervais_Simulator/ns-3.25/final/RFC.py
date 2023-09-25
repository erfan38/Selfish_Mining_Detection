import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.preprocessing import StandardScaler  # Import StandardScaler
from matplotlib.table import Table
import time


train_df = pd.read_csv('reduced_dims_training.csv')
test_df = pd.read_csv('reduced_dims_testing.csv')

X_train = train_df.iloc[:, :-1]
y_train = train_df.iloc[:, -1]

X_test = test_df.iloc[:, :-1]
y_test = test_df.iloc[:, -1]

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

start_time_train = time.time()
rfc = RandomForestClassifier()
rfc.fit(X_train_scaled, y_train)
end_time_train = time.time()

start_time = time.time()
predictions = rfc.predict(X_test_scaled)
end_time = time.time()
computation_time_test = end_time - start_time
computation_time_train = end_time_train - start_time_train

accuracy = accuracy_score(y_test, predictions)
precision = precision_score(y_test, predictions)
recall = recall_score(y_test, predictions)
f1 = f1_score(y_test, predictions)

data = [['Accuracy', accuracy],
    ['Precision', precision],
    ['Recall', recall],
    ['F1 Score', f1],
    ['Time Complexity of test', computation_time_test],
    ['Time complexity of train', computation_time_train]]

fig, ax = plt.subplots(figsize=(8, 5))
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=data, colLabels=['Metric', 'Score'], cellLoc='center', loc='center')

table.auto_set_font_size(False)
table.set_fontsize(14)
table.scale(1.2, 1.2)

plt.show()

print("Time Complexity (sec):", computation_time_test, computation_time_train)
