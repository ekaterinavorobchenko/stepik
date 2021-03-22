from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_xpath("//button")
    input1.click()

    new_window = browser.window_handles[1]
    browser.switch_to_window(new_window)

    time.sleep(3)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_xpath("//div/input[@id='answer']")
    input1.send_keys(y)


    input2 = browser.find_element_by_xpath("//button")
    input2.click()

finally:
    time.sleep(10)
    browser.quit()