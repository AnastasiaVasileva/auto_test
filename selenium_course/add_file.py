import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.XPATH, "//input[@name='firstname']")
    first_name.send_keys('Test')

    last_name = browser.find_element(By.XPATH, "//input[@name='lastname']")
    last_name.send_keys('Nast')

    email = browser.find_element(By.XPATH, "//input[@name='email']")
    email.send_keys('testnast@gmail.com')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "justfile.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.XPATH, "//input[@id='file']")
    element.send_keys(file_path)

    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
