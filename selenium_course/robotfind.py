import math
def calc(x_value):
  return str(math.log(abs(12*math.sin(int(x_value)))))
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.XPATH, "//img")
    x_value = x_element.get_attribute("valuex")
    y = calc(x_value)
    input1 = browser.find_element(By.XPATH, "//input[@id='answer']")
    input1.send_keys(y)
    input2 = browser.find_element(By.XPATH, "//input[@id='robotCheckbox']")
    input2.click()
    input3 = browser.find_element(By.XPATH, "//input[@id='robotsRule']")
    input3.click()
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
