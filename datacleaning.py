import pandas as pd
import jieba as jb
from wordcloud import WordCloud as wc
import string
from zhon.hanzi import punctuation
import matplotlib.pyplot as plt
import re
df = pd.read_csv("美团评论_全部.csv", encoding='gbk')
blackground=plt.imread("ho.jpg")
df = df.dropna(subset=["评论"])
df = df.drop_duplicates(subset=['ID'], keep=False)
df_clear = df.drop(df[df["评论"].apply(len) < 2].index)
df_clear.reset_index(drop=True, inplace=True)
# print(df_clear["评论"])

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
# translator = str.maketrans(string.punctuation, ' '*len(string.punctuation))
# all_content.translate(translator)
# all_content= all_content.translate(translator)
cut_text = " ".join(jb.lcut(all_content))
wordcloud = wc(font_path="C:/Windows/Fonts/simfang.ttf",mask=blackground,
                      background_color='White', height=400, width=800,  scale=20, prefer_horizontal=0.9999).generate(cut_text)
plt.figure(figsize=(10, 10))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
# print(cut_text)
plt.show()