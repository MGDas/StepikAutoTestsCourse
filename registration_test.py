from selenium import webdriver

def register(url):

    browser = webdriver.Chrome()
    browser.get(url)

    num, data = ['first', 'second', 'third'], ['Petr', 'Petrov', 'petrov@mail.com']
    for n, d in zip(num, data):
        browser.find_element_by_css_selector(f'input[required].{n}').send_keys(f'{d}')

    browser.find_element_by_tag_name('button').click()
    welcome_text = browser.find_element_by_tag_name("h1").text

    browser.quit()

    return welcome_text
