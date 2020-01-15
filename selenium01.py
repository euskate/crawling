# pip install selenium
from selenium import webdriver
from bs4 import BeautifulSoup
options = webdriver.ChromeOptions()

options.add_argument('window-size=1920x1080')
# options.add_argument('headless')        # 화면표시 안됨.

driver = webdriver.Chrome('./chromedriver.exe', chrome_options=options)

driver.get("http://ihongss.com/webboard")


driver.find_element_by_name("email").send_keys('20191216')
driver.find_element_by_name("pw").send_keys('20191216')
driver.find_element_by_css_selector('#form1 > div:nth-child(4) > input').click()
# driver.find_element_by_xpath('//*[@id="form1"]/div[3]/input')

driver.get("http://daum.net") # 로그인 이후의 페이지
html = driver.page_source
soup = BeautifulSoup(html, 'html_parser')
