#import packages

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Read Dataset
dataset=pd.read_csv("hours.csv")

headers=['numberofhours','riskscore']
dataset.columns=headers
print(dataset.head())
X=dataset.iloc[:,:-1].values
print(X)
y=dataset.iloc[:,1].values
print(y)
#Import Linear Regression and create object of it
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X,y)
print("Accuracy : ", str(regressor.score(X, y) * 100))

#Predict value using regressor object
y_pred=regressor.predict([[10]])
print(y_pred)

#Take user input
hours=int(input('Enter the no of hours:'))

#Calculate value of y
eq=regressor.coef_*hours+regressor.intercept_

print('y = %f*%f+%f' %(regressor.coef_,hours,regressor.intercept_))
print('Equation for best fit line is: y=%f*x+%f' %(regressor.coef_,regressor.intercept_))
print("Risk Score: ", eq[0])

plt.plot(X, y,'o')
plt.plot(X, regressor.predict(X));
plt.show()
