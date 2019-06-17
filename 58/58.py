import requests
from bs4 import BeautifulSoup
import re
import fontTools
import base64
from fontTools.ttLib import TTFont
import xml.etree.ElementTree as et

def get_price(url):
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
    response = requests.request("GET", url, headers=headers)
    content=response.text
    font=re.findall("base64,(.*?)'",content)[0]
    fontdata = base64.b64decode(font)
    file = open('58.woff', 'wb')
    file.write(fontdata)
    file.close()
    onlineFonts = TTFont('58.woff')
    onlineFonts.saveXML('test.xml')
    root=et.parse('test.xml').getroot()
    con=root.find('cmap').find('cmap_format_12').findall('map')
    for i in con:
        num=i.attrib['name']
        code=i.attrib['code'].replace('0x','&#x')+';'
        content=content.replace(code,str(int(num[-2:])-1))
    soup = BeautifulSoup(content, 'lxml')
    newprice = soup.find('div', class_='house-basic-right fr').find('span', class_='price strongbox').text.replace('万','')
    neweve=soup.find('div',class_='house-basic-right fr').find('span',class_='unit strongbox').text.replace('元/平','')
    print('破解后的总价为%s。破解后的均价为%s' % (newprice,neweve))
    return newprice,neweve
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
soup=BeautifulSoup(response.text,'lxml')
for i in soup.find('ul',class_='house-list-wrap').find_all('li'):
    fangurl = i.find('h2', class_='title').find('a').get('href')
    price = i.find('div', class_='price').find('p', class_='sum').text.replace('万', '')
    eve = i.find('div', class_='price').find('p', class_='unit').text.replace('元/㎡', '')
    print('正确的总价为%s。正确的均价为%s'%(price,eve))
    newprice, neweve=get_price(fangurl)





