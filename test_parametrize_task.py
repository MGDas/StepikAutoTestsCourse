from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
import time
import math

@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

def answer():
    return str(math.log(int(time.time())))

links = ['236895', '236896', '236897', '236898', '236899', '236899', '236904', '236905']

class TestAnswer:

    @pytest.mark.parametrize('link', links)
    def test_1(self, browser, link):
        browser.get(f'https://stepik.org/lesson/{link}/step/1')
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.TAG_NAME, "textarea")))

        browser.find_element_by_tag_name('textarea').send_keys(answer())

        browser.find_element_by_css_selector('.submit-submission').click()

        WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'smart-hints__hint')))

        correct = browser.find_element_by_css_selector('.smart-hints__hint').text
        assert correct == 'Correct!', "f{correct}"
