#import packages

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Read Dataset
dataset=pd.read_csv("/home/parij/Downloads/boston-housing/train.csv")

X=dataset.iloc[:,1:-1].values
#print(X)
y=dataset.iloc[:,14].values
#print(y)

#Import Linear Regression and create object of it
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X,y)
print("Accuracy : ", str(regressor.score(X, y) * 100))

#Predict value using regressor object(values are taken at random... STUDY THE DATASET then fix the values
y_pred=regressor.predict([[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.11,0.13,0.12,0.14]])
print(y_pred)

#Take user input
crim=float(input('Per capita crime rate:'))
zn=float(input('Proportion of residential land zone:'))
indus=float(input('Proportion of non-retail:'))
chas=float(input('Charles River dummy variable:'))
nox=float(input('nitrogen oxide concentration:'))
rm=float(input('average number of rooms per dwelling:'))
age=float(input('proportion of owner-occupied:'))
dis=float(input('weighted mean of distances:'))
rad=float(input('index of accessibility to radial highways:'))
tax=float(input('full-value property tax-rate:'))
ptratio=float(input('pupil-teacher ratio by town:'))
black=float(input('proportion of blacks by town:'))
lstat=float(input('lower status of population:'))
#print(regressor.coef_[0])
#Calculate value of y
eq=lstat*regressor.coef_[12]+black*regressor.coef_[11]+ptratio*regressor.coef_[10]+tax*regressor.coef_[9]+rad*regressor.coef_[8]+dis*regressor.coef_[7]+age*regressor.coef_[6]+rm*regressor.coef_[5]+nox*regressor.coef_[4]+chas*regressor.coef_[3]+indus*regressor.coef_[2]+zn*regressor.coef_[1]+crim*regressor.coef_[0]+regressor.intercept_

#print('y = %f*%f+%f' %(regressor.coef_,hours,regressor.intercept_))
print('Equation for best fit line is: y=%f*x12+%fx11+%fx10+%fx9+%fx8+%fx7+%fx6+%fx5+%fx4+%fx3+%fx2+%fx1+%fx0+%f' %(regressor.coef_[12],regressor.coef_[11],regressor.coef_[10],regressor.coef_[9],regressor.coef_[8],regressor.coef_[7],regressor.coef_[6],regressor.coef_[5],regressor.coef_[4],regressor.coef_[3],regressor.coef_[2],regressor.coef_[1],regressor.coef_[0],regressor.intercept_))
print("Risk Score: ", eq)

#############plotting not done right 
plt.plot(X, y,'o')
plt.plot(X, regressor.predict(X));
plt.show()
