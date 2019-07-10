from selenium import webdriver
from math import log, sin
import time

browser = webdriver.Chrome()
link = "http://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element_by_tag_name("button")
time.sleep(1)

x = browser.find_element_by_css_selector('span[id="input_value"]').text
answer = browser.find_element_by_id('answer')

browser.execute_script("return arguments[0].scrollIntoView(true);", answer)

answer.send_keys(str(log(abs(12*sin(int(x))))))

for select in ["[id='robotCheckbox']", "[id='robotsRule']", "button"]:
    browser.find_element_by_css_selector(select).click()
