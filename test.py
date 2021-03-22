from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


def sum(x, y):
    return str(x + y)

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("num1")
    x_e = x_element.text
    x = int(x_e)

    y_element = browser.find_element_by_id("num2")
    y_e = y_element.text
    y = int(y_e)
    summa = sum(x,y)




    select = Select(browser.find_element_by_class_name("custom-select"))
    select.select_by_value(summa)  # ищем элемент с текстом "Python"


    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(10)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()