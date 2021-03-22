from selenium import webdriver
import time
import os
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_xpath("//div/input[@name='firstname']")
    input1.send_keys("Максим")

    input2 = browser.find_element_by_xpath("//div/input[@name='lastname']")
    input2.send_keys("Петров")

    input3 = browser.find_element_by_xpath("//div/input[@name='email']")
    input3.send_keys("dhcch@email.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "manyal.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)


    input2 = browser.find_element_by_xpath("//button")
    input2.click()

finally:
    time.sleep(10)
    browser.quit()