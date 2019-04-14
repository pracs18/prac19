import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
from sklearn.cluster import KMeans
import csv

###########reading dataset and converting it into set of tuples 
path='/home/parij/Documents/subs.csv'

data=csv.reader(open(path))
li=[]
mi=[]
for line in data:
	li.append(tuple(list(map(float,line[:2]))))
	mi.append(tuple(list(map(float,line[:3]))))
print(li)
############ELBOW METHOD
noofclusters=range(1,5)
kmeans=[KMeans(n_clusters=i) for i in noofclusters]
score=[kmeans[i].fit(mi).score(mi) for i in range(len(noofclusters))]
plt.plot(noofclusters, score)
plt.xlabel('Number of Clusters')
plt.ylabel('Score')
plt.title('Elbow Curve')
plt.show()

print('Based on the visual elbow method, value of k is 2')

############Actual KMeans for boston dataset

m1=li[1]
m2=li[-1]

c1=[]
c2=[]


def distance(p1,p2):
	return sqrt(sum((v1-v2)**2 for v1,v2 in zip(p1,p2)))

def recluster():
	c1.clear()
	c2.clear()
	for point in li:
		d1=distance(point,m1)
		d2=distance(point,m2)
		if d1<=d2:
			c1.append(point)
		else:
			c2.append(point)
def cal_mean(cluster):
	x=0
	y=0
	n=0
	for i in cluster:
		x+=i[0]
		y+=i[1]
		n+=1
	return (x/n,y/n)

clusters_found=False
while not clusters_found:
	recluster()
	prevm1=m1
	prevm2=m2
	m1=cal_mean(c1)
	m2=cal_mean(c2)
	if prevm1==m1 and prevm2==m2:
		clusters_found=True

print('Cluster 1:',c1)
print('Cluster 2:',c2)

#########visualization based on only 1st and 2nd column
cluster1=np.asarray(c1)
cluster2=np.asarray(c2)
plt.scatter(cluster1[:,0],cluster1[:,1])
plt.scatter(cluster2[:,0],cluster2[:,1])
plt.show()
