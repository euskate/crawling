# pip install selenium
from selenium import webdriver
from bs4 import BeautifulSoup
import time
options = webdriver.ChromeOptions()

options.add_argument('window-size=1920x1080')
# options.add_argument('headless')        # 화면표시 안됨.

driver = webdriver.Chrome('./chromedriver.exe', chrome_options=options)

driver.get("http://ihongss.com/webboard")

driver.execute_script("document.getElementsByName('email')[0].value='20191216'")
driver.execute_script("document.getElementsByName('pw')[0].value='20191216'")
driver.execute_script("document.getElementsByClassName('btn btn-primary')[0].click()")
# driver.find_element_by_name("email").send_keys('20191216')
# driver.find_element_by_name("pw").send_keys('20191216')
# driver.find_element_by_css_selector('#form1 > div:nth-child(4) > input').click()
# driver.find_element_by_xpath('//*[@id="form1"]/div[3]/input')

time.sleep(3)
driver.execute_script("alert('hello')")