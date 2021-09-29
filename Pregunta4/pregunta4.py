import pandas as pd
import numpy as np
from sklearn import tree,preprocessing
dataset = pd.read_csv("wine.csv")
print(dataset)
X=dataset[list(dataset.columns[1:])]
y=dataset["Class"]
data = preprocessing.KBinsDiscretizer(n_bins=5).fit(X,y)
data2=data.transform(dataset[list(dataset.columns[1:])])
print(data2)
clasificador=tree.DecisionTreeClassifier(criterion='entropy',min_samples_split=10)
clasificacion= clasificador.fit(X, y)
print(clasificacion.predict([[12.85,1.6,2.52,17.8,95,2.48,2.37,.26,1.46,3.93,1.09,3.63,1015]]))