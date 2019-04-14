import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
from sklearn.cluster import KMeans
import csv

###########reading dataset and converting it into set of tuples 
path='/home/parij/stuff/iris.csv'

data=csv.reader(open(path))
li=[]

for line in data:
	li.append(tuple(list(map(float,line[:4]))))

############ELBOW METHOD
noofclusters=range(1,10)
kmeans=[KMeans(n_clusters=i) for i in noofclusters]
score=[kmeans[i].fit(li).score(li) for i in range(len(noofclusters))]
plt.plot(noofclusters, score)
plt.xlabel('Number of Clusters')
plt.ylabel('Score')
plt.title('Elbow Curve')
plt.show()

print('Based on the visual elbow method, value of k is 3')

############Actual KMeans for iris dataset

df=pd.read_csv(path)
X=df.iloc[:,:4].values
Y=df.iloc[:,4].values
kmeans_obj=KMeans(n_clusters=3)
kmeans_obj.fit(X,Y)

results=kmeans_obj.labels_
print('Clusters formed are:')
print(results)
cluster1=0
cluster2=0
cluster3=0

for i in results:
	if i==0:
		cluster1+=1
	elif i==1:
		cluster2+=1
	else:
		cluster3+=1

print('Length of cluster 1:',cluster1)
print('Length of cluster 2:',cluster2)
print('Length of cluster 3:',cluster3)


print('Center of cluster 1:',kmeans_obj.cluster_centers_[0])
print('Center of cluster 2:',kmeans_obj.cluster_centers_[1])
print('Center of cluster 3:',kmeans_obj.cluster_centers_[2])
