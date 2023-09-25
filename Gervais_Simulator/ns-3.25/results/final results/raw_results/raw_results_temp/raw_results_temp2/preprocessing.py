import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load the dataset
dataset = pd.read_csv('dataset.csv')

# Separate features (X) and labels (y)
X = dataset.drop(columns=['Label'])
y = dataset['Label']

# Data Cleaning: Check for missing values
missing_values = X.isnull().sum()
print("Missing values:\n", missing_values)

# Data Normalization: Use Min-Max Scaler
min_max_scaler = MinMaxScaler()
X_normalized = min_max_scaler.fit_transform(X)

# Data Standardization: Use Standard Scaler
standard_scaler = StandardScaler()
X_standardized = standard_scaler.fit_transform(X_normalized)

# Split the dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X_standardized, y, test_size=0.2, random_state=42)

# Create a Random Forest Classifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the classifier
rf_classifier.fit(X_train, y_train)

# Predictions on the test set
y_pred = rf_classifier.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

