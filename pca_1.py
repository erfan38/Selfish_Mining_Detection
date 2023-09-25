import numpy as np
from sklearn.decomposition import PCA
import pandas as pd

df=pd.read_csv('shuffle_6f.csv')
X = df.drop(columns=['Label']).to_numpy()
y = df['Label'].to_numpy()
#X = np.load('training_data.npy')
pca = PCA(n_components=1)
X_new = pca.fit(X)
print(np.cumsum(pca.explained_variance_ratio_))
print(pca.singular_values_)
X_new = pca.fit_transform(X)
print(X_new)
df = pd.DataFrame(X_new, columns=['Feature1'])#, 'Feature2'])
df['Label'] = y
df.to_csv('reduced_dims_6f.csv')
