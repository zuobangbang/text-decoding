import requests
import pandas
from bs4 import BeautifulSoup
import time
from pymongo import MongoClient
#解密函数
def change(string):
    changedict = {
        '\uf320': '0', '\uf331': '1', '\ue4f2': '2', '\uf725': '3', '\uf412': '4', '\uf5fd': '5', '\uecf9': '6',
        '\ueadf': '7', '\ue627': '8', '\ue649': '9', '\ueee9': '一', '\ue94c': '师', '\ue51a': '会', '\uf0f1': '四',
        '\ue7c2': '计', '\ue477': '财', '\uf137': '场', '\uead7': '聘', '\ue69a': '招', '\uf1f8': '工', '\ue204': '周',
        '\ueb7a': '端', '\ue4e4': '年', '\uf4ea': '设', '\uf846': '程', '\uf40b': '二', '\uf01f': '五', '\ue848': '天',
        '\uf7b3': '前', '\ue1ea': '网', '\uec3e': '广', '\ue860': '市', '\uf5d9': '月', '\uf333': '个', '\uee09': '告',
        '\ueca5': '作', '\uf0fb': '三', '\uee4b': '互', '\ue823': '生',
        '\ued57': '人', '\ue802': '政', '\ue9b7': '件', '\uebd8': '行', '\uea9c': '软', '\ue9ff': '银', '\uf298': '联',
        '\ue889': 'X', '\uf045': 'D', '\uf16f': 'H', '\uf8ef': 'L', '\uf01e': 'P', '\uf36b': 'T', '\ue31c': 'I',
        '\uec6f': 'C', '\ue787': 'G', '\ue13b': 'K', '\ue3e1': 'O', '\uf6ff': 'S', '\ue782': 'W', '\uec8a': 'B',
        '\ue0f1': 'Q', '\ueb3b': 'U', '\uf424': 'Y',
        '\uf56c': 'F', '\ued91': 'N', '\ue410': 'R', '\uef2d': 'V', '\uf588': 'A', '\ue054': 'E', '\ue6cf': 'M',
        '\uec8c': 'Z', '\uf107': 'J', '\uf7e4': 'I',
        '\uea76': 'd', '\uebdb': 'p', '\ue29a': 'h', '\ue19b': 'x', '\ue0fd': 't', '\uf61a': 'c', '\ue1cd': 'g',
        '\uf575': 'k', '\ue6cc': 'o', '\uefe4': 's', '\uf24b': 'w', '\ue555': 'b', '\uee4d': 'f', '\ue0d1': 'j',
        '\ue98e': 'n', '\ue526': 'r', '\uec00': 'v',
        '\uecfb': 'z', '\ueb59': 'a', '\ue441': 'e', '\ueb1f': 'i', '\uf32c': 'm', '\ue927': 'q', '\uf129': 'u',
        '\uf6a2': 'y'
    }
    for key,value in changedict.items():
        string=string.replace(key,value)
    return string
#抓取实习僧相关信息的函数
def spider(key,pages):
    df=pandas.DataFrame(columns=['职称', '发布时间', '地点', '薪资', '工作天数', '实习时长', '公司', '职位'])
    collection=MongoClient('localhost',27017)
    collection=collection['movie'][key]
    for page in range(1,pages+1):
        url='https://www.shixiseng.com/interns/c-None_?k={0}&p={1}'.format(key,str(page))
        headers={
            'User - Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
       }
        html=requests.get(url,headers=headers).text
        soup=BeautifulSoup(html,'lxml')
        soup=soup.find('ul',class_='position-list')
        infs=soup.find_all('li',class_='font')
        for inf in infs:
            data={}
            data['职称']=change(inf.find('a',class_='name').text)
            data['发布时间']=change(inf.find('span',class_='release-time').text)
            data['地点']=change(inf.find('div',class_='area').text)
            more=inf.find('div',class_='more').find_all('span')
            data['薪资']=change(more[0].text)
            data['工作天数']=change(more[1].text)
            data['实习时长']=change(more[2].text)
            data['公司']=change(inf.find('a',class_='company').text)
            data['职位']=change(inf.find('span',class_='type').text)
            df=df.append(data,ignore_index=True)
            collection.insert_one(data)#将数据存入MongoDB
            #print(data)
        print('完成第%d页抓取'%page)
    #print(df)
    df.to_csv('sxs-' + key + '.csv', index=False, mode='a', header=True, encoding='utf-8',columns=['职称', '发布时间', '地点', '薪资', '工作天数', '实习时长', '公司', '职位'])#将数据存入csv


if __name__=='__main__':
    #key='python'
    #pages=28
    key='java'#关键词
    pages=84#页面数
    spider(key,pages)