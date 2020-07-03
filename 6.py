from selenium import webdriver
import os

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://suninjuly.github.io/file_input.html")

driver.find_element_by_xpath("//*[@name = 'firstname']").send_keys("Уася")
driver.find_element_by_xpath("//*[@name = 'lastname']").send_keys("ТожеУася")
driver.find_element_by_xpath("//*[@name = 'email']").send_keys("Uasja@uasja.ru")

txt_file = os.path.abspath("C:\\downloads\\1.txt")
file_input = driver.find_element_by_xpath("//*[@name = 'file']")
file_input.send_keys(txt_file)

driver.find_element_by_xpath("//button[text()= 'Submit']").click()

