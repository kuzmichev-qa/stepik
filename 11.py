import pytest
import time
import math
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('url', ["236895", "236897"])
def test_guest_should_see_login_link(browser, url):
    link = f"https://stepik.org/lesson/{url}/step/1/"
    browser.get(link)
    answer = math.log(int(time.time()))
    browser.find_element_by_xpath("//*[@placeholder = 'Напишите ваш ответ здесь...']").send_keys(str(answer))
    browser.find_element_by_xpath("//button[@class= 'submit-submission']").click()
    a = browser.find_element_by_xpath("//*[text()= 'Correct!']")
    correct_text = a.text
    assert correct_text == "Correct!"