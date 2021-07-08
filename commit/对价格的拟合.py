import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#使用以下代码画出价格的直方图及对应的拟合曲线
df = pd.read_csv("美团美食.csv", encoding='UTF-8')
dic = dict(df.groupby("price").size().sort_values())
df_ma=df[['price']]
X=df_ma.values


sns.set_palette("hls") #设置所有图的颜色，使用hls色彩空间
sns.distplot(X,color="r",bins=30, hist_kws={ "color": "b","rwidth":0.85 },kde=True)
plt.xlabel("price")
plt.ylabel("count")

plt.show()
