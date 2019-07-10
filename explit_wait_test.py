from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from math import log, sin

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

price = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, 'price'), '10000')
)

browser.find_element_by_id('book').click()

x = browser.find_element_by_id('input_value').text
answer = browser.find_element_by_id('answer').send_keys(str(log(abs(12*sin(int(x))))))

browser.find_element_by_id('solve').click()
