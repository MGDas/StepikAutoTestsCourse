from selenium import webdriver
from math import log, sin
import time

link = 'http://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome()
browser.get(link)

browser.find_element_by_css_selector('.btn').click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

x = browser.find_element_by_id('input_value').text
answer = browser.find_element_by_id('answer').send_keys(str(log(abs(12*sin(int(x))))))

time.sleep(1)
browser.find_element_by_css_selector('.btn').click()
