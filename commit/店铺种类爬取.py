import requests
import re
import json
import time
import pandas as pd


def start():
    for w in range(0, 1600, 32):
        # 页码根据实际情况x32即可，我这里是设置50页为上限，为了避免设置页码过高或者数据过少情况，定义最大上限为1600-也就是50页，使用try-except来检测时候异常，异常跳过该页，一般作为无数据跳过该页处理
        try:
            # 注意uuid后面参数空余将uuid后xxx替换为自己的uuid参数
            url = 'https://apimobile.meituan.com/group/v4/poi/pcsearch/1?uuid=4103ae3807f44af69a0d.1620733635.1.0.0&userid=886801365&limit=32&offset='+str(w)+'&cateId=-1&q=%E7%81%AB%E9%94%85&token=TfhVWSmnV8zpvkgzTnWsd-HrsBAAAAAAhw0AAJ_T5tOAVgGRlSpU_QETf3IjTJ7DMgDs7pDWT4gJ6PAYImAM4PGKPlyIdWDVMKrEMg&areaId=17'
            # headers的数据可以在F12开发者工具下面的requests_headers中查看，需要实现选择如下headers信息
            # 必要情况 请求频繁 建议增加cookie参数在headers内
            headers = {
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Connection': 'keep-alive',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
                'Host': 'apimobile.meituan.com',
                'Origin': 'https://bj.meituan.com',
                'Referer': 'https://bj.meituan.com/',
                'Cookie': 'uuid=4103ae3807f44af69a0d.1620733635.1.0.0; mtcdn=K; lt=TfhVWSmnV8zpvkgzTnWsd-HrsBAAAAAAhw0AAJ_T5tOAVgGRlSpU_QETf3IjTJ7DMgDs7pDWT4gJ6PAYImAM4PGKPlyIdWDVMKrEMg; u=886801365; n=%E5%8D%96%E8%90%8C%E5%B0%8F%E8%A2%8B%E9%BC%A0; token2=TfhVWSmnV8zpvkgzTnWsd-HrsBAAAAAAhw0AAJ_T5tOAVgGRlSpU_QETf3IjTJ7DMgDs7pDWT4gJ6PAYImAM4PGKPlyIdWDVMKrEMg; ci=1; rvct=1; _lxsdk_cuid=1795b410d33c8-0f10b8b8801808-d7e1739-ea600-1795b410d34c8; unc=%E5%8D%96%E8%90%8C%E5%B0%8F%E8%A2%8B%E9%BC%A0; firstTime=1620733692210; _lxsdk_s=1795b410d35-ccf-ad6-34f%7C%7C13'
            }
            response = requests.get(url, headers=headers)
            print(response.text)
            #正则获取当前响应内容中的数据，因json方法无法针对店铺特有的title键值进行获取没所以采用正则
            titles = re.findall('","title":"(.*?)","address":"', response.text)
            addresses = re.findall(',"address":"(.*?)",', response.text)
            avgprices = re.findall(',"avgprice":(.*?),', response.text)
            avgscores = re.findall(',"avgscore":(.*?),', response.text)
            comments = re.findall(',"comments":(.*?),', response.text)
            backCateNames = re.findall(',"backCateName":"(.*?)",', response.text)
            areanames = re.findall(',"areaname":"(.*?)",', response.text)
            # 输出当前返回数据的长度 是否为32
            print(len(titles), len(addresses), len(avgprices), len(avgscores), len(comments), len(backCateNames),len(areanames))
            for o in range(len(titles)):
                # 循环遍历每一个值 写入文件中
                title = titles[o]
                address = addresses[o]
                avgprice = avgprices[o]
                avgscore = avgscores[o]
                backCateName = backCateNames[o]
                comment = comments[o]
                areaname = areanames[o]

                # 写入本地文件
                file_data(title, address, avgprice, avgscore, comment, backCateName, areaname)
            time.sleep(2)
            print(123)
        except:
            print("xixi")
#
#
# # 文件写入方法
def file_data(title, address, avgprice, avgscore, comment, backCateName,areaname):
    data = {
        '店铺名称': title,
        '店铺地址': address,
        '种类': backCateName,
        '平均消费价格': avgprice,
        '店铺评分': avgscore,
        '评价人数': comment,
        '地区':areaname

    }
    with open('../美团美食.txt', 'a', encoding='UTF-8')as fb:
        fb.write(json.dumps(data, ensure_ascii=False) + '\n')

if __name__ == '__main__':
    start()
    # ！！！！将爬取得到的数据从txt格式转换为csv
    list = []
    file = open("../美团美食.txt", 'r', encoding='utf-8')
    js = file.readlines()
    # dic = json.loads(js)
    file.close()
    for line in js:
        dict = json.loads(line)
        list.append(dict)
    pd.DataFrame(list).to_csv('../美团美食.csv', index=0, encoding='UTF-8')
    # print(list[0])