
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.manifold import TSNE


def plot_dual_distribution(data1, data2, bins=30, labels=('Data 1', 'Data 2'), title="Dual Distribution Plot"):
    """
    Plot the distributions of two 1-D NumPy arrays in a single figure.

    Parameters:
        data1 (numpy.ndarray): 1-D array containing the first set of data.
        data2 (numpy.ndarray): 1-D array containing the second set of data.
        bins (int): Number of bins in the histograms. Default is 30.
        labels (tuple): Labels for the two data sets. Default is ('Data 1', 'Data 2').
        title (str): Title of the plot. Default is "Dual Distribution Plot".
    """
    plt.hist(data1, bins=bins, density=True, alpha=0.5, color='blue', label=labels[0])
    plt.hist(data2, bins=bins, density=True, alpha=0.5, color='orange', label=labels[1])
    plt.title(title)
    plt.xlabel('Values')
    plt.ylabel('Density')
    plt.legend()
    plt.grid(True)
    plt.show()


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



data_benign = pd.read_csv('total_benign.csv').values
data_selfish = pd.read_csv('total_selfish.csv').values


X = np.concatenate((data_benign, data_selfish), axis=0)

labels_benign = np.zeros(data_benign.shape[0], dtype=int)
labels_selfish = np.ones(data_selfish.shape[0], dtype=int)

y = np.concatenate((labels_benign, labels_selfish), axis=0)
plot_2d_tsne(X, y)


# plot_dual_distribution(data_benign, data_selfish)
