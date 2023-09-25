import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
import time

train_df = pd.read_csv('reduced_dims_training.csv')
test_df = pd.read_csv('reduced_dims_testing.csv')

X_train = train_df[['Feature1']]
y_train = train_df['Label']

X_test = test_df[['Feature1']]
y_test = test_df['Label']

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

param_grid = {
    'n_estimators': [50, 100, 150],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

grid_search = GridSearchCV(RandomForestClassifier(random_state=42),
                            param_grid, cv=5, n_jobs=-1)


grid_search.fit(X_train_scaled, y_train)


best_params = grid_search.best_params_
best_model = grid_search.best_estimator_
start_time = time.time()
predictions = best_model.predict(X_test_scaled)
end_time = time.time()
computation_time = end_time - start_time

accuracy = accuracy_score(y_test, predictions)
precision = precision_score(y_test, predictions)
recall = recall_score(y_test, predictions)
f1 = f1_score(y_test, predictions)

data = [['Accuracy', accuracy],
        ['Precision', precision],
        ['Recall', recall],
        ['F1 Score', f1],
        ['Time Complexity', computation_time]]

fig, ax = plt.subplots(figsize=(8, 5))
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=data, colLabels=['Metric', 'Score'], cellLoc='center', loc='center')

table.auto_set_font_size(False)
table.set_fontsize(14)
table.scale(1.2, 1.2)

plt.show()

print("Best Hyperparameters:", best_params)
print("Time Complexity (sec):", computation_time)

