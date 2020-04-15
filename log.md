2020/4/15 Django DB

1. DB 이름을 막 바꾸다가 bookcode.objects.all() 실행 시 에러가 뜸
2. 어떡하지
3. 데이터베이스를 bookcode, bookdata, bookrank 로 나눔

BookCode
1. booktitle
2. yes24_bookcode

BookData
1. BookCode
2. author
3. publisher
4. published_date

BookRank
1. BookCode
2. rank
3. yes24_sellingpoint
==> 일별 데이터
