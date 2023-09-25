import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, precision_score, recall_score, f1_score
from prettytable import PrettyTable

dataset = pd.read_csv('dataset.csv')

X = dataset.drop(columns=['Label'])
y = dataset['Label']
print("Separating features (X) and labels (y) was done!")

#missing_values = X.isnull().sum()
#print("Missing values:\n", missing_values)

min_max_scaler = MinMaxScaler()
X_normalized = min_max_scaler.fit_transform(X)
print("Data Normalization was done!")

standard_scaler = StandardScaler()
X_standardized = standard_scaler.fit_transform(X_normalized)
print("Data Standardization was done!")

X_train, X_test, y_train, y_test = train_test_split(X_standardized, y, test_size=0.2, random_state=42)
print("Spliting the dataset was done!")

param_grid = {
    'n_estimators': [50, 100, 150],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
    # 'max_features': ['auto', 'sqrt', 'log2']
}

grid_search = GridSearchCV(RandomForestClassifier(random_state=42),
                           param_grid, cv=5, n_jobs=-1)
grid_search.fit(X_train, y_train)

best_rf_classifier = grid_search.best_estimator_
print("Best hyperparameters:", grid_search.best_params_)

cv_scores = cross_val_score(best_rf_classifier, X_train, y_train, cv=5)
print("Cross-validation scores:", cv_scores)
print("Mean CV accuracy:", cv_scores.mean())

y_pred_train = best_rf_classifier.predict(X_train)
train_accuracy = accuracy_score(y_train, y_pred_train)
print("Evaluating Misclassifications was done! ")
print("Training Accuracy:", train_accuracy)

# Predictions on the test set
y_pred_test = best_rf_classifier.predict(X_test)

print("Test Set Classification Report:")
print(classification_report(y_test, y_pred_test))

# Evaluate on unseen data (validation set)
X_train_new, X_val, y_train_new, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=42)
best_rf_classifier.fit(X_train_new, y_train_new)
y_val_pred = best_rf_classifier.predict(X_val)
val_accuracy = accuracy_score(y_val, y_val_pred)
print("Validation Accuracy:", val_accuracy)

# Create a table of results
data = [['Accuracy', val_accuracy],
        ['Precision', precision_score(y_val, y_val_pred, average='weighted')],
        ['Recall', recall_score(y_val, y_val_pred, average='weighted')],
        ['F1 Score', f1_score(y_val, y_val_pred, average='weighted')]]

fig, ax = plt.subplots(figsize=(8, 4))
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=data, colLabels=['Metric', 'Score'], cellLoc='center', loc='center')

# Formatting the table
table.auto_set_font_size(False)
table.set_fontsize(14)
table.scale(1.2, 1.2)

plt.show()
