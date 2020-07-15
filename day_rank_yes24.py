from pandas import DataFrame as df
import time
from datetime import datetime as dt
from datetime import timedelta as td
import crawling as cr
import get_book_info as gbi

today = dt.today().date() #datetime.date(0000, 0, 00)
mon = today.month
day = today.day

url = "http://www.yes24.com/24/category/bestseller?CategoryNumber=001001007&sumgb=07" #input()
# http://www.yes24.com/24/category/bestseller?CategoryNumber=001001007&sumgb=07
url += "&FetchSize=80"

for i in range(0, 10):
    url = "http://www.yes24.com/24/category/bestseller?CategoryNumber=001001007&sumgb=07" #input()
    # http://www.yes24.com/24/category/bestseller?CategoryNumber=001001007&sumgb=07
    url += "&FetchSize=80" 
    
    sear_date = today-td(i)
    mon = sear_date.month
    day = sear_date.day
    
    url += "&year=2020&month=%d&day=%d" (mon, day)
    
    t_list = []
    t2_list = []

    tmp_par = cr.makepar(url)
    tmp_par.findall('td','goodsTxtInfo')
    t_list.append()






