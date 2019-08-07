from sklearn.datasets import load_iris
from sklearn import tree

iris = load_iris()

clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target_names[iris.target])

from sklearn.externals import joblib
joblib.dump(clf, "decisiontreeiris.pkl")
