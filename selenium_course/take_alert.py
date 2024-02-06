import math
def calc(x_value):
  return str(math.log(abs(12*math.sin(int(x_value)))))
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button_alert = browser.find_element(By.XPATH, "//button[@type='submit']")
    button_alert.click()

    alert = browser.switch_to.alert
    alert.accept()

    x_element = browser.find_element(By.XPATH, "//span[@id='input_value']")
    x_value = x_element.text
    y = calc(x_value)
    input_answer = browser.find_element(By.XPATH, "//input[@id='answer']")
    input_answer.send_keys(y)
    
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
