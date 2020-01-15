# pip install selenium
from selenium import webdriver
from bs4 import BeautifulSoup
options = webdriver.ChromeOptions()

driver = webdriver.Chrome('./chromedriver.exe', chrome_options=options)

driver.get("https://www.interpark.com/member/login.do?_method=initial&GNBLogin=Y&&wid1=wgnb&wid2=wel_login&wid3=login&imfsUserPath=http%3A%2F%2Fwww.interpark.com%2Fmalls%2Findex.html%3FgateTp%3D1&historyGoCnt=-1")

driver.find_element_by_id("userId").send_keys('20191216')
driver.find_element_by_name("userPwd").send_keys('20191216')
# driver.find_element_by_css_selector('#form1 > div:nth-child(4) > input').click()
