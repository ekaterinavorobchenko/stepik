from selenium import webdriver
import time


from selenium.webdriver.chrome.webdriver import WebDriver



try:
    link = "http://suninjuly.github.io/cats.html"
    browser: WebDriver = webdriver.Chrome()
    browser.get(link)

    input = browser.find_element_by_id("button")


finally:
    time.sleep(10)
    browser.quit()