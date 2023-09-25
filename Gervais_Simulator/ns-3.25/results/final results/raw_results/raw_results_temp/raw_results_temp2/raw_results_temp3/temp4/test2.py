import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt

def plot_class_distributions(data, class_labels, dimensions=1, dimensions_per_figure=9):
    """
    Compare the distributions of each dimension separately for two classes using subplots.

    Parameters:
        data (numpy.ndarray): 2-D array containing the data.
        class_labels (numpy.ndarray): 1-D array containing class labels (0 or 1) corresponding to each sample.
        dimensions (int): Number of dimensions (features). Default is 37.
        dimensions_per_figure (int): Number of dimensions per figure. Default is 9.
    """
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

# Example usage
# Replace data_array and class_labels_array with your own data and class labels
# plot_class_distributions(data_array, class_labels_array, dimensions=37, dimensions_per_figure



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

X = np.load('X.npy')
y = np.load('y.npy')

plot_2d_tsne(X, y)



# d = 0
# plot_dual_distribution(X[:1600, d], X[1600:, d])

plot_class_distributions(X, y)
