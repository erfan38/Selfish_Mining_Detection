import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt


def plot_class_distributions(data_df, label_column='label', dimensions_per_figure=9):
    """
    Compare the distributions of each dimension separately for two classes using subplots.

    Parameters:
        data_df (pandas.DataFrame): DataFrame containing the data and label column.
        label_column (str): Name of the column containing class labels (0 or 1). Default is 'label'.
        dimensions_per_figure (int): Number of dimensions per figure. Default is 9.
    """
    class0_data = data_df[data_df[label_column] == 0].drop(columns=[label_column])
    class1_data = data_df[data_df[label_column] == 1].drop(columns=[label_column])

    dimensions = len(class0_data.columns)
    num_figures = (dimensions + dimensions_per_figure - 1) // dimensions_per_figure

    for figure_idx in range(num_figures):
        start_dim = figure_idx * dimensions_per_figure
        end_dim = min((figure_idx + 1) * dimensions_per_figure, dimensions)

        fig, axes = plt.subplots(3, 3, figsize=(15, 10))
        fig.suptitle(f"Class Distributions Comparison (Dimensions {start_dim + 1}-{end_dim})", fontsize=16)

        for idx, column in enumerate(class0_data.columns[start_dim:end_dim], start=start_dim):
            row = idx // 3 - start_dim // 3
            col = idx % 3

            ax = axes[row, col]
            ax.hist(class0_data[column], bins=30, density=True, alpha=0.5, color='blue', label='Class 0')
            ax.hist(class1_data[column], bins=30, density=True, alpha=0.5, color='orange', label='Class 1')
            ax.set_title(column)
            ax.set_xlabel('Values')
            ax.set_ylabel('Density')
            ax.legend()

        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        plt.savefig(str(figure_idx)+'.png')
        # plt.show()



dataset = pd.read_csv('dataset.csv').drop(columns=['Iteration'])
plot_class_distributions(dataset, label_column='Label')
