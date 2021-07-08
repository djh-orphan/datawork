import pandas as pd
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg

#注意：！！！！以下代码使用时要将原csv文件中的列名修改为对应的英文格式
df = pd.read_csv("美团美食.csv", encoding='UTF-8')
fea = ["price", "class"]
X = df[fea]
y = df["score"]
dtree = DecisionTreeClassifier(min_samples_leaf=8, max_depth=8, )
dtree = dtree.fit(X, y)
data = tree.export_graphviz(dtree, out_file=None, feature_names=fea)
graph = pydotplus.graph_from_dot_data(data)
graph.write_png('mydecisiontree.png')

img = pltimg.imread('mydecisiontree.png')
imgplot = plt.imshow(img)
plt.show()
