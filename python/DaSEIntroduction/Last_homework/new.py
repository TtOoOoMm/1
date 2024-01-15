import requests

name = input("请输入您要搜索的内容：")
index = int(input("你想要获取多少页数据？="))
url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword"
data = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko Core/1.70.3883.400 QQBrowser/10.8.4559.400",
    "Cookie": "route-cell=ksa; Hm_lvt_1039f1218e57655b6677f30913227148=1645874220; Hm_lvt_5fd8501a4e4e0eddf0c4596de7bd57ab=1645874220; ASP.NET_SessionId=k01k1uam3yetouyrhrbfry0k; Hm_lpvt_1039f1218e57655b6677f30913227148=1645874226; Hm_lpvt_5fd8501a4e4e0eddf0c4596de7bd57ab=1645874226; SERVERID=b9a24dfa0858e01aa6ecd705cdaafe55|1645874406|1645874293",
    "Referer": "http://www.kfc.com.cn/kfccda/storelist/index.aspx"
}

# 创建一个txt文件，准备将信息写入其中
with open('kfc_stores.txt', 'w', encoding='utf-8') as file:
    for i in range(index):
        data_2 = {
            "cname": "",
            "keyword": name,
            "pageIndex": i,
            "pageSize": 10,
            "pid": ""
        }
        resp = requests.post(url, headers=data, data=data_2)
        dic = resp.json()
        for i in dic['Table1']:
            title = i['storeName']
            address = i['addressDetail']
            file.write(title + ' ' + address + '\n')