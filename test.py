from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_xpath("//div/label/span[@id='input_value']")
    x = x_element.text
    y = calc(x)

    button = browser.find_element_by_xpath("//button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)


    option1 = browser.find_element_by_xpath("//div/input[@type='checkbox']")
    option1.click()

    option2 = browser.find_element_by_id("robotsRule")
    option2.click()

    input2 = browser.find_element_by_xpath("//button")
    input2.click()

finally:
    time.sleep(10)
    browser.quit()