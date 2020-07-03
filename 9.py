from selenium import webdriver
from selenium.webdriver.support.ui import Select
import random


url = "http://selenium1py.pythonanywhere.com/ru/"


def test_check_language():
    try:
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get(url)
        select = Select(driver.find_element_by_tag_name("select"))
        select.select_by_value("de")
        driver.find_element_by_xpath("//button[@class = 'btn btn-default']").click()

        new_language = driver.find_element_by_xpath("//button[@class = 'btn btn-default']").text
        assert new_language != "Выполнить"
        assert new_language == "Ausführen"
    finally:
        driver.quit()


def test_check_basket():
    try:
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get(url)
        driver.find_element_by_xpath("//*[text() = 'Посмотреть корзину']").click()
        t2 = driver.find_element_by_xpath("//*[@class = 'page-header action']/h1").text
        assert t2 == "Корзина"
    finally:
        driver.quit()


def test_check_ragistration():
    try:
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get(url)
        random_email = random.randint(100000, 999999)
        driver.find_element_by_xpath("//*[@id = 'login_link']").click()
        driver.find_element_by_xpath("//*[@name = 'registration-email']").send_keys(str(random_email)+'@1.ru')
        driver.find_element_by_xpath("//*[@name = 'registration-password1']").send_keys('123456789ww')
        driver.find_element_by_xpath("//*[@name = 'registration-password2']").send_keys('123456789ww')
        driver.find_element_by_xpath("//*[@name = 'registration_submit']").click()
        driver.find_element_by_xpath("//a[@href = '/ru/accounts/']").click()
        checked_element = driver.find_element_by_xpath("//div[@class = 'page-header action']/h1").text
        assert checked_element == "Профиль"
    finally:
        driver.quit()


def test_login():
    try:
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get(url)
        driver.find_element_by_xpath("//*[@id = 'login_link']").click()
        driver.find_element_by_xpath("//*[@name = 'login-username']").send_keys("967123@1.ru")
        driver.find_element_by_xpath("//*[@name = 'login-password']").send_keys("123456789ww")
        driver.find_element_by_xpath("//*[@name = 'login_submit']").click()
        driver.find_element_by_xpath("//a[@href = '/ru/accounts/']").click()
        checked_element = driver.find_element_by_xpath("//div[@class = 'page-header action']/h1").text
        assert checked_element == "Профиль"
    finally:
        driver.quit()


def test_check_books_list():
    try:
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get(url)
        driver.find_element_by_xpath("//*[text() = 'Все товары']").click()
        books_list = driver.find_elements_by_xpath("//*[@class = 'product_pod']")
        assert len(books_list) >= 10
    finally:
        driver.quit()


if __name__ == "__main__":
   test_check_basket()
   test_check_books_list()
   test_check_language()
   test_check_ragistration()
   test_login()
