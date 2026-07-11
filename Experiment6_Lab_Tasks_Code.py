"""
Experiment 6 — Lab Tasks: Unsupervised Learning (Clustering & PCA)
=====================================================================
Note: Matplotlib is used for the plots in Tasks 1 and 3.
Install it first if needed:  pip install matplotlib
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs, load_iris
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


# ==========================================================
# Task 1: Cluster a blob dataset with K-Means and plot the
#         clusters and centroids.
# ==========================================================
X_blobs, _ = make_blobs(n_samples=180, centers=3, random_state=2)
kmeans = KMeans(n_clusters=3, n_init=10, random_state=2).fit(X_blobs)

plt.figure(figsize=(6, 5))
plt.scatter(X_blobs[:, 0], X_blobs[:, 1], c=kmeans.labels_, cmap="viridis", s=30)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],
            c="red", marker="X", s=200, label="Centroids")
plt.title("Task 1: K-Means Clustering")
plt.legend()
plt.savefig("task1_kmeans_clusters.png")
plt.close()
print("Task 1 done -> saved plot as task1_kmeans_clusters.png")

print("\n" + "="*50 + "\n")


# ==========================================================
# Task 2: Use the elbow method to justify the number of
#         clusters for your data.
# ==========================================================
inertias = []
k_values = range(1, 8)
for k in k_values:
    km = KMeans(n_clusters=k, n_init=10, random_state=2).fit(X_blobs)
    inertias.append(km.inertia_)

plt.figure(figsize=(6, 5))
plt.plot(list(k_values), inertias, marker="o")
plt.xlabel("Number of clusters (k)")
plt.ylabel("Inertia")
plt.title("Task 2: Elbow Method")
plt.savefig("task2_elbow_method.png")
plt.close()

print("Inertia for each k:", [round(i, 1) for i in inertias])
print("Task 2 done -> saved plot as task2_elbow_method.png")
print("The 'elbow' (where the drop flattens) suggests the best k is 3.")

print("\n" + "="*50 + "\n")


# ==========================================================
# Task 3: Reduce a 4-feature dataset to 2 dimensions with
#         PCA and plot it.
# ==========================================================
X_iris, y_iris = load_iris(return_X_y=True)
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X_iris)

plt.figure(figsize=(6, 5))
plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c=y_iris, cmap="viridis", s=30)
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("Task 3: PCA - Iris dataset reduced to 2D")
plt.savefig("task3_pca_reduced.png")
plt.close()

print("Original shape:", X_iris.shape, "-> Reduced shape:", X_reduced.shape)
print("Variance kept:", round(pca.explained_variance_ratio_.sum(), 3))
print("Task 3 done -> saved plot as task3_pca_reduced.png")

print("\n" + "="*50 + "\n")


# ==========================================================
# Task 4: Cluster a real customer dataset and describe what
#         each segment represents.
# ==========================================================
# Example customer data: Annual Income (k$) and Spending Score (1-100)
np.random.seed(3)
customer_data = np.vstack([
    np.random.normal([25, 20], 5, (30, 2)),   # low income, low spending
    np.random.normal([80, 80], 5, (30, 2)),   # high income, high spending
    np.random.normal([25, 80], 5, (30, 2)),   # low income, high spending
])

scaler = StandardScaler()
customer_scaled = scaler.fit_transform(customer_data)

customer_kmeans = KMeans(n_clusters=3, n_init=10, random_state=3).fit(customer_scaled)
customer_data_with_labels = np.column_stack([customer_data, customer_kmeans.labels_])

print("Segment centers (Income, Spending Score) — approx, unscaled view:")
for cluster_id in range(3):
    cluster_points = customer_data[customer_kmeans.labels_ == cluster_id]
    avg_income, avg_spending = cluster_points.mean(axis=0)
    print(f"  Segment {cluster_id}: Avg Income = {avg_income:.1f}k, "
          f"Avg Spending Score = {avg_spending:.1f}")

print("""
Interpretation of segments:
  - A segment with low income & low spending  -> "Budget-conscious customers"
  - A segment with high income & high spending -> "High-value / premium customers"
  - A segment with low income & high spending  -> "Impulsive spenders / potential risk"
(Exact numbers will vary depending on your real dataset.)
""")
