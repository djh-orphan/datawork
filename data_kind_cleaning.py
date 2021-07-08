import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#from kmeans import Kmeans
# 整理种类表格
df = pd.read_csv("美团美食.csv", encoding='UTF-8')
df = df[~df['店铺评分'].isin([0.0])]
df = df[~df['平均消费价格'].isin([0.0])]
df = df[~df['评价人数'].isin([0.0])]
df = df[df['平均消费价格']<200]
df = df[df['平均消费价格']>30]
df = df[df['店铺评分']>4]
df.loc[(df["种类"] == "重庆火锅"), "种类"] = "川渝火锅"
df.loc[(df["种类"] == "四川火锅"), "种类"] = "川渝火锅"
dictionary = dict(df.groupby("种类").size().sort_values())
n = 1
for key, value in dictionary.items():
    dictionary[key] = n
    n = n + 1
print(dictionary)
df["类"]=df["种类"].map(dictionary)
dic = dict(df.groupby("种类").size().sort_values())
# print(df.groupby("地区").size().sort_values())
dic1 = dict(df.groupby("地区").size().sort_values())
lis = []
lis1 = ["海淀区"]
for key, value in dic.items():
    if value < 10:
        lis.append(str(key))
    if key == "烤串" or key == "火锅" or key == "小火锅" or key == "特色火锅":
        lis.append(str(key))

for key, value in dic1.items():
    if value < 5:
        lis1.append(str(key))
cut=[0,4.5,5]
label=[0,1]
df["好坏"]=pd.cut(df["店铺评分"],cut,labels=label)
df = df[~df['种类'].isin(lis)]
df = df[~df['地区'].isin(lis1)]
df.to_csv("美团美食.csv", index=0, encoding='UTF-8')
dc=dict(df.groupby("种类")["评价人数"].mean().sort_values())
dc1=dict(df.groupby("种类").size().sort_values())
print(dic)
print(dic1)
lis=list(dc.keys())
lis1=list(dc.values())
print(lis)
print(lis1)
print(df.groupby("种类").size().sort_values())
print(df.groupby("地区").size().sort_values())
dic1 = dict(df.groupby("地区")["评价人数"].sum())
dic2 = dict(df.groupby("地区")["评价人数"].mean())
# dic = dict(df.groupby("平均消费价格").size().sort_values())
dic3={}
dic4={}
for key in dic1.keys():
    dic3["北京市海淀区"+key]=dic1[key]/sum(dic1.values())*800




for key in dic2.keys():
    dic4["北京市海淀区" + key] = dic2[key]/sum(dic2.values())*800
print(dic3)
print(dic4)
df2=pd.Series(dic3)
print(df2)
df2.to_csv("地点.csv",)
df3=pd.Series(dic4)
print(df3)
df3.to_csv("地点2.csv",)

df_ma=df[["店铺评分","平均消费价格","类"]]
X=df_ma.values



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
ax.scatter(x0[:, 0], x0[:, 1],x0[:, 2] ,c = "red", marker='o', label='label0')
ax.scatter(x1[:, 0], x1[:, 1],x1[:, 2] ,c = "green", marker='*', label='label1')
ax.scatter(x2[:, 0], x2[:, 1],x2[:, 2],c = "blue", marker='+', label='label2')
ax.scatter(x3[:, 0], x3[:, 1],x3[:, 2],c = "yellow", marker='.', label='label3')


ax.set_xlabel('score', fontsize=14)
ax.set_ylabel('avg_price', fontsize=14)
ax.set_zlabel('class', fontsize=14)
plt.legend(loc=2)
plt.show()
