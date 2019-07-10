from selenium import webdriver
import math

link = 'http://suninjuly.github.io/get_attribute.html'
browser = webdriver.Chrome()
browser.get(link)

x = browser.find_element_by_css_selector('[valuex]').get_attribute('valuex')
answer = browser.find_element_by_id('answer').send_keys(str(math.log(abs(12*math.sin(int(x))))))

for select in ["[id='robotCheckbox']", "[id='robotsRule']", "button"]:
    browser.find_element_by_css_selector(select).click()
