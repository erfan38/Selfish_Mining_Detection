import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# Load standardized datasets
X_benign_standardized = pd.read_csv('benign_standardized2.csv')
X_selfish_standardized = pd.read_csv('selfish_standardized2.csv')

# Load target labels
target_column = "your_target_column_name_here"  # Replace with the actual target column name
y_benign = pd.read_csv('each_benign.csv')[target_column]
y_selfish = pd.read_csv('each_selfish.csv')[target_column]

# Split datasets into train and test sets
X_benign_train, X_benign_test, y_benign_train, y_benign_test = train_test_split(X_benign_standardized, y_benign, test_size=0.2, random_state=42)
X_selfish_train, X_selfish_test, y_selfish_train, y_selfish_test = train_test_split(X_selfish_standardized, y_selfish, test_size=0.2, random_state=42)

# Combine train and test data
X_train = pd.concat([X_benign_train, X_selfish_train], ignore_index=True)
y_train = pd.concat([y_benign_train, y_selfish_train], ignore_index=True)
X_test = pd.concat([X_benign_test, X_selfish_test], ignore_index=True)
y_test = pd.concat([y_benign_test, y_selfish_test], ignore_index=True)

# Create and train Random Forest Regressor
rfr = RandomForestRegressor(random_state=42)
rfr.fit(X_train, y_train)

# Make predictions
y_pred = rfr.predict(X_test)

# Calculate metrics
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print metrics
print(f"Mean Absolute Error: {mae:.2f}")
print(f"R-squared Score: {r2:.2f}")

