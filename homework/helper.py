from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def is_element_present(browser, how, what):
    try:
        browser.find_element(by=how, value=what)
    except NoSuchElementException:
        return False
    return True