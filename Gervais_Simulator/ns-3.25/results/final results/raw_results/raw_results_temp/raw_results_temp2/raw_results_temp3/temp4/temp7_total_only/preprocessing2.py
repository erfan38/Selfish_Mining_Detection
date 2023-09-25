import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

def plot_2d_tsne(X, y):
    """
    Plot a 2D t-SNE visualization of two classes.
    
    Parameters:
        X (numpy.ndarray): Feature matrix of shape (n_samples, n_features).
        y (numpy.ndarray): Label array of shape (n_samples).
    """
    tsne = TSNE(n_components=2, random_state=42)
    tsne_results = tsne.fit_transform(X)

    plt.figure(figsize=(10, 6))
    plt.scatter(tsne_results[y == 0, 0], tsne_results[y == 0, 1], label='Class 1', alpha=0.7)
    plt.scatter(tsne_results[y == 1, 0], tsne_results[y == 1, 1], label='Class 2', alpha=0.7)
    plt.title('2D t-SNE Plot')
    plt.xlabel('t-SNE Dimension 1')
    plt.ylabel('t-SNE Dimension 2')
    plt.legend()
    plt.show()



dataset = pd.read_csv('dataset.csv')

X = dataset.drop(columns=['Label'])
y = dataset['Label']
print("Separating features (X) and labels (y) was done!")
X = dataset.drop(columns=['Label'])

#missing_values = X.isnull().sum()
#print("Missing values:\n", missing_values)

min_max_scaler = MinMaxScaler()
X_normalized = min_max_scaler.fit_transform(X)
print("Data Normalization was done!")
np.save('X.npy', X_normalized)
np.save('y.npy', y)
#standard_scaler = StandardScaler()
X_standardized = StandardScaler().fit_transform(X_normalized)
print("Data Standardization was done!")




plot_2d_tsne(X_normalized, y)



# Apply a logarithmic transformation to the features
#X_transformed = np.log1p(X_standardized)  # log(1 + x) to handle zero values

# Introduce noise to certain features
noise_level = 0.7  # Adjust the noise level as needed
num_samples, num_features = X_standardized.shape
noise = np.random.normal(0, noise_level, (num_samples, num_features))
X_noisy = X_standardized + noise

X_train, X_test, y_train, y_test = train_test_split(X_noisy, y, test_size=0.2, random_state=42)
print("Splitting the dataset was done!")

#X_train, X_test, y_train, y_test = train_test_split(X_standardized, y, test_size=0.2, random_state=42)
#print("Spliting the dataset was done!")

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

