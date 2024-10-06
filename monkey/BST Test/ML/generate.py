import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from adjustText import adjust_text


# Load the dataset
try:
    df = pd.read_csv('Tree_Species.csv', encoding='latin1')
except FileNotFoundError:
    print("Error: 'Tree_Species.csv' not found. Please make sure the file is in the same directory as the script.")
    exit()
except Exception as e:
    print(f"An error occurred while reading the file: {e}")
    exit()


# Select features for PCA
features = ['DiameterAtBreastHeight', 'Height', 'Width']
X = df[features].dropna()  # Drop rows with missing values


# Standardize the features
x = StandardScaler().fit_transform(X)


# Apply PCA with 2 components
pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x)
principalDf = pd.DataFrame(data=principalComponents, columns=['principal component 1', 'principal component 2'])


# Add Species information to the PCA data
finalDf = pd.concat([principalDf, df[['Species']].reset_index(drop=True)], axis=1)


# Plot the PCA results
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel('Principal Component 1', fontsize=15)
ax.set_ylabel('Principal Component 2', fontsize=15)
ax.set_title('2 component PCA', fontsize=20)


# Color-code by Species
targets = finalDf['Species'].unique()
colors = plt.cm.get_cmap('tab10', len(targets))
for target, color in zip(targets, colors.colors):
    indicesToKeep = finalDf['Species'] == target
    ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1'],
               finalDf.loc[indicesToKeep, 'principal component 2'],
               c=[color],
               s=50)


# Add labels and legend
texts = []
for i, txt in enumerate(targets):
    texts.append(plt.text(finalDf.loc[finalDf['Species'] == txt, 'principal component 1'].mean(),
                 finalDf.loc[finalDf['Species'] == txt, 'principal component 2'].mean(),
                 txt,
                 ha='center',
                 va='center',
                 fontsize=8,
                 color=colors(i)))

adjust_text(texts, arrowprops=dict(arrowstyle='->', color='black'))
ax.legend(targets, loc='upper right', title='Species')


# Plot the feature vectors
for i, feature in enumerate(features):
    ax.arrow(0, 0, pca.components_[0, i] * 4, pca.components_[1, i] * 4,
             head_width=0.1, head_length=0.1, fc='k', ec='k')
    ax.text(pca.components_[0, i] * 4.5, pca.components_[1, i] * 4.5,
            feature, color='k', ha='center', va='center')


ax.grid()
plt.show()

