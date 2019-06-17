import requests
from bs4 import BeautifulSoup


def fanti(url):
    headers = {
        'authority': "nj.58.com",
        'cache-control': "max-age=0,no-cache",
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        'referer': "https://nj.58.com/bjhnj/ershoufang/k3/pn2/?utm_source=market&spm=u-2d2yxv86y3v43nkddh1.bdpcpz_bt&PGTID=0d30000c-07e4-6c94-2eb6-8eed6c45ab74&ClickID=1",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "zh-CN,zh;q=0.9",
        'cookie': 'f=n; commontopbar_new_city_info=172%7C%E5%8D%97%E4%BA%AC%7Cnj; userid360_xml=69363F4BD6B100689E6625B0A1608B02; time_create=1563168206263; id58=c5/nn1u7RVIzM+Ppfs9xAg==; 58tj_uuid=107b7ced-b4bd-47ec-9d2f-c165eaebd74d; als=0; xxzl_deviceid=GHTBYDTvqT%2FzNvhXGW9PcZI%2FOd8dxoiafRRPWiCwAy0meweYtEkDuyheOSzEfTH%2B; param8716kop=1; wmda_uuid=d2eb2cd61aac2107ec4f5d3e9c10e778; wmda_new_uuid=1; isSmartSortTipShowed=true; param8616=0; Hm_lvt_a3013634de7e7a5d307653e15a0584cf=1543928107; xxzl_smartid=d47369e304bc2048d00926e257266506; mcity=nj; f=n; commontopbar_new_city_info=172%7C%E5%8D%97%E4%BA%AC%7Cnj; city=nj; 58home=nj; commontopbar_ipcity=nj%7C%E5%8D%97%E4%BA%AC%7C0; new_uv=4; utm_source=market; wmda_session_id_6333604277682=1560576200192-c08d4eb5-86bc-d4a0; wmda_visited_projects=%3B1731916484865%3B3381039819650%3B6333604277682; new_session=0; sessionid=deb90633-b564-4d9a-af9e-25c268c3de20; Hm_lvt_5bcc464efd3454091cf2095d3515ea05=1560576678; Hm_lpvt_5bcc464efd3454091cf2095d3515ea05=1560576678; bProtectShowed=true; Hm_lvt_b2c7b5733f1b8ddcfc238f97b417f4dd=1560576684; Hm_lpvt_b2c7b5733f1b8ddcfc238f97b417f4dd=1560576684; gr_user_id=a1af686f-31c5-40e0-9c41-f0b6029150c2; spm=u-2d2yxv86y3v43nkddh1.bdpcpz_bt; init_refer=; ppStore_fingerprint=824E20DE7E820CA75A070BC5C58748641138F71442060BC7%EF%BC%BF1560580831828; JSESSIONID=A818A948743EC5FDD1EC168AD7932E80; xzfzqtoken=FdHXJWdSTdtaKW66Z%2Bq%2B0iyWH44j8UiM4ju8l1tWhFRT1GANwN6UQKZVUIRGRmcKin35brBb%2F%2FeSODvMgkQULA%3D%3D',
            'Postman-Token': "21e45ec5-95f6-4619-aa2f-fef29f559ecd,d08b636b-1f54-43a2-80f3-ce5eab3df162",
        'Host': "nj.58.com",
        'Connection': "keep-alive"
    }
    response = requests.get(url,headers=headers)
    soup=BeautifulSoup(response.text,'lxml')
    newprice=soup.find('div',class_='house-basic-right fr').find('span',class_='price strongbox').text.replace('万','')
    newarea=soup.find('div',class_='house-basic-right fr').find('span',class_='unit strongbox').text.replace('元/平','')
    return newprice,newarea

url = "https://nj.58.com/bjhnj/ershoufang/k3/pn2/"
querystring = {"utm_source":"market","spm":"u-2d2yxv86y3v43nkddh1.bdpcpz_bt","PGTID":"0d30000c-07e4-6c94-2eb6-8eed6c45ab74","ClickID":"1"}
headers = {
    'authority': "nj.58.com",
    'cache-control': "max-age=0,no-cache",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    'referer': "https://nj.58.com/bjhnj/ershoufang/k3/?utm_source=market&spm=u-2d2yxv86y3v43nkddh1.bdpcpz_bt&PGTID=0d30000c-07e4-6887-0e1f-d4647bae4dd5&ClickID=1",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "zh-CN,zh;q=0.9",
    'cookie':'f=n; commontopbar_new_city_info=172%7C%E5%8D%97%E4%BA%AC%7Cnj; userid360_xml=69363F4BD6B100689E6625B0A1608B02; time_create=1563169183411; id58=c5/nn1u7RVIzM+Ppfs9xAg==; 58tj_uuid=107b7ced-b4bd-47ec-9d2f-c165eaebd74d; als=0; xxzl_deviceid=GHTBYDTvqT%2FzNvhXGW9PcZI%2FOd8dxoiafRRPWiCwAy0meweYtEkDuyheOSzEfTH%2B; param8716kop=1; wmda_uuid=d2eb2cd61aac2107ec4f5d3e9c10e778; wmda_new_uuid=1; isSmartSortTipShowed=true; param8616=0; Hm_lvt_a3013634de7e7a5d307653e15a0584cf=1543928107; xxzl_smartid=d47369e304bc2048d00926e257266506; mcity=nj; f=n; commontopbar_new_city_info=172%7C%E5%8D%97%E4%BA%AC%7Cnj; city=nj; 58home=nj; commontopbar_ipcity=nj%7C%E5%8D%97%E4%BA%AC%7C0; new_uv=4; utm_source=market; wmda_session_id_6333604277682=1560576200192-c08d4eb5-86bc-d4a0; wmda_visited_projects=%3B1731916484865%3B3381039819650%3B6333604277682; new_session=0; sessionid=deb90633-b564-4d9a-af9e-25c268c3de20; Hm_lvt_5bcc464efd3454091cf2095d3515ea05=1560576678; Hm_lpvt_5bcc464efd3454091cf2095d3515ea05=1560576678; bProtectShowed=true; Hm_lvt_b2c7b5733f1b8ddcfc238f97b417f4dd=1560576684; Hm_lpvt_b2c7b5733f1b8ddcfc238f97b417f4dd=1560576684; gr_user_id=a1af686f-31c5-40e0-9c41-f0b6029150c2; spm=u-2d2yxv86y3v43nkddh1.bdpcpz_bt; init_refer=; xzfzqtoken=FdHXJWdSTdtaKW66Z%2Bq%2B0iyWH44j8UiM4ju8l1tWhFRT1GANwN6UQKZVUIRGRmcKin35brBb%2F%2FeSODvMgkQULA%3D%3D; ppStore_fingerprint=824E20DE7E820CA75A070BC5C58748641138F71442060BC7%EF%BC%BF1560582199672; JSESSIONID=1DDE237B9DCBD61ECDC03C29D516EA91',
    'Postman-Token': "6358c570-38ba-454a-bb33-5daa09c7d1b1,287ba303-5c87-4912-8898-f411083935c3",
    'Host': "nj.58.com",
    'Connection': "keep-alive"
    }
response = requests.request("GET", url, headers=headers)
n=['0','1','2','3','4','5','6','7','8','9']
result={}
change={}
soup=BeautifulSoup(response.text,'lxml')
for i in soup.find('ul',class_='house-list-wrap').find_all('li'):
    n = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # 得到列表页的总价与单价
    price=i.find('div',class_='price').find('p',class_='sum').text.replace('万','')
    area=i.find('div',class_='price').find('p',class_='unit').text.replace('元/㎡','')
    # print(price)
    # print(area)
    # 得到详情页经加密过的总价与单价
    fangurl = i.find('h2', class_='title').find('a').get('href')
    newprice, newarea=fanti(fangurl)
    # print(newprice)
    # print(newarea)
    # 这里是将总价与加密的总价；单价与加密的单价生成映射，找出对映关系
    for w in range(len(price)):
        if price[w] in n:
            n.remove(price[w])
            result[newprice[w]]=price[w]
            change[price[w]]=newprice[w]
    for w in range(len(area)):
        if area[w] in n:
            n.remove(area[w])
            result[newarea[w]]=area[w]
            change[area[w]]=newarea[w]
    print(result)

    #print映射结果


import re
#这个是详情页得到正确的总价与单价函数
def get_price():
    url = "https://nj.58.com/ershoufang/38472263840925x.shtml"

    querystring = {"utm_source":"market","spm":"u-2d2yxv86y3v43nkddh1.bdpcpz_bt","from":"1-list-145","iuType":"j_2","PGTID":"0d30000c-00b9-51df-316c-014000e7ed7f","ClickID":"5"}

    headers = {
        'authority': "nj.58.com",
        'cache-control': "max-age=0,no-cache",
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        'referer': "https://nj.58.com/jiangning/ershoufang/?utm_source=market&spm=u-2d2yxv86y3v43nkddh1.bdpcpz_bt&PGTID=0d40000c-07e4-6c81-67cb-f5f5699e43b5&ClickID=1",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "zh-CN,zh;q=0.9",
        'cookie': "f=n; commontopbar_new_city_info=172%7C%E5%8D%97%E4%BA%AC%7Cnj; userid360_xml=69363F4BD6B100689E6625B0A1608B02; time_create=1563168206263; id58=c5/nn1u7RVIzM+Ppfs9xAg==; 58tj_uuid=107b7ced-b4bd-47ec-9d2f-c165eaebd74d; als=0; xxzl_deviceid=GHTBYDTvqT%2FzNvhXGW9PcZI%2FOd8dxoiafRRPWiCwAy0meweYtEkDuyheOSzEfTH%2B; param8716kop=1; wmda_uuid=d2eb2cd61aac2107ec4f5d3e9c10e778; wmda_new_uuid=1; isSmartSortTipShowed=true; param8616=0; Hm_lvt_a3013634de7e7a5d307653e15a0584cf=1543928107; xxzl_smartid=d47369e304bc2048d00926e257266506; mcity=nj; f=n; commontopbar_new_city_info=172%7C%E5%8D%97%E4%BA%AC%7Cnj; city=nj; 58home=nj; commontopbar_ipcity=nj%7C%E5%8D%97%E4%BA%AC%7C0; new_uv=4; utm_source=market; wmda_session_id_6333604277682=1560576200192-c08d4eb5-86bc-d4a0; wmda_visited_projects=%3B1731916484865%3B3381039819650%3B6333604277682; new_session=0; sessionid=deb90633-b564-4d9a-af9e-25c268c3de20; Hm_lvt_5bcc464efd3454091cf2095d3515ea05=1560576678; Hm_lpvt_5bcc464efd3454091cf2095d3515ea05=1560576678; bProtectShowed=true; Hm_lvt_b2c7b5733f1b8ddcfc238f97b417f4dd=1560576684; Hm_lpvt_b2c7b5733f1b8ddcfc238f97b417f4dd=1560576684; gr_user_id=a1af686f-31c5-40e0-9c41-f0b6029150c2; spm=u-2d2yxv86y3v43nkddh1.bdpcpz_bt; init_refer=; xzfzqtoken=zkiP4RhoN3XzO7noPYhTZ6q%2Fd0h%2FUugOemRZNEH7rJ7SY19UTU5qAiXYB1p3%2FEBgin35brBb%2F%2FeSODvMgkQULA%3D%3D; duibiId=; JSESSIONID=23D30B58D6DFAFFA6E7CCA4E91BCEEC2; ppStore_fingerprint=824E20DE7E820CA75A070BC5C58748641138F71442060BC7%EF%BC%BF1560583754442,f=n; commontopbar_new_city_info=172%7C%E5%8D%97%E4%BA%AC%7Cnj; userid360_xml=69363F4BD6B100689E6625B0A1608B02; time_create=1563168206263; id58=c5/nn1u7RVIzM+Ppfs9xAg==; 58tj_uuid=107b7ced-b4bd-47ec-9d2f-c165eaebd74d; als=0; xxzl_deviceid=GHTBYDTvqT%2FzNvhXGW9PcZI%2FOd8dxoiafRRPWiCwAy0meweYtEkDuyheOSzEfTH%2B; param8716kop=1; wmda_uuid=d2eb2cd61aac2107ec4f5d3e9c10e778; wmda_new_uuid=1; isSmartSortTipShowed=true; param8616=0; Hm_lvt_a3013634de7e7a5d307653e15a0584cf=1543928107; xxzl_smartid=d47369e304bc2048d00926e257266506; mcity=nj; f=n; commontopbar_new_city_info=172%7C%E5%8D%97%E4%BA%AC%7Cnj; city=nj; 58home=nj; commontopbar_ipcity=nj%7C%E5%8D%97%E4%BA%AC%7C0; new_uv=4; utm_source=market; wmda_session_id_6333604277682=1560576200192-c08d4eb5-86bc-d4a0; wmda_visited_projects=%3B1731916484865%3B3381039819650%3B6333604277682; new_session=0; sessionid=deb90633-b564-4d9a-af9e-25c268c3de20; Hm_lvt_5bcc464efd3454091cf2095d3515ea05=1560576678; Hm_lpvt_5bcc464efd3454091cf2095d3515ea05=1560576678; bProtectShowed=true; Hm_lvt_b2c7b5733f1b8ddcfc238f97b417f4dd=1560576684; Hm_lpvt_b2c7b5733f1b8ddcfc238f97b417f4dd=1560576684; gr_user_id=a1af686f-31c5-40e0-9c41-f0b6029150c2; spm=u-2d2yxv86y3v43nkddh1.bdpcpz_bt; init_refer=; xzfzqtoken=zkiP4RhoN3XzO7noPYhTZ6q%2Fd0h%2FUugOemRZNEH7rJ7SY19UTU5qAiXYB1p3%2FEBgin35brBb%2F%2FeSODvMgkQULA%3D%3D; duibiId=; JSESSIONID=23D30B58D6DFAFFA6E7CCA4E91BCEEC2; ppStore_fingerprint=824E20DE7E820CA75A070BC5C58748641138F71442060BC7%EF%BC%BF1560583754442; f=n; JSESSIONID=BF1F50CF9C1388CEE6265E144DC8DC33",
        'Postman-Token': "1b97a8eb-5c87-4916-9aaa-bdf8a4c28111,bea6b402-9dd2-4f6e-a679-45cb2b0f8547",
        'Host': "nj.58.com",
        'Connection': "keep-alive"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    soup=BeautifulSoup(response.text,'lxml')
    #提取包含总计与单价信息
    content=soup.find('meta',attrs={'name':'description'}).get('content')
    print(content)
    price=re.findall('售价：(.*?)万元',content)[0]
    eve=re.findall('（(.*?)元/㎡）',content)[0]
    print(price)
    print(eve)
get_price()
