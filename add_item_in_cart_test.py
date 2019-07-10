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

for i in range(1, 6):
    add_to_cart = browser.find_element_by_css_selector(
        "div.catalog__list.itemWrapper .item:nth-child({}) .item__button--addToCart".format(i))
    add_to_cart.click()
    print('Add item {} in cart'.format(i))
    time.sleep(1)

cart = browser.find_element_by_css_selector("a.mainHeader__btn.mainHeader__btn--cart")
cart.click()
time.sleep(1)
print('Go to Cart')

len_cart = len(browser.find_elements_by_css_selector("div.cart__list section"))
print(f"In cart is {len_cart} items!")

for i in range(1, 6):
    delite_item = browser.find_element_by_css_selector(
        "div.cart__list section:nth-child(1) a.item__delete")
    start = datetime.now()
    delite_item.click()
    end = datetime.now()

    print('Delite item {} - {}'.format(i, str(end - start)))
    time.sleep(1)

time.sleep(1)
print()
print('Bye!!!')

browser.quit()
