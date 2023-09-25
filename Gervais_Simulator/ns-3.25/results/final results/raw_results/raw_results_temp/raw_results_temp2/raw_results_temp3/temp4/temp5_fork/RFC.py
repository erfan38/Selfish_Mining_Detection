import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from matplotlib.table import Table
import time

if __name__ == "__main__":
    start_time = time.time()
    
    # Load the training and test datasets
    train_df = pd.read_csv('training_1_feature.csv')
    test_df = pd.read_csv('test_1_feature.csv')

    # Assuming the last column in the training dataset is the target variable
    X_train = train_df.iloc[:, :-1]
    y_train = train_df.iloc[:, -1]

    X_test = test_df.iloc[:, :-1]
    y_test = test_df.iloc[:, -1]

    # Initializing Random Forest Classifier
    rfc = RandomForestClassifier()

    # Train the model on the training data
    rfc.fit(X_train, y_train)

    # Make predictions on the test data
    predictions = rfc.predict(X_test)
    end_time = time.time()
    computation_time = end_time - start_time
    
    # Calculate evaluation metrics
    accuracy = accuracy_score(y_test, predictions)
    precision = precision_score(y_test, predictions)
    recall = recall_score(y_test, predictions)
    f1 = f1_score(y_test, predictions)

    # Create a table of results
    data = [['Accuracy', accuracy],
            ['Precision', precision],
            ['Recall', recall],
            ['F1 Score', f1],
            ['Time Complexity', computation_time]]

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.axis('tight')
    ax.axis('off')
    table = ax.table(cellText=data, colLabels=['Metric', 'Score'], cellLoc='center', loc='center')

    # Formatting the table
    table.auto_set_font_size(False)
    table.set_fontsize(14)
    table.scale(1.2, 1.2)

    plt.show()
    
    print("Time Complexity (sec):", computation_time)

