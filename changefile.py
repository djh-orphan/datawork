import json
import pandas as pd
import csv

list = []
file = open("美团美食.txt", 'r', encoding='utf-8')
js = file.readlines()
# dic = json.loads(js)
file.close()
for line in js:
    dict = json.loads(line)
    list.append(dict)
pd.DataFrame(list).to_csv('美团美食.csv', index = 0, encoding='UTF-8')
print(list[0])
#
# for i in js:

# def write():
#     a = []
#     dict = dic[0]
#     for headers in sorted(dict.keys()):  # 把字典的键取出来
#         a.append(headers)
#     header = a  # 把列名给提取出来，用列表形式呈现
#     with open('美团美食.csv', 'a', newline='', encoding='utf-8') as f:
#         writer = csv.DictWriter(f, fieldnames=header)  # 提前预览列名，当下面代码写入数据时，会将其一一对应。
#         writer.writeheader()  # 写入列名
#         writer.writerows(dic)  # 写入数据
#     print("数据已经写入成功！！！")
