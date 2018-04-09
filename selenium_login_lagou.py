from selenium import webdriver
from requests import Session
from time import sleep
from random import randint
req = Session()
req.headers.clear()

driver = webdriver.PhantomJS()
url = "https://passport.lagou.com/login/login.html?service=https://www.lagou.com/"
driver.get(url)
driver.find_element_by_xpath('/html/body/section/div[1]/div[2]/form/div[1]/input').send_keys("18560382295")
sleep(10)
driver.find_element_by_xpath('/html/body/section/div[1]/div[2]/form/div[2]/input').send_keys("SeekH0pe")

sleep(10)
driver.find_element_by_xpath('/html/body/section/div[1]/div[2]/form/div[5]/input').click()
sleep(10)
cookies = driver.get_cookies()
for cookie in cookies:
    req.cookies.set(cookie['name'],cookie['value'])

html=req.get("https://www.lagou.com/gongsi")
print(html.headers)
