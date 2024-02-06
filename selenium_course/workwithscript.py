from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = "http://suninjuly.github.io/get_attribute.html"

try:

    browser = webdriver.Chrome()
    #browser.execute_script("alert('Robots at work');")
    browser.execute_script("document.title='Script executing';alert('Robots at work');")

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
