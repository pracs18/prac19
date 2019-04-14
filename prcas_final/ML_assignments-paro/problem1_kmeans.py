import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
from sklearn.cluster import KMeans

points=[(0.1,0.6),(0.15,0.71),(0.08,0.9),(0.16,0.85),(0.2,0.3),(0.25,0.5),(0.24,0.1),(0.3,0.2)]
clusters={}

########CENTROIDS FOR THE CLUSTERS
m1=points[1]
m2=points[-1]

#######LIST TO STORE CLUSTERS
c1=[]
c2=[]

def distance(p1,p2):
	return sqrt(sum((v1-v2)**2 for v1,v2 in zip(p1,p2)))

def recluster():
	p=1
	c1.clear()
	c2.clear()
	for point in points:
		d1=distance(point,m1)
		d2=distance(point,m2)
		if d1<=d2:
			c1.append(point)
			clusters[p]=1
		else:
			c2.append(point)
			clusters[p]=2
		p+=1
	
def cal_mean(cluster):
	x=0
	y=0
	n=0
	for point in cluster:
		x+=point[0]
		y+=point[1]
		n+=1
	
	return (x/n,y/n)




cluster_found=False
while not cluster_found:
	recluster()
	prevm1=m1
	prevm2=m2
	m1=cal_mean(c1)
	m2=cal_mean(c2)
	if prevm1==m1 and prevm2==m2:
		cluster_found=True
#print(clusters)
print('Cluster 1:',c1)
print('Cluster 2:',c2)


def elbow_method():
	clustno=range(1,5)
	kmeans=[KMeans(n_clusters=i) for i in clustno]
	score=[kmeans[i].fit(points).score(points) for i in range(len(kmeans))]
	plt.plot(clustno, score)
	plt.xlabel('Number of Clusters')
	plt.ylabel('Score')
	plt.title('Elbow Curve')
	plt.show()

print('*************************************************')
print('Q1) Which cluster does P6 belong to?')
#print(str(points[5]))
print(str(clusters[6]))
print()
print('Q2) What is population of cluster around m2?')
print(str(len(c2)))
print()
print('Q3) What is the updated value of m1 and m2?')
print('Centroid m1:',str(m1))
print('Centroid m2:',str(m2))
print()
print('Q4) What is the best value of K for the given problem?')
elbow_method()
print('As per graph, value of K should be 2')
print('*************************************************')

##############VISUALISATION OF CLUSTERS
cluster1=np.asarray(c1)
cluster2=np.asarray(c2)

plt.scatter(cluster1[:,0],cluster1[:,1])
plt.scatter(cluster2[:,0],cluster2[:,1])
plt.show()
