import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

df = pd.read_csv("data.csv", encoding="latin1")
features = ['SALES', 'QUANTITYORDERED', 'PRICEEACH', 'MSRP']

data = df[features].copy()
data = data.fillna(data.median()).drop_duplicates()
X = StandardScaler().fit_transform(data)

wcss = [KMeans(n_clusters=k, random_state=42, n_init=10)
        .fit(X).inertia_ for k in range(1, 11)]

plt.plot(range(1, 11), wcss, marker='o')
plt.xlabel("K")
plt.ylabel("WCSS")
plt.title("Elbow Method")
plt.show()

km = KMeans(n_clusters=3, random_state=42, n_init=10)
data['Cluster'] = km.fit_predict(X)

print(data['Cluster'].value_counts().sort_index())
print(data.groupby('Cluster')[features].mean().round(2))
print("Silhouette Score:", round(silhouette_score(X, data['Cluster']), 3))

sns.scatterplot(x=X[:, 0], y=X[:, 2], hue=data['Cluster'], palette='Set1')
plt.xlabel("Standardized Sales")
plt.ylabel("Standardized Price Each")
plt.title("K-Means Clusters")
plt.show()