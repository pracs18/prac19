import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Creating the points in numpy
X = np.array([
    [0.1, 0.6],
    [0.15, 0.71],
    [0.08, 0.9],
    [0.16, 0.85],
    [0.2, 0.3],
    [0.25, 0.5],
    [0.24, 0.1],
    [0.3, 0.2]
])

kmeans = KMeans(n_clusters=2, init=np.array([[0.1, 0.6], [0.3, 0.2]]), n_init=1)
kmeans.fit(X)

print('P6 belongs to cluster number ' + str(kmeans.labels_[5]))
labels = list(kmeans.labels_)
print('M2 has ' + str(labels.count(1)) + ' points in its cluster')
print('M1 is (' + str(kmeans.cluster_centers_[0][0]) + ', ' + str(kmeans.cluster_centers_[0][1]) + ')')
print('M2 is (' + str(kmeans.cluster_centers_[1][0]) + ', ' + str(kmeans.cluster_centers_[1][1]) + ')')
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