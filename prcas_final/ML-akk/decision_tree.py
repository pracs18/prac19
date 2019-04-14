import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

df = pd.read_csv('buy_data.csv')
df = df.apply(LabelEncoder().fit_transform)

X, y = df.drop('Buys', axis=1), df['Buys']
train_x, test_x, train_y ,test_y = train_test_split(X, y, test_size=0.2, random_state=1)

classifier = DecisionTreeClassifier()
classifier.fit(train_x, train_y)
print(f'Score is: {classifier.score(test_x, test_y)*100:.2f}%')

from sklearn.tree import export_graphviz
export_graphviz(classifier, out_file='tree.dot')
