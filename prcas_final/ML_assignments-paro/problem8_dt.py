
#import packages
import numpy as np
import pandas as pd

#reading Dataset
dataset=pd.read_csv("dt.csv")
X=dataset.iloc[:,:-1]
print(X)
y=dataset.iloc[:,5].values
print(y)

#Perform Label encoding
from sklearn.preprocessing import LabelEncoder
labelencoder_X = LabelEncoder()

X = X.apply(LabelEncoder().fit_transform)
print(X)

from sklearn.tree import DecisionTreeClassifier
regressor=DecisionTreeClassifier()
regressor.fit(X.iloc[:,1:5],y)

#Predict value for the given expression
X_in=np.array([1,1,0,0])

y_pred=regressor.predict([X_in])
print("Prediction:", y_pred)
S=['<21','Low','Female','Married']
print(LabelEncoder().fit_transform(S).reshape(1,-1))
y_test=regressor.predict(LabelEncoder().fit_transform(S).reshape(1,-1))
print("Predicted:",y_test)
from sklearn.externals.six import StringIO  
from IPython.display import Image  
from sklearn.tree import export_graphviz
import pydotplus

dot_data = StringIO()

export_graphviz(regressor, out_file=dot_data, filled=True, rounded=True, special_characters=True)

graph = pydotplus.graph_from_dot_data(dot_data.getvalue()) 
graph.write_png('tree.png')
