from pandas import DataFrame as df
import time
from datetime import datetime as dt
import crawling as cr

url = 'http://www.yes24.com/24/category/bestseller?CategoryNumber=001001025010004&sumgb=06'
url += '&FetchSize=%s&GS=03' %(40) 
# 리스트 00개씩, 품절제외(gs=03)

tmp_par = cr.makepar(url)
#url parsing(crawling, makepar function)

def mak_url_list(url) : # get: 리스트형 url / return: url_list
    url_list = []

    idx = 1
    idx_list = []

    for page in [1] : #page number you want to gather
        tmpurl = url + '&PageNumber=%s' % (page) #insert page info
        tmp_par = cr.makepar(tmpurl) #parsing by page
        for i in tmp_par.find_all('td', 'goodsTxtInfo'):
            # 베스트셀러보기 include 'goodsTxtInfo' (베스트분석)
            # 빠른분야찾기 include 'goods_info' (카테고리분석)
            
            idx_list.append(idx)
            idx += 1

            url_list.append('http://www.yes24.com' + i.find('a', href=True)['href'])
return url_list        

### you can choose the way to insert url_list ###
url_list = mak_url_list(url)
# url_list ="""http://www.yes24.com/Product/Goods/89309569?Acode=101""".split('\n')
###  ###

t_list = []
t2_list = []
a_list = []
pu_list = []
d_list = []
pr_list = []
sp_list = []
info_list = []
page_list = []
weight_list = []
size_list = []
cate_list = []
review_list=[]

def gbi_yes(url_list) : #get best info(yes24)
    for url in url_list :
    #url = url_list[0]
        print('present url\n%s' %url)
        tmp_par = cr.makepar(url)
        
        #도서명
        t_list.append(tmp_par.find('h2', 'gd_name').text) 

        #부제
        if tmp_par.find('h3', 'gd_nameE') is None : 
            t2_list.append('')
        else :
            t2_list.append(tmp_par.find('h3', 'gd_nameE').text)

        #저자
        #a_list.append(tmp_par.find('span', 'gd_auth').find_all('a')[0].text) #공저자 다 포함시킬 수 있는걸로 변경?
        a_list.append(tmp_par.find('span', 'gd_auth').get_text(' ', strip=True)) #.replace(' 저','')

        #출판사
        pu_list.append(tmp_par.find('span', 'gd_pub').text) 

        #출간일
        d_list.append(tmp_par.find('span', 'gd_date').text.replace('년 ','-').replace('월 ','-').replace('일','')) #출간일

        #가격
        pr_list.append(int(tmp_par.find_all('em', 'yes_m')[0].text.replace('원','').replace(',',''))) #tmp_par.find_all('em', 'yes_m') = 정가 할인가 전부 찾을때

        #판매지수
        if tmp_par.find('span','gd_sellNum') is None : sp_list.append(0)
        else : sp_list.append(int(tmp_par.find('span','gd_sellNum').get_text(' ',strip=True).split(' ')[2])) #셀링포인트
        tmp_info = " ".join(tmp_par.find('tbody','b_size').find_all('td')[1].text.split(' | '))

        #도서규격
        a = tmp_info.replace('쪽','').replace('g','').replace('mm','').split(' ')
        page_list.append(a[0])
        print(len(a))
        if len(a) < 3:
            weight_list.append('')
            size_list.append(a[1])
        else :
            weight_list.append(a[1])
            size_list.append(a[2])
        
        #카테고리
        tmp_list = []
        for tmp in tmp_par.find('div','gd_infoSet infoSet_txtCont').find_all('li') :
            cate = tmp.get_text(strip=True).split('>') # 전체 카테
            #de_cate = cate[2]+'>'+cate[3]
            tmp_list.append(cate[-1])
        cate_list.append(", ".join(tmp_list))
        
        #리뷰수
        if tmp_par.find('span','gd_reviewCount').find('em') is None :
            review_list.append('0')
        else :
            review_list.append(int(tmp_par.find('span','gd_reviewCount').find('em').text)) #리뷰수

    raw_data = df({'제목': t_list,
                   '부제' : t2_list,
                   '저자': a_list,
                   '출판사': pu_list,
                   '출간일': d_list,
                   '가격': pr_list,
                   '지수': sp_list,
                   '쪽': page_list,
                   '무게': weight_list,
                   '판형': size_list,
                   '분류': cate_list,
                   '리뷰수': review_list,
                   'URL': url_list})
    return raw_data

# fn = str(dt.today().date()) # file name = today's date
rd = gbi_yes(url_list)
rd.to_csv('getinfo.csv', header=True, index=True, encoding='ms949')
