import numpy as np
from sklearn.decomposition import PCA
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.preprocessing import StandardScaler
import time

# Load and process the original datasets
df_1 = pd.read_csv('training.csv')
df_2 = pd.read_csv('testing.csv')

X_1 = df_1.iloc[:, :-1].to_numpy()  # drop label
y_1 = df_1.iloc[:, -1].to_numpy()   # label

X_2 = df_2.iloc[:, :-1].to_numpy()
y_2 = df_2.iloc[:, -1].to_numpy()

# Apply PCA to reduce dimensionality
pca = PCA(n_components=1)
X_training = pca.fit_transform(X_1)
X_testing = pca.fit_transform(X_2)

print(np.cumsum(pca.explained_variance_ratio_))
print(pca.singular_values_)

# Create DataFrames for the reduced datasets
df_training = pd.DataFrame(X_training, columns=['Feature1'])
df_testing = pd.DataFrame(X_testing, columns=['Feature1'])
df_training['Label'] = y_1
df_testing['Label'] = y_2
df_training.to_csv('reduced_dims_training.csv', index=False)
df_testing.to_csv('reduced_dims_testing.csv', index=False)

# Start processing the reduced datasets
if __name__ == "__main__":
    start_time = time.time()

    train_df = pd.read_csv('reduced_dims_training.csv')
    test_df = pd.read_csv('reduced_dims_testing.csv')

    X_train = train_df[['Feature1']]
    y_train = train_df['Label']

    X_test = test_df[['Feature1']]
    y_test = test_df['Label']

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Create and train the RandomForestClassifier
    rf_classifier = RandomForestClassifier(random_state=42, n_estimators=100, max_depth=10, min_samples_split=2, min_samples_leaf=1)
    rf_classifier.fit(X_train_scaled, y_train)

    # Make predictions using the trained model
    predictions = rf_classifier.predict(X_test_scaled)
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

    print("Time Complexity (sec):", computation_time)

