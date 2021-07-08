import pandas as pd


#以下代码全部都属于数据清洗过程
df = pd.read_csv("../美团美食.csv", encoding='UTF-8')
df = df[~df['店铺评分'].isin([0.0])]
df = df[~df['平均消费价格'].isin([0.0])]
df = df[~df['评价人数'].isin([0.0])]
df = df[df['平均消费价格'] < 200]
df = df[df['平均消费价格'] > 30]
df = df[df['店铺评分'] > 4]
df.loc[(df["种类"] == "重庆火锅"), "种类"] = "川渝火锅"
df.loc[(df["种类"] == "四川火锅"), "种类"] = "川渝火锅"

#挑选出种类标签不是火锅或者种类特征不明显的样本删除
dic = dict(df.groupby("种类").size().sort_values())
lis=[]
for key, value in dic.items():
    if value < 10:
        lis.append(str(key))
    if key == "烤串" or key == "火锅" or key == "小火锅" or key == "特色火锅":
        lis.append(str(key))
df = df[~df['种类'].isin(lis)]

#对种类编号
n = 1
for key, value in dic.items():
    dic[key] = n
    n = n + 1
# print(dic)
df["类"] = df["种类"].map(dic)

#对不符合要求的地区进行删除
dic1 = dict(df.groupby("地区").size().sort_values())
# print(dic1)
lis1 = ["海淀区"]
for key, value in dic1.items():
    if value < 5:
        lis1.append(str(key))
df = df[~df['地区'].isin(lis1)]

