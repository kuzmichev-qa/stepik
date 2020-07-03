from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.implicitly_wait(12)
driver.get("http://suninjuly.github.io/explicit_wait2.html")

WebDriverWait(driver, 12).until(
        EC.text_to_be_present_in_element((By.XPATH, "//*[@id = 'price']"), "$100"))
driver.find_element_by_xpath("//*[@id = 'book']").click()