import pytest
from selenium.common.exceptions import NoSuchElementException


@pytest.mark.parametrize('language', ["ru", "es"])
class TestLanguage(object):
    def test_guest_should_see_login_link(self, browser, language):
        link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
        browser.get(link)

        button = browser.find_element_by_xpath("//button[@value ='Añadir al carrito']")
        assert button, "Нет кнопки "'"Добавить в корзину"'""