import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

#以下代码全部都属于数据清洗过程
df = pd.read_csv("美团美食.csv", encoding='UTF-8')
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


#以下为评论清洗以及词云图构建
import jieba as jb
from zhon.hanzi import punctuation
from wordcloud import WordCloud as wc
import string
import re
df = pd.read_csv("美团评论_全部.csv", encoding='gbk')
df = df.dropna(subset=["评论"])
df = df.drop_duplicates(subset=['ID'], keep=False)
df_clear = df.drop(df[df["评论"].apply(len) < 2].index)
df_clear.reset_index(drop=True, inplace=True)
all_content = ''
translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
translator_zhon = str.maketrans(punctuation, ' ' * len(punctuation))
for i in range(1, len(df_clear["评论"])):
    df_clear["评论"][i] = df_clear["评论"][i].translate(translator)
    df_clear["评论"][i] = df_clear["评论"][i].translate(translator_zhon)
    df_clear["评论"][i] = re.sub( '[员可以但太人各种了的很好吃不错是非常也还都就有超级特别我和最喜来整体感觉真下次给赞去尤其]' , '', df_clear["评论"][i])

    # print(df_clear["评论"][i])
    all_content = all_content + df_clear["评论"][i]
all_content = str(all_content)

cut_text = " ".join(jb.lcut(all_content))
blackground=plt.imread("ho.jpg")
wordcloud = wc(font_path="C:/Windows/Fonts/simfang.ttf",mask=blackground,
                      background_color='White', height=400, width=800,  scale=20, prefer_horizontal=0.9999).generate(cut_text)
plt.figure(figsize=(10, 10))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
# print(cut_text)
plt.show()