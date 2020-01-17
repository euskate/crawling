
# 파일명 : selenium03.py
# 이미지 크로링
from selenium import webdriver
import urllib.request
import time

# 절대 경로 가져오기
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(os.path.join(BASE_DIR, "crawling"))


# options = webdriver.ChromeOptions()

# options.add_argument('headless') #화면 표시 X
# options.add_argument("disable-gpu")   
# options.add_argument("lang=ko_KR")    
# options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # user-agent 

# driver = webdriver.Chrome('./chromedriver.exe', 
#     options=options)

# url = "http://ihongss.com/home/post?id=p_1579160264639"
# driver.get(url)
# time.sleep(2)
# # copy -> selector
# img = driver.find_element_by_css_selector('#image_view_0')
# print(img)

# file = img.get_attribute("src") #찾은 태그 중에서 src의 값
# urllib.request.urlretrieve(file, "./download/a2.png")

# driver.close()  
  