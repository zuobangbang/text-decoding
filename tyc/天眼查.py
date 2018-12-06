import requests
import time
from bs4 import BeautifulSoup

def company_url(names):
    headers={
        'Host': 'www.tianyancha.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    id = []
    for name in names:
        url = 'https://www.tianyancha.com/search?key={0}'.format(name)
        html = requests.get(url, headers=headers).text
        #html = requests.get(url, headers=headers,proxies=proxies).text#加IP的情况
        # print(html)
        soup = BeautifulSoup(html, 'lxml')
        infs = soup.find_all('div', class_='search-item')
        if not infs:
            print('抱歉没有找到%s的相关信息' % name)
            continue
        for inf in infs:
            url = inf.find('div', class_='search-result-single').get('data-id')
            id.append(url)
    return id
def change(content):
    dit={
        '4':'1',
        '6':'2',
        '1':'3',
        '8':'4',
        '9':'6',
        '2':'7',
        '7':'8',
        '3':'9','将':'人'
    }
    w=''
    for i in content:
        try:
            w=w+dit[i]
        except KeyError:
            w=w+i
    return w
def company_infs(ids):
    for id in ids:
        url='https://www.tianyancha.com/company/{0}'.format(id)
        headers={
            #加登陆Cookie，经营范围不需要解密，不加登陆Cookie,经营范围需要解密
            'Cookie': 'TYCID=7fa70730ef1311e8abf1f759478dd116; undefined=7fa70730ef1311e8abf1f759478dd116; ssuid=4630380104; _ga=GA1.2.1014893189.1543830278; RTYCID=954b354804ed476a8d5b6b80237bb010; CT_TYCID=ef71b9b7f1894bcaa05d76385f83738b; _gid=GA1.2.153414381.1544018274; aliyungf_tc=AQAAAF2mOBDAhQUAwL9B31sr7XAya2U2; csrfToken=pO8Nt3V4DQNpvNftXqaktmxW; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1543830278,1544010572,1544010837,1544083415; bannerFlag=true; token=4878fae888774153bdc8cbd79735a494; _utm=bfb21e55bc814728b3bdabcffa8bdfcd; tyc-user-info=%257B%2522myQuestionCount%2522%253A%25220%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522monitorUnreadCount%2522%253A%25223%2522%252C%2522discussCommendCount%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODM2MjA3Mjg3OSIsImlhdCI6MTU0NDA4OTk1MiwiZXhwIjoxNTU5NjQxOTUyfQ.K1TBSD4HZMAa2kIwdtnaKXZMWesuZBWVJVNsVWxL4vWtL_nbip3aULXPZWx1BtDDIIFO6dXboOGqE723ai0LFQ%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522mobile%2522%253A%252218362072879%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODM2MjA3Mjg3OSIsImlhdCI6MTU0NDA4OTk1MiwiZXhwIjoxNTU5NjQxOTUyfQ.K1TBSD4HZMAa2kIwdtnaKXZMWesuZBWVJVNsVWxL4vWtL_nbip3aULXPZWx1BtDDIIFO6dXboOGqE723ai0LFQ; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1544089956; _gat_gtag_UA_123487620_1=1; cloud_token=529471f4607c41bdba6cd7c206739aa4; cloud_utm=2752c5d488fe484d93cf887bbcdb9c25',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
'Host': 'www.tianyancha.com',
'Referer': 'https://www.tianyancha.com/',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
        html=requests.get(url,headers=headers).text
        # html = requests.get(url, headers=headers,proxies=proxies).text#加IP的情况
        soup=BeautifulSoup(html,'lxml')
        data={}
        number=soup.find_all('text',class_='tyc-num lh24')
        #print(number)
        data['name']=soup.find('div',class_='header').find('h1',class_='name').text
        data['法人代表']=soup.find('div',class_='name').find('a',class_='link-click').text
        data['注册资本']=change(number[0].text)
        data['注册时间']=change(number[1].text)
        if soup.find('div',class_='num-opening'):
            data['公司状态']=soup.find('div',class_='num-opening').text
        elif soup.find('div',class_='num-cancel'):
            data['公司状态']=soup.find('div',class_='num-cancel').text
        someinfs=soup.find('table',class_='table -striped-col -border-top-none').find_all('tr')
        #print(someinfs)
        #data['工商注册号']=someinfs[0].find('td',width='30%').text
        #data['组织机构代码']=someinfs[0].find('td',width='20%').text
        #data['统一社会信用代码']=someinfs[1].find_all('td')[1].text
        #data['公司类型']=someinfs[1].find_all('td')[3].text
        #data['纳税人识别号']=someinfs[2].find_all('td')[1].text
        #data['行业']=someinfs[2].find_all('td')[3].text
        #data['营业期限']=someinfs[3].find_all('td')[1].text
        data['核准日期'] = change(someinfs[3].find_all('td')[3].text)
        #data['实缴资本']=someinfs[5].find_all('td')[1].text
        #data['登记机关']=someinfs[5].find_all('td')[3].text
        #data['参保人数']=someinfs[6].find_all('td')[1].text
        #data['英文名称']=someinfs[6].find_all('td')[3].text
        #data['地址']=someinfs[7].find_all('td')[1].text
        data['经营范围'] = change(soup.find('span',class_='js-full-container hidden').text)
        if not data['经营范围']:
            data['经营范围']=change(soup.find('span',class_='js-split-container').text)
        print(data)


if __name__=='__main__':
    names=['宁城县刘东种养殖专业合作社','优酷信息技术（北京）有限公司']
    ids=company_url(names)
    company_infs(ids)



