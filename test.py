from selenium import webdriver
import unittest

class TestAbs(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'D:PATHchromedriver.exe')
        print("Browser Opened")
        
    def test_open_chercher_tech(self):
        self.driver.get("http://suninjuly.github.io/registration1.html")
        print("Chrome")

    input = driver.find_element_by_xpath('//div[1]/div[1]/input')
    input.send_keys('Маша')

    input = driver.find_element_by_xpath('//div[1]/div[2]/input')
    input.send_keys('Дубинина')

    input = driver.find_element_by_xpath('//div[1]/div[3]/input')
    input.send_keys('eka-vorobchenko@mail.ru')

    button = driver.find_element_by_xpath('//div/form/button')
    button.click()

    def test_abs1(self):
        self.assertEqual(browser.find_element_by_tag_name("h1").text, "Congratulations! You have successfully registered!", 'Error Registration 1')


    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input = browser.find_element_by_xpath('//div[1]/div[1]/input')
    input.send_keys('Маша')

    input = browser.find_element_by_xpath('//div[1]/div[2]/input')
    input.send_keys('dsjhckdhdhbck@fjdzkvjndfv')

    button = browser.find_element_by_xpath('//div/form/button')
    button.click()


    def test_abs2(self):
        self.assertEqual(browser.find_element_by_tag_name("h1").text, "Congratulations! You have successfully registered!", 'Error Registration 1')

if __name__ == "__main__":
    unittest.main()