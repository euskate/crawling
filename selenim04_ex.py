
# # 파일명 : selenium04.py

# from selenium import webdriver
# import urllib.request
# import time

# # 절대 경로 가져오기
# import os

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(os.path.join(BASE_DIR, "crawling"))

# options = webdriver.ChromeOptions()

# options.add_argument('headless') #화면 표시 X
# options.add_argument("disable-gpu")   
# options.add_argument("lang=ko_KR")    
# options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # user-agent 

# driver = webdriver.Chrome('./chromedriver.exe', 
#     options=options)

# url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=image&query=%EB%AC%B4%ED%99%94%EA%B3%BC"
# driver.get(url)
# time.sleep(2)
# # copy -> selector
# img = driver.find_elements_by_css_selector('#_sau_imageTab > div.photowall._photoGridWrapper > div.photo_grid._box > div:nth-child(1) > a.thumb._thumb > img')
# print(img)

# file = img.get_attribute("src") #찾은 태그 중에서 src의 값
# for idx, val in enumerateu(file):
#     urllib.request.urlretrieve(file, f)

# driver.close()  
  



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

query = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
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
