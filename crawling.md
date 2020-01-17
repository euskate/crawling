# Reference of Crawling
크롤링에 관련된 개인 정리 레퍼런스입니다.

## 라이브러리
### beautifulsoup

[BeatuifulSoup Documentaion](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

beautifulsoup이란?
    
> beautifulsoup은 html의 태그를 다룰 수 있는 라이브러리이다. html에서 필요한 정보들을 쏙쏙 뽑아낼 때 사용한다. 

beautifulsoup 설치
```
> pip install bs4
```
아나콘다 설치여부 확인
```
> conda list beautifulsoup4
```


## HTML 크롤링

exam1.html에서
div 태그 찾기

```py
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
```py
    for tmp in all_divs:
        # print(tmp)
        all_p = tmp.find_all("p")
        # print(all_p)
        for tmp1 in all_p:
            # print(tmp1)
            print(tmp1.text)
```

네이버 영화 제목 가져오기

```py
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
```py
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
```
import csv
import readline
import pymongo

#http://ihongss.com/csv/exam1.csv

conn = pymongo.MongoClient('192.168.99.100', 32766)
db = conn.get_database("db1")
coll = db.get_collection("exam1") 

f = open('./resources/exam1.csv', 'r', encoding="utf-8")
rdr = csv.reader(f)
column = next(rdr) #[컬럼명 읽기]

for line in rdr:
    dict1 = dict()    
    for idx, val in enumerate(line):
        dict1[column[idx]] = val

    # print(dict1)
    coll.insert_one(dict1)
conn.close()
```
## 셀레니움

[Selenium Documentation](https://selenium.dev/documentation/en/getting_started/)

> Selenium은 웹 브라우져를 컨트롤하여 웹 UI 를 Automation 하는 도구 중의 하나이다. 

#### 크롬드라이버 다운로드

https://chromedriver.chromium.org/downloads

- 설치되어있는 크롬의 버전과 같은 버전의 크롬드라이버를 다운 받는다.
    - 버전 확인 방법
    - Chrome > 더보기 > 도움말 > Chrome 정보
- 다운받은 크롬드라이버를 프로젝트 폴더에 넣는다.

#### 라이브러리 설치

`pip install selenium`

  1. login 이후 페이지로 들어가는 법
```py
# pip install selenium
from selenium import webdriver

options = webdriver.ChromeOptions()

options.add_argument('window-size=1920x1080')
# options.add_argument('headless')        # 화면표시 안됨.

driver = webdriver.Chrome('./chromedriver.exe', chrome_options=options)

driver.get("http://ihongss.com/webboard")

driver.find_element_by_name("email").send_keys('20191216')
driver.find_element_by_name("pw").send_keys('20191216')
driver.find_element_by_css_selector('#form1 > div:nth-child(4) > input').click()
# driver.find_element_by_xpath('//*[@id="form1"]/div[3]/input')

```

***.click() < 시험에 나온다. >***

- `webdriver.ChromeOptions().add_argument()` : 
크롬 옵션에 arg를 추가한다.
- `driver = webdriver.Chrome('./chromedriver.exe', chrome_options=options)` : 크롬 드라이버를 설정하여 driver 변수에 담는다.
- `driver.get('url')` : 주소를 driver로 가져온다.
  
- 요소 기준 한가지 가져오기
  - `driver.find_element_by_class_name('class_name')` : 클래스 네임을 기준으로 가져온다.
  - `driver.find_element_by_css_selector`
  - `driver.find_element_by_id`
  - `driver.find_element_by_link_text`
  - `driver.find_element_by_name`
  - `driver.find_element_by_xpath`
  - `driver.find_element_by_partial_link_text`

- 요소 기준 복수로 가져오기
  - `driver.find_elements_....` : 복수로 가져온다.

#### 요소검사

Chrome > 개발자도구(`F12`) > 요소 확인 > 검사(`Ctrl + Shift + I`)



```py
## 파일명 : selenium02.py ###############################
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('headless')

options.add_argument("disable-gpu")   
options.add_argument("lang=ko_KR")    
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # user-agent 

driver = webdriver.Chrome('./chromedriver.exe', 
    chrome_options=options)

driver.get("https://datalab.naver.com/shoppingInsight/sCategory.naver") 
time.sleep(3)
tag = driver.find_element_by_class_name('rank_top1000_list').find_elements_by_tag_name("li")

for tmp in tag:
    print(tmp.text.split("\n"))
```

#### 자바 스크립트 실행하기
```py
driver.execute_script("document.getElementsByName('email')[0].value='20191216'")
driver.execute_script("document.getElementsByName('pw')[0].value='20191216'")
driver.execute_script("document.getElementsByClassName('btn btn-primary')[0].click()")
```


### 스케쥴러

파이썬 라이브러리 설치 : 

`> pip install apscheduler`

```py
# pip install apscheduler

from apscheduler.schedulers.blocking import BlockingScheduler
import time

def exec_interval():     # 일정시간 간격으로 수행
    print("hello world")

def exec_cron():
    str = time.strftime('%c', time.localtime(time.time()))
    print("cron: ",str)

sched = BlockingScheduler()

# # 5초간격으로 함수 호출
# sched.add_job(exec_interval, 'interval', seconds=5)
# sched.start()

# 예약 방식 (매시간 10초, 30초일 경우 구동)
sched.add_job(exec_cron,'cron', minute="*", second="10, 30")
sched.start()
```


## MongoDB to Oracle

### pyMongo에서 데이터 읽기

```py
import pymongo

conn = pymongo.MongoClient('192.168.99.100',32766)
db = conn.get_database("db2")
coll = db.get_collection("p20200115")

# SELECT * FROM p20200115
data1 = coll.find()

# SELECT * FROM p20200115 WHERE ID='a'
data2 = coll.find({'id':'a'})

# SELECT ID, NAME FROM p20200115 WHERE ID='a'
data3 = coll.find({'id':'a'},{'id':1, 'name':1})

# SELECT * FROM p20200115 WHERE age > 10
data4 = coll.find({'age':{"$gt":20}})

# SELECT * FROM p20200115 ORDER BY name ASC
data5 = coll.find().sort('name', 1)     # 1(ASC), -1(DESC)

# SELECT * FROM p20200115 WHERE age>10 AND age<=30
data6 = coll.find({"age":{"$gte":10, "$lte":30}})

# SELECT COUNT(*) FROM TABLE
data7 = coll.find().count()

# SELECT * FROM TABLE WHERE ID='a' OR NAME='b'
data8  = coll.find({'$or':[{"id":'a'},{"name":'b'}]})

#SELECT * FROM p202001015 id=a or name in (b)
data9 = coll.find({'$or':[ {"id":'a'}, {'name':{'$regex':'bb'}} ] }) 
```

### Oracle에서 자동으로 순번이 증가하는 기본키 컬럼 'NO'만들기
--- 시퀀스 생성
```SQL
CREATE SEQUENCE SEQ_TABLE1_NO
START WITH 1
INCREMENT BY 1
NOMAXVALUE
NOCACHE;
COMMIT;
```

--- SEQ_TABLE1_NO = SEQ_TABLE_NO+1
```SQL
INSERT INTO TABLE(NO, ID, NAME, AGE)
VALUES(SEQ_TABLE_NO.nextval, 'a','name',34);
COMMIT;
```

### mongoDB의 데이터를 Oracle로 이동
```py
import pymongo
import cx_Oracle as oci

conn_o = oci.connect('admin/1234@192.168.99.100:32764/xe', encoding="utf-8")
cursor = conn_o.cursor()

conn = pymongo.MongoClient('192.168.99.100',32766)
db = conn.get_database("db2")
coll = db.get_collection("p20200115")

data1 = coll.find({},{'_id':False}) # id값 빼기

for tmp in data1:
    print(tmp)
    sql = """
        INSERT INTO TABLE1(NO, ID, NAME, AGE)
        VALUES(SEQ_TABLE1_NO.nextval, :id, :name, :age)
    """
    cursor.execute(sql, tmp)
    conn_o.commit()

conn_o.close()      # 오라클 연결 끊기
conn.close()        # 몽고DB 연결 끊기
```

### 이미지 크롤링

- 먼저, 다운로드 받을 폴더를 만든다.
- 셀레니움을 활용하여 저장한 변수를
- urllib.request.urlretrieve를 통해 저장한다.

- 새로운 메소드
    - file = img.get_attribute("src") # 찾은 태그 중에서 src의 값
    - urllib.request.urlretrieve(file, "./download/a2.png")

```py
# 파일명 : selenium03.py
from selenium import webdriver
import urllib.request

options = webdriver.ChromeOptions()

options.add_argument('headless')        # 화면으로 표시 안함
options.add_argument("disable-gpu")   
options.add_argument("lang=ko_KR")    
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # user-agent 

driver = webdriver.Chrome('./chromedriver.exe', options=options)

url = "http://ihongss.com/home/post?id=p_1579160264639"
driver.get(url)
# copy -> selector
img = driver.find_element_by_css_selector("#image_view_0")
print(img)

file = img.get_attribute("src") # 찾은 태그 중에서 src의 값

urllib.request.urlretrieve(file, "./download/a2.png")
```

```py
# 절대 경로 가져오기
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(os.path.join(BASE_DIR, "하위 프로젝트 디렉토리"))
```

selenium의
Set of special keys codes.
를 가져 옴
```py
query = driver.find_element_by_xpath('//*[@id="query"]')
query.send_keys('사과')
query.send_keys(Keys.ENTER)
# from selenium.webdriver.common.keys import Keys
```

### 이미지 여러 개 가져오기 (네이버 이미지 검색어)

```py
# 파일명 : selenium04.py

from selenium import webdriver
import urllib.request
import time
from selenium.webdriver.common.keys import Keys

# 절대 경로 가져오기 (여기서는 사용 안함)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(os.path.join(BASE_DIR, "crawling"))

options = webdriver.ChromeOptions()

# options.add_argument('headless') #화면 표시 X
options.add_argument("disable-gpu")   
options.add_argument("lang=ko_KR")    
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # user-agent 

driver = webdriver.Chrome('./chromedriver.exe', options=options)

url = "https://www.naver.com"
driver.get(url)
time.sleep(2)

query = driver.find_element_by_xpath('//*[@id="query"]')
query.send_keys('무화과')
query.send_keys(Keys.ENTER)
# from selenium.webdriver.common.keys import Keys

imgspan = driver.find_element_by_xpath('//*[@id="lnb"]/div/div[1]/ul/li[2]/a/span')
imgspan.click()

link = list()

for i in range(1, 21, 1): 
    try:
        img = driver.find_element_by_xpath('//*[@id="_sau_imageTab"]/div[1]/div[2]/div['+ str(i) + ']/a[1]/img') 
    except:
        img = driver.find_element_by_xpath('//*[@id="_sau_imageTab"]/div[2]/div[2]/div['+ str(i) + ']/a[1]/img')   
    print(img)
    link.append(img.get_attribute("src"))

for idx, tmp in enumerate(link):
    urllib.request.urlretrieve(tmp, './download/n'+str(idx)+'.jpg')
```

#bmKHarofYZ4ziM\:
