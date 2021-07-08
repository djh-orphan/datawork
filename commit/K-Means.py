import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

df = pd.read_csv("../美团美食.csv", encoding='UTF-8')
df_ma = df[["店铺评分", "平均消费价格", "类"]]
X = df_ma.values

print(X)
estimator = KMeans(n_clusters=4)
estimator.fit(X)
label_pred = estimator.labels_

x0 = X[label_pred == 0]
x1 = X[label_pred == 1]
x2 = X[label_pred == 2]
x3 = X[label_pred == 3]

fig = plt.figure(figsize=(12, 8))
ax = plt.gca(projection="3d")
ax.scatter(x0[:, 0], x0[:, 1], x0[:, 2], c="red", marker='o', label='label0')
ax.scatter(x1[:, 0], x1[:, 1], x1[:, 2], c="green", marker='*', label='label1')
ax.scatter(x2[:, 0], x2[:, 1], x2[:, 2], c="blue", marker='+', label='label2')
ax.scatter(x3[:, 0], x3[:, 1], x3[:, 2], c="yellow", marker='.', label='label3')

ax.set_xlabel('score', fontsize=14)
ax.set_ylabel('avg_price', fontsize=14)
ax.set_zlabel('class', fontsize=14)
plt.legend(loc=2)
plt.show()
