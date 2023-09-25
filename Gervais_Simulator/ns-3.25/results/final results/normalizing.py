import pandas as pd
from sklearn.preprocessing import StandardScaler

# 1- Load CSV files
benign_1 = pd.read_csv('each_benign.csv')
benign_2 = pd.read_csv('total_benign.csv')
selfish_1 = pd.read_csv('each_selfish.csv')
selfish_2 = pd.read_csv('total_selfish.csv')

# 2- Combine benign and selfish data
benign_data = pd.concat([benign_1, benign_2], ignore_index=True)
selfish_data = pd.concat([selfish_1, selfish_2], ignore_index=True)

# Assuming the last column is the target variable
target_column = benign_data.columns[-1]

# Separate features and target variable
X_benign = benign_data.drop(columns=[target_column])
y_benign = benign_data[target_column]

X_selfish = selfish_data.drop(columns=[target_column])
y_selfish = selfish_data[target_column]

# Data Cleaning: Handle missing values if needed
X_benign.fillna(0, inplace=True)
X_selfish.fillna(0, inplace=True)

# Standardization using StandardScaler
scaler = StandardScaler()

X_benign_standardized = scaler.fit_transform(X_benign)
X_selfish_standardized = scaler.transform(X_selfish)

# Save standardized datasets to CSV files
pd.DataFrame(X_benign_standardized, columns=X_benign.columns).to_csv('benign_standardized.csv', index=False)
pd.DataFrame(X_selfish_standardized, columns=X_selfish.columns).to_csv('selfish_standardized.csv', index=False)

