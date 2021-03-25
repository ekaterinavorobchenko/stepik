
def test_buttun(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    button = browser.find_element_by_css_selector("#add_to_basket_form")
    assert button, "Кнопка не найдена"



