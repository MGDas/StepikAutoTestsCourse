from selenium import webdriver
import math
import time

link = 'http://suninjuly.github.io/math.html'
browser = webdriver.Chrome()
browser.get(link)

x = browser.find_element_by_id('input_value').text
answer = browser.find_element_by_id('answer').send_keys(str(math.log(abs(12*math.sin(int(x))))))

human_checked = browser.find_element_by_id("humanRule").get_attribute("checked")
print("value of human radio: ", human_checked)
assert human_checked == 'true', "Human radio is not selected by default"
time.sleep(2)

browser.find_element_by_id('robotCheckbox').click()

rule = browser.find_element_by_id('robotsRule')
robots_checked = rule.get_attribute("checked")

assert robots_checked == 'false', "Robot Checked is None"

rule.click()
browser.find_element_by_css_selector('button').click()
