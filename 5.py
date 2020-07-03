from selenium import webdriver


driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/execute_script.html")

num1 = driver.find_element_by_xpath("//span[@id = 'input_value']").text


driver.find_element_by_xpath("//select[@id = 'dropdown']").click()

driver.find_element_by_xpath(f"//option[@value = '{int(num1)+int(num2)}']").click()
driver.find_element_by_xpath("//button[@type = 'submit']").click()