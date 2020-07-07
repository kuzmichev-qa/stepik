import pytest

from homework.helper import *


@pytest.mark.parametrize('language', ["ru", "fr", "es"])
class TestLanguage(object):

    def test_guest_should_see_login_link(self, browser, language):
        link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
        browser.get(link)

        assert is_element_present(browser, By.XPATH, "//*[@id = 'add_to_basket_form']"), "No button"
