from selenium import webdriver
import unittest
import time

class TestAbs(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        print("Browser Opened")

    def test_open_chercher_tech1(self):
        self.driver.get("http://suninjuly.github.io/registration1.html")
        time.sleep(2)
        print("Chrome")


        input = self.driver.find_element_by_css_selector('.first_block .first')
        input.send_keys('Маша')

        input = self.driver.find_element_by_css_selector('.first_block .second')
        input.send_keys('Дубинина')

        input = self.driver.find_element_by_css_selector('.first_block .third')
        input.send_keys('eka-vorobchenko@mail.ru')

        time.sleep(2)

        button = self.driver.find_element_by_css_selector('.btn')
        button.click()

        self.assertEqual(self.driver.find_element_by_tag_name("h1").text, "Congratulations! You have successfully registered!", 'Error Registration 1')


    def test_open_chercher_tech2(self):
        self.driver.get("http://suninjuly.github.io/registration2.html")
        time.sleep(2)
        print("Chrome")

        input = self.driver.find_element_by_css_selector('.first_block .first')
        input.send_keys('Маша')

        input = self.driver.find_element_by_css_selector('.first_block .third')
        input.send_keys('dsjhckdhdhbck@fjdzkvjndfv')

        time.sleep(2)

        button = self.driver.find_element_by_class_name('btn')
        button.click()

        self.assertEqual(self.driver.find_element_by_tag_name("h1").text,"Congratulations! You have successfully registered!", 'Error Registration 1')

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()