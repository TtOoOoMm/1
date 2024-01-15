import requests

def canteen():
    # 1、获取url
    url = 'https://www.mcdonalds.com.cn/ajaxs/search_by_keywords'
    
    # 2、ua伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Core/1.94.197.400 QQBrowser/11.6.5265.400'
    }
    
    # 3、定义url携带的参数
    address = input('请输入所在城市:')
    data = {
        'keywords': address,
        'location[info]': 'OK',
        'location[position][lng]': '121.47004',
        'location[position][lat]': '31.23136'
    }
    
    # 4、模拟浏览器发送post请求
    respond = requests.post(url, data, headers)
    
    dic_obj = respond.json()
    fileName = address + '.txt'
    
    # 写入txt文件
    with open(fileName, 'w', encoding='utf-8') as file:
        for item in dic_obj:
            file.write(str(item) + ': ' + str(dic_obj[item]) + '\n')

if __name__ == '__main__':
    while True:
        canteen()
        answer = input('是否继续搜索？y或n' + '\n')
        if answer.lower() != 'y':
            break