import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.impute import SimpleImputer 

# Load CSV files
each_benign_df = pd.read_csv('each_benign.csv')
total_benign_df = pd.read_csv('total_benign.csv')
each_selfish_df = pd.read_csv('each_selfish.csv')
total_selfish_df = pd.read_csv('total_selfish.csv')

# Combine the dataframes
dfs = [each_benign_df, total_benign_df, each_selfish_df, total_selfish_df]

# Clean the data (remove rows with missing values)
cleaned_dfs = [df.dropna() for df in dfs]

# Combine all data into a single dataframe
combined_df = pd.concat(cleaned_dfs, ignore_index=True)

# Identify the target column
target_column = 'Attack Success'

# Separate features (X) and target (y)
X = combined_df.drop(columns=[target_column])
y = combined_df[target_column]

# Normalize the data using MinMaxScaler
scaler = MinMaxScaler()
X_normalized = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)

# Use SimpleImputer to handle missing values
imputer = SimpleImputer(strategy='mean')  # You can choose other strategies as well
X_imputed = pd.DataFrame(imputer.fit_transform(X_normalized), columns=X_normalized.columns)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_normalized, y, test_size=0.2, random_state=42)

# Initialize the Random Forest Classifier
classifier = RandomForestClassifier()

# Fit the classifier to the training data
classifier.fit(X_train, y_train)

# Make predictions on the test data
y_pred = classifier.predict(X_test)

#  accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Save the preprocessed data to a CSV file
preprocessed_df = pd.concat([X_normalized, y], axis=1)
preprocessed_df.to_csv('preprocessed_data_classification.csv', index=False)

