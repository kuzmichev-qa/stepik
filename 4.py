from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/get_attribute.html")

x_element = driver.find_element_by_xpath("//img[@id = 'treasure']")
x = x_element.get_attribute('valuex')
y = calc(x)
print(y)
driver.find_element_by_xpath("//*[@id = 'answer']").send_keys(y)
driver.find_element_by_xpath("//*[@id = 'robotCheckbox']").click()
driver.find_element_by_xpath("//*[@id = 'robotsRule']").click()
driver.find_element_by_xpath("//button[@class = 'btn btn-default']").click()