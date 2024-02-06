import math
def calc(x_value):
  return str(math.log(abs(12*math.sin(int(x_value)))))
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time 

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.XPATH, "//span[@id='num1']")
    num_value1 = num1.text

    num2 = browser.find_element(By.XPATH, "//span[@id='num2']")
    num_value2 = num2.text

    num_sum = int(num_value1) + int(num_value2)

    select = Select(browser.find_element(By.XPATH, "//select[@id='dropdown']"))
    select.select_by_value(str(num_sum))

    button = browser.find_element(By.XPATH, "//button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
