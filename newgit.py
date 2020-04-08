import ..

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

