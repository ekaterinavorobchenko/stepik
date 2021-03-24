import pytest
from selenium import webdriver
import time
import math

answer = math.log(int(time.time()))

def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('link',["https://stepik.org/lesson/236895/step/1","https://stepik.org/lesson/236896/step/1","https://stepik.org/lesson/236897/step/1",
                         "https://stepik.org/lesson/236898/step/1","https://stepik.org/lesson/236899/step/1","https://stepik.org/lesson/236903/step/1",
                         "https://stepik.org/lesson/236904/step/1","https://stepik.org/lesson/236905/step/1"])
class Testlink():
    def test_link(link, browser):
        browser.get(link)

        input = browser.find_element_by_id("ember86")
        input.send_keys(answer)

        button = browser.find_element_by_class("submit-submission")
        button.click()