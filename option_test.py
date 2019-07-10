from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


link = 'http://suninjuly.github.io/selects1.html'
browser = webdriver.Chrome()
browser.get(link)
time.sleep(1)

num1 = browser.find_element_by_id('num1').text
num2 = browser.find_element_by_id('num2').text
sum = int(num1) + int(num2)

select = Select(browser.find_element_by_id("dropdown")).select_by_visible_text(str(sum))
browser.find_element_by_tag_name('button').click()
