import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score, classification_report

# Load the dataset
dataset = pd.read_csv('dataset.csv')

# Separate features (X) and labels (y)
X = dataset.drop(columns=['Label'])
y = dataset['Label']
print("Separating features (X) and labels (y) was done!")

# Normalize the data using Min-Max scaling
scaler = MinMaxScaler()
X_normalized = scaler.fit_transform(X)
print("Data Normalization was done!")

# Split the normalized data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X_normalized, y, test_size=0.2, random_state=42)
print("Splitting the dataset was done!")

# Define the hyperparameter grid for SVM
param_grid = {
    'C': [0.1, 1, 10],
    'kernel': ['linear', 'rbf'],
    'gamma': ['scale', 'auto']
}

# Perform grid search and find the best SVM model
grid_search = GridSearchCV(SVC(random_state=42), param_grid, cv=5, n_jobs=-1)
grid_search.fit(X_train, y_train)

best_svm_classifier = grid_search.best_estimator_
print("Best hyperparameters for SVM:", grid_search.best_params_)

# Cross-validation scores
cv_scores = cross_val_score(best_svm_classifier, X_train, y_train, cv=5)
print("Cross-validation scores for SVM:", cv_scores)
print("Mean CV accuracy for SVM:", cv_scores.mean())

# Training Accuracy
y_pred_train = best_svm_classifier.predict(X_train)
train_accuracy = accuracy_score(y_train, y_pred_train)
print("Training Accuracy for SVM:", train_accuracy)

# Test Set Classification Report
y_pred_test = best_svm_classifier.predict(X_test)
print("Test Set Classification Report for SVM:")
print(classification_report(y_test, y_pred_test))

# Split the training data again into training and validation sets
X_train_new, X_val, y_train_new, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=42)

# Fit the SVM model on the new training set
best_svm_classifier.fit(X_train_new, y_train_new)

# Predict on the validation set
y_val_pred = best_svm_classifier.predict(X_val)
val_accuracy = accuracy_score(y_val, y_val_pred)
print("Validation Accuracy for SVM:", val_accuracy)

