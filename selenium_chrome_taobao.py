from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import  re
from pyquery import PyQuery as pq
browser=webdriver.Chrome()
wait=WebDriverWait(browser, 20)
def search():
    try:
        browser.get('https://taobao.com')

        input=wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR,'#q'))
        )
        submit=wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,'#J_TSearchForm > div.search-button > button'))
        )
        input.send_keys("美食")
        submit.click()
        total=wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.total'))
    )
        print(get_prduct())
        return total.text
    except TimeoutError:
        return search()
def next_page(page):
    try:
        input=wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.form > input'))
        )
        sumbit = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit'))
        )
        input.clear()
        input.send_keys(page)
        sumbit.click()
        wait.until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > ul > li.item.active > span'),str(page))
    )
        print(get_prduct())
    except TimeoutError:
        return next_page(page)
def get_prduct():
    wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#mainsrp-itemlist .items .item'))
    )
    htmltext = browser.page_source
    doc=pq(htmltext)
    items=doc("#mainsrp-itemlist .items .item").items()
    for item in items:
        product ={
            'image':item.find('.pic .img').attr('src'),
            'title':item.find('.pic .img').attr('alt'),
            'deal':item.find('.deal-cnt').text()[:-3],
            'shop':item.find('.shop').text(),
            'location':item.find('.location').text()
        }
        return product
def main():
    total=search()
    print(total)
    total=int(re.compile('(\d+)').search(total).group(1))
    print(total)
    for page in range(2,5):
        next_page(page)

if __name__=="__main__":
    main()
