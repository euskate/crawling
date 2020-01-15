from bs4 import BeautifulSoup
import requests

"""
<div class="tit3">
    <a href="/movie/bi/mi/basic.nhn?code=135874" title="스파이더맨: 홈커밍">스파이더맨: 홈커밍</a>
</div>
"""

url = "http://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cnt&date=20170714"
str = requests.get(url)
# print(str.text)

soup = BeautifulSoup(str.text, 'html.parser')

all_div_tit3 = soup.find_all('div',{"class":'tit3'})

for tmp in all_div_tit3:
    # print(tmp.find("a").text)         # 텍스트 추출
    print(tmp.find("a").attrs['title'])     # 제목 속성 추출
    print(tmp.find("a").attrs['href'])     # 참조 속성 추출    
