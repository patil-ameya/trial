import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset=pd.read_csv('data.csv')
x=dataset.iloc[:,:-1]
y=dataset.iloc[:,5]

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()

x=x.apply(le.fit_transform)
print(x)

from sklearn.tree import DecisionTreeClassifier

regressor=DecisionTreeClassifier(criterion='entropy')
regressor.fit(x.iloc[:, 1:5],y)

x_in=np.array([1,1,0,0])
y_pred=regressor.predict([x_in])

print('prediction=',y_pred)

from six import StringIO
from sklearn.tree import export_graphviz
import pydotplus
from IPython.display import Image

dot_data=StringIO()

export_graphviz(regressor,out_file=dot_data,filled=True,rounded=True,special_characters=True)
graph=pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('tree.png')
