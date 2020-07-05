import pytest
import random


def test_avtorization(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    random_email = random.randint(100000, 999999)
    browser.find_element_by_xpath("//*[@id = 'login_link']").click()
    browser.find_element_by_xpath("//*[@name = 'registration-email']").send_keys(str(random_email) + '@1.ru')
    browser.find_element_by_xpath("//*[@name = 'registration-password1']").send_keys('123456789ww')
    browser.find_element_by_xpath("//*[@name = 'registration-password2']").send_keys('123456789ww')
    browser.find_element_by_xpath("//*[@name = 'registration_submit']").click()
    browser.find_element_by_xpath("//a[@href = '/ru/accounts/']").click()
    checked_element = browser.find_element_by_xpath("//div[@class = 'page-header action']/h1").text
    assert checked_element == "Профиль"


