import requests, csv
import time
import json
#创建文件夹并打开
fp = open("../美团评论_全部.csv", 'a', newline='', encoding ='utf-8-sig')
writer = csv.writer(fp) #我要写入
#写入内容
writer.writerow(("用户", "ID", "链接", "评论")) #运行一次

for num in range(0, 160, 32):
    # no = random.randint(0, 7)
    # headers_meituan = {
    #     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36",
    #     "Cookie":"uuid=13054dab8e4e4937b13f.1619519425.1.0.0; mtcdn=K; _lxsdk_cuid=17912e16adfc8-03d441e416591-d7e163f-ea600-17912e16adf88; userTicket=vCLfEaAuUgenkPKwewnYpNKJuWaxnMupCnmpVZvZ; u=886801365; n=%E5%8D%96%E8%90%8C%E5%B0%8F%E8%A2%8B%E9%BC%A0; lt=yU5PuDlvXmK-2yoJk7Y-S-jUdBIAAAAAZg0AAMvz7bPKW1R8RvnpxBQPap_2q1eMaEthsw3hgfVLX3IYJ1TNNOURka175uQB05imLw; mt_c_token=yU5PuDlvXmK-2yoJk7Y-S-jUdBIAAAAAZg0AAMvz7bPKW1R8RvnpxBQPap_2q1eMaEthsw3hgfVLX3IYJ1TNNOURka175uQB05imLw; token=yU5PuDlvXmK-2yoJk7Y-S-jUdBIAAAAAZg0AAMvz7bPKW1R8RvnpxBQPap_2q1eMaEthsw3hgfVLX3IYJ1TNNOURka175uQB05imLw; lsu=; token2=yU5PuDlvXmK-2yoJk7Y-S-jUdBIAAAAAZg0AAMvz7bPKW1R8RvnpxBQPap_2q1eMaEthsw3hgfVLX3IYJ1TNNOURka175uQB05imLw; ci=1; rvct=1; unc=%E5%8D%96%E8%90%8C%E5%B0%8F%E8%A2%8B%E9%BC%A0; _hc.v=99fcce23-43a8-d227-9078-f25e85587770.1619525977; lat=39.904177; lng=116.238844; _lxsdk=17912e16adfc8-03d441e416591-d7e163f-ea600-17912e16adf88; firstTime=1619526653564; _lxsdk_s=179133e7c63-e44-86d-e21%7C%7C203"}
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
        'Host': 'apimobile.meituan.com',
        'Origin': 'https://bj.meituan.com',
        'Referer': 'https://bj.meituan.com/',
         'Cookie':"uuid=13054dab8e4e4937b13f.1619519425.1.0.0; mtcdn=K; _lxsdk_cuid=17912e16adfc8-03d441e416591-d7e163f-ea600-17912e16adf88; userTicket=vCLfEaAuUgenkPKwewnYpNKJuWaxnMupCnmpVZvZ; u=886801365; n=%E5%8D%96%E8%90%8C%E5%B0%8F%E8%A2%8B%E9%BC%A0; lt=yU5PuDlvXmK-2yoJk7Y-S-jUdBIAAAAAZg0AAMvz7bPKW1R8RvnpxBQPap_2q1eMaEthsw3hgfVLX3IYJ1TNNOURka175uQB05imLw; mt_c_token=yU5PuDlvXmK-2yoJk7Y-S-jUdBIAAAAAZg0AAMvz7bPKW1R8RvnpxBQPap_2q1eMaEthsw3hgfVLX3IYJ1TNNOURka175uQB05imLw; token=yU5PuDlvXmK-2yoJk7Y-S-jUdBIAAAAAZg0AAMvz7bPKW1R8RvnpxBQPap_2q1eMaEthsw3hgfVLX3IYJ1TNNOURka175uQB05imLw; lsu=; token2=yU5PuDlvXmK-2yoJk7Y-S-jUdBIAAAAAZg0AAMvz7bPKW1R8RvnpxBQPap_2q1eMaEthsw3hgfVLX3IYJ1TNNOURka175uQB05imLw; ci=1; rvct=1; unc=%E5%8D%96%E8%90%8C%E5%B0%8F%E8%A2%8B%E9%BC%A0; _hc.v=99fcce23-43a8-d227-9078-f25e85587770.1619525977; lat=39.904177; lng=116.238844; _lxsdk=17912e16adfc8-03d441e416591-d7e163f-ea600-17912e16adf88; firstTime=1619526653564; _lxsdk_s=179133e7c63-e44-86d-e21%7C%7C203"

    }
    print ("正在爬取%s条…"%num)
    url="https://apimobile.meituan.com/group/v4/poi/pcsearch/1?uuid=13054dab8e4e4937b13f.1619519425.1.0.0&userid=886801365&limit=32&offset="+str(num)+"&cateId=-1&q=%E7%81%AB%E9%94%85&token=yU5PuDlvXmK-2yoJk7Y-S-jUdBIAAAAAZg0AAMvz7bPKW1R8RvnpxBQPap_2q1eMaEthsw3hgfVLX3IYJ1TNNOURka175uQB05imLw"
    # url = "https://www.meituan.com/meishi/api/poi/getMerchantComment?uuid=615228109dcc44379e1b.1618918489.1.0.0&platform=1&partner=126&originUrl=https%3A%2F%2Fwww.meituan.com%2Fmeishi%2F291262%2F&riskLevel=1&optimusCode=10&id=291262&userId=886801365&offset="+str(num)+"&pageSize=10&sortType=1"
    # ajax_url = "https://www.meituan.com/meishi/api/poi/getMerchantComment?uuid=995201beb6774274a2b1.1618914789.1.0.0&platform=1&partner=126&originUrl=https%3A%2F%2Fwww.meituan.com%2Fmeishi%2F112027864%2F&riskLevel=1&optimusCode=10&id=112027864&userId=886801365&offset=" + str(num) + "&pageSize=10&sortType=1"
    response = requests.get(url = url, headers=headers)
    # print(response.text)
#
    dict1 = json.loads(response.text)
    for item in dict1["data"]["comments"]:
        name = item["userName"]
        user_id = item["userId"]
        user_url = item["userUrl"]
        comment = item["comment"]
        result = (name, user_id, user_url, comment)
        writer.writerow(result)
    time.sleep(5)

fp.close()