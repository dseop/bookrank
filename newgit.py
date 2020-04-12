from pandas import DataFrame as df
import crawling as cr

url = 'http://www.yes24.com/24/Category/BestSeller?CategoryNumber=001&sumgb=06' # yes24 종합베스트셀러 / 20개씩 / 최근 7일 간
par_html = cr.makepar(url) # parsed html

book_date_list = []

t_list = []
sp_list = []

tmp = par_html.find_all('td', 'goodsTxtInfo')[0]
tmp.a.get('href')
link_url = 'yes24.com/Product/Goods/'
move_url = link_url+t_list[0][1]

for tmp in par_html.find_all('td', 'goodsTxtInfo'):
    t_list.append((tmp.a.text, tmp.a.get('href').split('/')[3])) # tuple version

    tmp_url = 'http://www.yes24.com'+tmp.a.get('href')
    

#   # t_list.append(tmp.a.text)
    # #insert book title
    # href_list.append(tmp.a.get('href'))
    # code_list.append(tmp.a.get('href').split('/')[3])
    #    

# a_list = []
# pu_list = []
aupu_list = []
d_list = []

# tmp = par_html.findAll('div','aupu')[0]
# tmp2 = list(tmp.stripped_strings)
# tmp2[len(tmp2)-1][2:] # 0000년 00월만 빼내는 코드

for tmp in par_html.find_all('div', 'aupu'):
    tmp_list = []
    for a_s in tmp.find_all('a'):
        tmp_list.append(a_s.text)
    aupu_list.append(tmp_list) # aupu_list[last] == publisher
    tmp2 = list(tmp.stripped_strings)
    d_list.append(tmp2[len(tmp2)-1][2:])

