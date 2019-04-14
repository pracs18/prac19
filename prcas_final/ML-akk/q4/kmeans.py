import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Creating the points in numpy
X = np.array([
    [1.0, 1.0],
    [1.5, 2.0],
    [3.0, 4.0],
    [5.0, 7.0],
    [3.5, 5.0],
    [4.5, 5.0],
    [3.5, 4.5]
])

kmeans = KMeans(n_clusters=2, init=np.array([[0.1, 0.6], [0.3, 0.2]]), n_init=1)
kmeans.fit(X)

plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, s=50, cmap='viridis')

centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)
plt.show()

print('Refer graph for best K for this dataset')

sum_of_squared_distances = []
for k in range(1, 8):
    km = KMeans(n_clusters=k)
    km.fit(X)
    sum_of_squared_distances.append(km.inertia_)

plt.plot(range(1, 8), sum_of_squared_distances, 'bx-')
plt.xlabel('k')
plt.ylabel('Sum_of_squared_distances')
plt.title('Elbow Method For Optimal K')
plt.show()