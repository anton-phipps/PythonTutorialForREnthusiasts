# Machine Learning Fundamentals with Scikit-learn

## Overview
Machine Learning (ML) is the process of training algorithms to find patterns in data. In Python, the **Scikit-learn** ecosystem provides a unified API for nearly every common ML task.

## 1. Supervised Learning: Classification
Predicting a discrete category (e.g., Iris species).

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# 1. Load data
iris = load_iris()
X, y = iris.data, iris.target

# 2. Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 3. Choose a model and Train
# In R: randomForest(y ~ ., data = train)
clf = RandomForestClassifier(n_estimators=100)
clf.fit(X_train, y_train)

# 4. Predict and Evaluate
y_pred = clf.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
print(classification_report(y_test, y_pred, target_names=iris.target_names))
```

## 2. Unsupervised Learning: Clustering
Grouping data points without labels (e.g., Customer segmentation).

```python
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Using the same Iris data (X)
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(X)

# Visualize the clusters
plt.scatter(X[:, 0], X[:, 1], c=clusters, cmap='viridis')
plt.title("K-Means Clustering of Iris Data")
plt.show()
```

## 3. Dimensionality Reduction: PCA
Compressing features while keeping the most important information.

```python
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)

print(f"Original shape: {X.shape}")
print(f"Reduced shape: {X_reduced.shape}")
```

## 4. Reinforcement Learning (RL) - The Concept
RL is about an **Agent** taking **Actions** in an **Environment** to maximize a **Reward**.
*   **Key difference:** There is no "truth" label. The agent learns from trial and error.
*   **Common Library:** `Gymnasium` (formerly OpenAI Gym).

---

## 🏆 Challenge Exercise: The Titanic Classifier
1.  Load the `titanic` dataset (from `seaborn.load_dataset('titanic')`).
2.  Preprocess the data: Handle missing values and convert `sex` to a numeric column.
3.  Train a `LogisticRegression` or `RandomForestClassifier` to predict `survived`.
4.  Use a 20% test set and report the **Accuracy** and **Confusion Matrix**.
5.  **Bonus:** Use `GridSearchCV` from `sklearn.model_selection` to find the best hyperparameters for your model.

---
[⬅️ Previous](../06_bayesian/01_pymc_intro.md) | [🏠 Table of Contents](../../README.md) | [Next ➡️](02_pytorch_neural_networks.md)
