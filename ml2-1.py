import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score
from scipy.cluster.hierarchy import linkage, dendrogram
from google.colab import files

uploaded = files.upload()
df = pd.read_csv(next(iter(uploaded)), encoding="latin1")
features = ['SALES', 'QUANTITYORDERED', 'PRICEEACH', 'MSRP']

data = df[features].copy()
data = data.fillna(data.median()).drop_duplicates()
X = StandardScaler().fit_transform(data)

print("Shape:", X.shape)

Z = linkage(X, method='ward')
plt.figure(figsize=(10, 5))
dendrogram(Z, truncate_mode='lastp', p=20)
plt.title("Hierarchical Clustering Dendrogram")
plt.xlabel("Clusters")
plt.ylabel("Distance")
plt.show()

hc = AgglomerativeClustering(n_clusters=3, linkage='ward')
data['Cluster'] = hc.fit_predict(X)

print(data['Cluster'].value_counts().sort_index())
print(data.groupby('Cluster')[features].mean().round(2))
print("Silhouette Score:", round(silhouette_score(X, data['Cluster']), 3))