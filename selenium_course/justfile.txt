import math
def calc(x_value):
  return str(math.log(abs(12*math.sin(int(x_value)))))
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.XPATH, "//span[@id='input_value']")
    x_value = x_element.text
    y = calc(x_value)
    input_answer = browser.find_element(By.XPATH, "//input[@id='answer']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input_answer)
    input_answer.click()
    input_answer.send_keys(y)
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
