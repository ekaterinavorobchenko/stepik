from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium import webdriver
import time
import math

answer = math.log(int(time.time()))

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('link',["https://stepik.org/lesson/236895/step/1","https://stepik.org/lesson/236896/step/1","https://stepik.org/lesson/236897/step/1",
                         "https://stepik.org/lesson/236898/step/1","https://stepik.org/lesson/236899/step/1","https://stepik.org/lesson/236903/step/1",
                         "https://stepik.org/lesson/236904/step/1","https://stepik.org/lesson/236905/step/1"])

def test_link(link, browser):
    browser.get(link)


    input = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div .textarea"))
    )
    input.send_keys(str(answer))


    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
    )
    button.click()

    result = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "smart-hints__hint"))
    )

    assert result.text == "Correct!", print(result.text)




