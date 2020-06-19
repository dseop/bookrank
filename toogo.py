from bs4 import BeautifulSoup as bs
from pandas import DataFrame as df
import crawling as cr

o = open('class_toogo/html.txt')
tbody_html = o.readlines

# url = 'https://gbadmin.gilbut.co.kr/customer/author_recruit?search_date=&gr_strdate=&gr_enddate=&search_cate1=004000&search_cate2=004001&search_state=&search_F=GR_NAME&search_S='
# tmp_par = cr.makepar(url)

par_url = bs(tbody_html, 'html.parser')

tr_list = par_url.find_all('tr')
td_list = []
for i in tr_list :
    td_list.append(i.get_text('/', strip=True).split('/'))

result_1 = []
result_2 = []
result_3 = []
for k in td_list :
    result_1.append(k[5])
    result_2.append(k[4])
    result_3.append(k[2][:3])

df({
    'date': result_1,
    'title': result_2,
    'name': result_3,
}).to_csv('getinfo.csv', header=True, index=True, encoding='ms949')