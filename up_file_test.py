from selenium import webdriver
import os
import time


link = 'http://suninjuly.github.io/file_input.html'
browser = webdriver.Chrome()
browser.get(link)

len_input = browser.find_elements_by_tag_name('input[placeholder]')
for inp in len_input:
    inp.send_keys('placeholder')

current = os.path.abspath(os.path.dirname(__file__))
file = os.path.join(current, 'file.txt')

try:
    browser.find_element_by_id('file').send_keys(file)
    print('Sended')
except:
    print('Not')

browser.find_element_by_tag_name('button').click()
