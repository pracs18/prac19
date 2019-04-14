import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import load_boston
import matplotlib.pyplot as plt

X = load_boston()['data']

print('Refer graph for best K for this dataset')

sum_of_squared_distances = []
for k in range(1, 9):
    km = KMeans(n_clusters=k)
    km.fit(X)
    sum_of_squared_distances.append(km.inertia_)

plt.plot(range(1, 9), sum_of_squared_distances, 'bx-')
plt.xlabel('k')
plt.ylabel('Sum_of_squared_distances')
plt.title('Elbow Method For Optimal K')
plt.show()

k = int(input('Enter the optimal K selected from graph: '))

km = KMeans(n_clusters=k, max_iter=500)
km.fit(X)

plt.scatter(X[:, 0], X[:, 1], c=km.labels_, s=50, cmap='viridis')

centers = km.cluster_centers_
plt.scatter(centers[:, 4], centers[:, 5], c='black', s=200, alpha=0.5)