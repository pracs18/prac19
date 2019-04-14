import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv('hours.csv')
X, y = df['Hours'].values.reshape(-1, 1), df['Risk Factor']

regressor = LinearRegression().fit(X, y)
print(f'Coefficient of Determination: {regressor.score(X, y)}')

y_pred = regressor.predict(X)

import matplotlib.pyplot as plt
plt.scatter(X, y, color='black')
plt.plot(X, y_pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()
