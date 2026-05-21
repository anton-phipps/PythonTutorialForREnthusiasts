# Lesson 10: Unsupervised Learning (Clustering & PCA)

## Overview
Unsupervised Learning involves finding patterns in data without a "target" or "label" (y). In R, you likely used `kmeans()`, `hclust()`, or `prcomp()`. Python's **Scikit-learn** provides these same tools with a consistent interface.

---

## 1. Clustering: Finding Hidden Groups
Clustering aims to group similar observations together.

### K-Means Clustering
The most popular clustering algorithm. It partitions data into *K* clusters where each observation belongs to the cluster with the nearest mean.
*   **R:** `kmeans(df, centers = 3)`

### Python (Pandas)
```python
from sklearn.cluster import KMeans

# 1. Instantiate the model
kmeans = KMeans(n_clusters=3, random_state=42)

# 2. Fit and Predict (Returns the cluster labels)
clusters = kmeans.fit_predict(X)

# 3. Access cluster centers
centers = kmeans.cluster_centers_
```

### Python (Polars)
```python
import polars as pl
from sklearn.cluster import KMeans

# 1. Instantiate the model
kmeans = KMeans(n_clusters=3, random_state=42)

# 2. Fit and Predict using numpy array
clusters = kmeans.fit_predict(X.to_numpy())

# 3. Access cluster centers
centers = kmeans.cluster_centers_
```

### DBSCAN (Density-Based Spatial Clustering)
Unlike K-Means, DBSCAN finds clusters based on density and can identify "outliers" (noise). It doesn't require you to specify the number of clusters in advance.
*   **R:** `dbscan::dbscan(df, eps = 0.5)`

### Python (Pandas)
```python
from sklearn.cluster import DBSCAN

# eps: maximum distance between two samples for them to be considered neighbors
# min_samples: minimum number of samples in a neighborhood for a point to be a core point
db = DBSCAN(eps=0.5, min_samples=5)
clusters = db.fit_predict(X)
```

### Python (Polars)
```python
from sklearn.cluster import DBSCAN

# Use numpy conversion for Polars
db = DBSCAN(eps=0.5, min_samples=5)
clusters = db.fit_predict(X.to_numpy())

# Note: Outliers are labeled as -1
```

---

## 2. Dimensionality Reduction: PCA
Principal Component Analysis (PCA) simplifies data by reducing the number of variables while retaining as much information (variance) as possible.
*   **R:** `prcomp(df, scale. = TRUE)`

### Python (Pandas)
```python
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
```

### Python (Polars)
```python
import polars as pl
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Scale data (Polars -> Numpy)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X.to_numpy())

# Reduce to 2 components
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# View explained variance ratio
print(f"Explained Variance: {pca.explained_variance_ratio_}")
```

---

## 3. Comparison with R
| Algorithm | R Function | Python (Sklearn) |
| --- | --- | --- |
| **K-Means** | `kmeans()` | `KMeans()` |
| **DBSCAN** | `dbscan::dbscan()` | `DBSCAN()` |
| **Hierarchical** | `hclust()` | `AgglomerativeClustering()` |
| **PCA** | `prcomp()` | `PCA()` |
| **TSNE** | `Rtsne::Rtsne()` | `TSNE()` |

---

## 4. Key Concept: Scaling
In R, many functions have a `scale = TRUE` argument. In Python, you must **explicitly** use a transformer like `StandardScaler` or `MinMaxScaler`. Failing to scale data with different units (e.g., age vs. income) will lead to poor clustering and PCA results.

### Python (Pandas)
```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

### Python (Polars)
```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X.to_numpy())
```

---

## 🏆 Challenge Exercise: The Flower Segmenter
1.  **Data:** Load the `iris` dataset (`sns.load_dataset('iris')`).
2.  **Preprocessing:** Remove the `species` column (since this is unsupervised) and scale the numeric features.
3.  **Step 1:** Use **K-Means** to find 3 clusters. 
4.  **Step 2:** Use **PCA** to reduce the 4-dimensional data down to 2 dimensions.
5.  **Step 3:** Create a scatter plot of your 2 PCA components, colored by your K-Means cluster labels.
6.  **Comparison:** How well did the clusters match the actual species? (You can color the plot by actual species to check).

---
[⬅️ Previous](01_supervised_learning.md) | [🏠 Table of Contents](../../README.md) | [Next ➡️](03_pytorch_neural_networks.md)
