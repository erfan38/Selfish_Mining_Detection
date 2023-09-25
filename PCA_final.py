import numpy as np
from sklearn.decomposition import PCA
import pandas as pd

df_1 = pd.read_csv('training.csv')
df_2 = pd.read_csv('testing.csv')

X_1 = df_1.iloc[:, :-1].to_numpy()  # drop label
y_1 = df_1.iloc[:, -1].to_numpy()   #label

X_2 = df_1.iloc[:, :-1].to_numpy()
y_2 = df_1.iloc[:, -1].to_numpy()  

pca = PCA(n_components=1)
X_training = pca.fit_transform(X_1)
X_testing = pca.fit_transform(X_2)

print(np.cumsum(pca.explained_variance_ratio_))
print(pca.singular_values_)

df_training = pd.DataFrame(X_training, columns=['Feature1'])
df_testing = pd.DataFrame(X_testing, columns=['Feature1'])
df_training['Label'] = y_1
df_testing['Label'] = y_2
df_training.to_csv('reduced_dims_training.csv', index=False)  # Use index=False to avoid saving the row indices
df_testing.to_csv('reduced_dims_testing.csv', index=False) 

