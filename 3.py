from selenium import webdriver
import time
import unittest


class TestAbs(unittest.TestCase):

    def test_1(self):
        try:
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)
            first_name = browser.find_element_by_tag_name("input")
            first_name.send_keys("Ivan")
            last_name = browser.find_elements_by_class_name("form-control")[1]
            last_name.send_keys("Petrov")
            email = browser.find_element_by_css_selector("[placeholder = 'Input your email']")
            email.send_keys("S11@22.ru")
            phone = browser.find_element_by_xpath("//input[@placeholder = 'Input your phone:']")
            phone.send_keys("+71723843544")
            addres = browser.find_element_by_xpath("//label[.='Address:']//..//input")
            addres.send_keys("")
            button = browser.find_element_by_css_selector("button.btn")
            button.click()
            time.sleep(1)
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            welcome_text = welcome_text_elt.text
            assert "Congratulations! You have successfully registered!" == welcome_text

        finally:
            time.sleep(10)
            browser.quit()


if __name__ == "__main__":
    unittest.main()