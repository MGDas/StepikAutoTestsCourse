from selenium import webdriver
import time

link = 'http://suninjuly.github.io/registration2.html'
browser = webdriver.Chrome()
browser.get(link)

inp = 'input[required]'

name = browser.find_element_by_css_selector(inp + '.first')
name.send_keys('Petr')

surname = browser.find_element_by_css_selector(inp + '.second')
surname.send_keys('Petrov')

email = browser.find_element_by_css_selector(inp + '.third')
email.send_keys('petrov@mail.com')

button = browser.find_element_by_css_selector("button.btn")
button.click()
time.sleep(1)

welcome_text_elt = browser.find_element_by_tag_name("h1")
welcome_text = welcome_text_elt.text

assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text
