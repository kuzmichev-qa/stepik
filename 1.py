from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://suninjuly.github.io/alert_accept.html")

driver.find_element_by_xpath("//*[text() = 'I want to go on a magical journey!']").click()
alert = driver.switch_to.alert
alert.accept()
x_element = driver.find_element_by_xpath("//*[@id='input_value']").text
y = calc(x_element)
driver.find_element_by_xpath("//*[@id = 'answer']").send_keys(y)
driver.find_element_by_xpath("//button[@class = 'btn btn-primary']").click()

