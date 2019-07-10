from selenium import webdriver
from datetime import datetime
import time

browser = webdriver.Chrome()
browser.set_window_size(1400, 1200)
print('Open brawser')
browser.get("https://test2.studiovector.art")
print('Open link')
time.sleep(1)

a = browser.find_element_by_css_selector("nav ul li:nth-child(1) a")
a.click()
time.sleep(1)
print('Go To Catalog')

for i in range(1, 11):

    add_to_cart = browser.find_element_by_css_selector(
        "section:nth-child({}) button.item__button.item__button--addToComparison".format(i))

    add_to_cart.click()
    print('Add item {} in comparison'.format(i))

    browser.execute_script("return arguments[0].scrollIntoView(true);", add_to_cart)

print()
cart = browser.find_element_by_css_selector("a.mainHeader__btn.mainHeader__btn--comparison")
cart.click()
time.sleep(1)
print('Go to Comparison')
print()

len_comparison = len(browser.find_elements_by_css_selector("tbody td img"))
print(f"In comparison is {len_comparison} items!")

for i in range(1, 11):

    delite_item = browser.find_element_by_css_selector(
        "a.comparison__btn.comparison__btn--delete")
    start = datetime.now()
    delite_item.click()
    end = datetime.now()
    print('Delite item {} - {}'.format(i, str(end - start)))



time.sleep(1)
print()
print('Bye!!!')

browser.quit()
