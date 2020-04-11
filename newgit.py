import bookrank.crawling as cr

url = 'http://www.yes24.com/24/Category/BestSeller?CategoryNumber=001&sumgb=06' # yes24 종합베스트셀러 / 20개씩 / 최근 7일 간
par_html = cr.makepar(url) # parsed html

book = [] # book name or code < yes24 경우 도서별 code 얻을 수 있음
def bookrank(par_html) :
    par_html.find('tbody')


print('hello')

##일단 기본적인 것들을 코딩해보자

a=1
b=2

print(a+b)

html = "www.yes24.co.kr"
print(html)

url = "http://www.yes24.com/24/category/bestseller?CategoryNumber=001001025&sumgb=07&FetchSize=80" 
# ex) &year=2020&month=4&day=8 이것도 추가 가능
pagenumber = "&PageNumber=%d" %1

url_2 = url + pagenumber
print(url_2)



