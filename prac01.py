from bs4 import BeautifulSoup
import requests

url = "https://tour.busan.go.kr/nurib/index.busan?menuCd=DOM_000000902000000000"
str = requests.get(url)
soup = BeautifulSoup(str.text, 'html.parser')

# all_span_col = soup.find_all('span',{"class":'txt'})
a = soup.find_all('meta')
print(a)
for tmp in a:
    try:
        print(tmp.attrs['property'])
    except Exception as e:
        print('None')

# for tmp in all_span_col:
#     # print(tmp.find("strong").text)