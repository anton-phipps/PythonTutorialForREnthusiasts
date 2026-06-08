# Block 1
import pandas as pd
import polars as pl
import numpy as np

# Create sample data
np.random.seed(42)
X = np.random.randn(100, 4)
X_df = pd.DataFrame(X, columns=['a', 'b', 'c', 'd'])
X_pl = pl.DataFrame(X, schema=['a', 'b', 'c', 'd'])

# We'll use X as a pandas DataFrame or numpy array depending on the example
X = X_df

# Block 2
from sklearn.cluster import KMeans

# 1. Instantiate the model
kmeans = KMeans(n_clusters=3, random_state=42)

# 2. Fit and Predict (Returns the cluster labels)
clusters = kmeans.fit_predict(X)

# 3. Access cluster centers
centers = kmeans.cluster_centers_

# Block 3
import polars as pl
from sklearn.cluster import KMeans

# 1. Instantiate the model
kmeans = KMeans(n_clusters=3, random_state=42)

# 2. Fit and Predict using numpy array
clusters = kmeans.fit_predict(X_pl.to_numpy())

# 3. Access cluster centers
centers = kmeans.cluster_centers_

# Block 4
from sklearn.cluster import DBSCAN

# eps: maximum distance between two samples for them to be considered neighbors
# min_samples: minimum number of samples in a neighborhood for a point to be a core point
db = DBSCAN(eps=0.5, min_samples=5)
clusters = db.fit_predict(X)

# Block 5
from sklearn.cluster import DBSCAN

# Use numpy conversion for Polars
db = DBSCAN(eps=0.5, min_samples=5)
clusters = db.fit_predict(X_pl.to_numpy())

# Note: Outliers are labeled as -1

# Block 6
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# IMPORTANT: Always scale your data before PCA!
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Reduce to 2 components
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# View explained variance ratio
print(f"Explained Variance: {pca.explained_variance_ratio_}")

# Block 7
import polars as pl
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Scale data (Polars -> Numpy)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_pl.to_numpy())

# Reduce to 2 components
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# View explained variance ratio
print(f"Explained Variance: {pca.explained_variance_ratio_}")

# Block 8
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Block 9
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_pl.to_numpy())

