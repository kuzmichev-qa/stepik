from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://suninjuly.github.io/redirect_accept.html")

driver.find_element_by_xpath("//button[@class = 'trollface btn btn-primary']").click()

new_window = driver.window_handles[1]
driver.switch_to.window(new_window)

x_element = driver.find_element_by_xpath("//*[@id='input_value']").text
y = calc(x_element)
driver.find_element_by_xpath("//*[@id = 'answer']").send_keys(y)
driver.find_element_by_xpath("//button[@class = 'btn btn-primary']").click()