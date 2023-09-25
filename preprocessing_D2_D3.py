import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import time


from sklearn.metrics import precision_score, recall_score, f1_score



def plot_class_distributions(data, class_labels, dimensions=1, dimensions_per_figure=9):

    class0_data = data[class_labels == 0]
    class1_data = data[class_labels == 1]

    num_figures = (dimensions + dimensions_per_figure - 1) // dimensions_per_figure

    for figure_idx in range(num_figures):
        start_dim = figure_idx * dimensions_per_figure
        end_dim = min((figure_idx + 1) * dimensions_per_figure, dimensions)

        fig, axes = plt.subplots(3, 3, figsize=(15, 10))
        fig.suptitle(f"Class Distributions Comparison (Dimensions {start_dim + 1}-{end_dim})", fontsize=16)

        for dim in range(start_dim, end_dim):
            row = (dim - start_dim) // 3
            col = (dim - start_dim) % 3

            ax = axes[row, col]
            ax.hist(class0_data[:, dim], bins=30, density=True, alpha=0.5, color='blue', label='Class 0')
            ax.hist(class1_data[:, dim], bins=30, density=True, alpha=0.5, color='orange', label='Class 1')
            ax.set_title(f"Dimension {dim + 1}")
            ax.set_xlabel('Values')
            ax.set_ylabel('Density')
            ax.legend()

        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        plt.show()

# dataset = pd.read_csv('shuffle_data1_receiveTime.csv')
dataset = pd.read_csv('reduced_dims_6f.csv')
#X = dataset.drop(columns=['Label'])
y = dataset['Label']
print("Separating features (X) and labels (y) was done!")
X = dataset.drop(columns=['Label'])


min_max_scaler = MinMaxScaler()
X_normalized = min_max_scaler.fit_transform(X)
print("Data Normalization was done!")
np.save('X.npy', X_normalized)
np.save('y.npy', y)
# X_standardized = StandardScaler().fit_transform(X_normalized)
print("Data Standardization was done!")

# num_samples, num_features = X_standardized.shape


X_train, X_test, y_train, y_test = train_test_split(X_normalized, y, test_size=0.2, random_state=42)
print("Spliting the dataset was done!")

param_grid = {
    'n_estimators': [50, 100, 150],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
    #'max_features': [ 'sqrt', 'log2']
}

grid_search = GridSearchCV(RandomForestClassifier(random_state=42),
                        param_grid, cv=5, n_jobs=-1)
grid_search.fit(X_train, y_train)

best_rf_classifier = grid_search.best_estimator_
print("Best hyperparameters:", grid_search.best_params_)

cv_scores = cross_val_score(best_rf_classifier, X_train, y_train, cv=5)
print("Cross-validation scores:", cv_scores)
print("Mean CV accuracy:", cv_scores.mean())

start_time_train = time.time()
y_pred_train= best_rf_classifier.predict(X_train)
end_time_train = time.time()
train_accuracy = accuracy_score(y_train, y_pred_train)
print("Evaluating Misclassifications was done! ")
print("Training Accuracy:", train_accuracy)

start_time_test = time.time()
# Predictions on the test set
y_pred_test = best_rf_classifier.predict(X_test)
end_time_test= time.time()

computation_time_test = end_time_test - start_time_test
print("Test Set Classification Report:")
print(classification_report(y_test, y_pred_test))


precision = precision_score(y_test, y_pred_test)
recall = recall_score(y_test, y_pred_test)
f1 = f1_score(y_test, y_pred_test)
accuracy = accuracy_score(y_test, y_pred_test)

print("Precision:", precision)
print("Recall:", recall)
print("F1-score:", f1)
print("Accuracy:", accuracy)
computation_time_train = end_time_train - start_time_train

# Evaluate on unseen data (validation set)
X_train_new, X_val, y_train_new, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=42)
best_rf_classifier.fit(X_train_new, y_train_new)
y_val_pred = best_rf_classifier.predict(X_val)
val_accuracy = accuracy_score(y_val, y_val_pred)
print("Validation Accuracy:", val_accuracy)
print("Time Complexity (sec):", computation_time_train, computation_time_test)

# Create a table of results
data = [['Accuracy', accuracy],
        ['Precision', precision],
        ['Recall', recall],
        ['F1 Score', f1],
        ['Time Complexity of train', computation_time_train],
        ['Time complexity of test', computation_time_test]]

fig, ax = plt.subplots(figsize=(8, 5))
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=data, colLabels=['Metric', 'Score'], cellLoc='center', loc='center')

# Formatting the table
table.auto_set_font_size(False)
table.set_fontsize(14)
table.scale(1.2, 1.2)

plt.show()

feature_names = dataset.drop(columns=['Label']).columns

print("Feature Names:")
for feature in feature_names:
    print(feature)
