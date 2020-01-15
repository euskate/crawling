# Reference of Crawling
크롤링에 관련된 개인 정리 레퍼런스입니다.

## 라이브러리
### beautifulsoup

beautifulsoup이란?
    
> beautifulsoup은 html의 태그를 다룰 수 있는 라이브러리이다. html에서 필요한 정보들을 쏙쏙 뽑아낼 때 사용한다. 

beautifulsoup 설치
```
$ pip install bs4
```
아나콘다 설치여부 확인
```
conda list beautifulsoup4
```


## HTML 크롤링

exam1.html에서
div 태그 찾기

```
from bs4 import BeautifulSoup


with open('./resources/exam1.html') as fp:
    soup = BeautifulSoup(fp, 'html.parser')

    # div tag 전체 찾기
    all_divs = soup.find_all("div")
    print(all_divs)

    # div tag 첫번쨰 찾기
    first_divs = soup.find("div")
    print(first_divs)
```

div 태그 안의 p 태그 찾기
```
    for tmp in all_divs:
        # print(tmp)
        all_p = tmp.find_all("p")
        # print(all_p)
        for tmp1 in all_p:
            # print(tmp1)
            print(tmp1.text)
```

네이버 영화 제목 가져오기

```
from bs4 import BeautifulSoup
import requests

"""
<div class="tit3">
    <a href="/movie/bi/mi/basic.nhn?code=135874" title="스파이더맨: 홈커밍">스파이더맨: 홈커밍</a>
</div>
"""

url = "http://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cnt&date=20170714"
str = requests.get(url)
print(str.text)

soup = BeautifulSoup(str.text, 'html.parser')

all_div_tit3 = soup.find_all('div',{"class":'tit3'})

for tmp in all_div_tit3:
    print(tmp.find("a").text)            # 텍스트 추출
    print(tmp.find("a").attrs['title'])     # 제목 속성 추출
    print(tmp.find("a").attrs['href'])     # 참조 속성 추출    
```


## XML 크롤링

- xml 추출 : 파일에서
```
from xml.etree.ElementTree import parse

doc = parse('./resources/exam1.xml')

a = doc.findall("student")

for tmp in a:
    print(tmp.findtext("name"))
    print(tmp.findtext("age"))
    print(tmp.find("addr").attrib)
```

- xml 추출 : url에서
```
from xml.etree.ElementTree import parse
from urllib.request import urlopen

url = 'http://ihongss.com/xml/exam1.xml'
str1 = urlopen(url)
doc1 = parse(str1)

for item in doc1.iterfind('items/item'):
    print(item.attrib)              # <item id="a">
    print(item.findtext("name"))    # <name>a</name>

```

## CSV 크롤링
```
import csv

f = open('./resources/exam1.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
next(rdr, None)     # 컬럼 skip

for line in rdr:
    # print(type(line))
    print(line)
```

## 셀레니움

pip install selenium