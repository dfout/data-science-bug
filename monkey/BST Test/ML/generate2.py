import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Load the data
df = pd.read_csv('Tree_Species.csv')

# Select relevant columns and handle missing values
features = ['DiameterAtBreastHeight', 'Height', 'Width', 'Species']
df_subset = df[features].dropna()

# Separate features and target variable
X = df_subset[['DiameterAtBreastHeight', 'Height', 'Width']]
species = df_subset['Species']

# Scale the features
x = StandardScaler().fit_transform(X)

# Perform PCA
pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x)
principalDf = pd.DataFrame(data=principalComponents,
                           columns=['principal component 1', 'principal component 2'])

# Combine PCA results with species
finalDf = pd.concat([principalDf, df_subset[['Species']]], axis=1)

# Plot the PCA results
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel('Principal Component 1', fontsize=15)
ax.set_ylabel('Principal Component 2', fontsize=15)
ax.set_title('2 component PCA', fontsize=20)

targets = finalDf['Species'].unique()
colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k', 'orange', 'purple', 'brown']  # Add more colors if needed
for target, color in zip(targets, colors):
    indicesToKeep = finalDf['Species'] == target
    ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1']
               , finalDf.loc[indicesToKeep, 'principal component 2']
               , c=color
               , s=50)
ax.legend(targets)
ax.grid()

# Add vector lines for original dimensions
def draw_vector(v0, v1, ax=None):
    ax = ax or plt.gca()
    arrowprops = dict(arrowstyle='->',
                      linewidth=2,
                      shrinkA=0, shrinkB=0)
    ax.annotate('', v1, v0, arrowprops=arrowprops)

# Plot the vectors for the original features
for length, vector in zip(pca.explained_variance_, pca.components_):
    v = vector * 3 * np.sqrt(length)  # Scale the vectors for visibility
    draw_vector(pca.mean_, pca.mean_ + v)

plt.show()