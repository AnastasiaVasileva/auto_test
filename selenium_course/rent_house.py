import math
def calc(x_value):
  return str(math.log(abs(12*math.sin(int(x_value)))))
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time 

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    wait_price = WebDriverWait(browser, 12).until(
      EC.text_to_be_present_in_element((By.ID, "price"), "100")
      )
    buy = browser.find_element(By.XPATH, "//button[@id='book']")
    buy.click()

    browser.execute_script("window.scrollTo(0, 900)")

    tsarea = browser.find_element(By.XPATH, "//input[@id='answer']")
    x_element = browser.find_element(By.XPATH, "//span[@id='input_value']")
    x_value = x_element.text
    y = calc(x_value)
    tsarea.send_keys(y)

    but_click = browser.find_element(By.XPATH, "//button[@id='solve']")
    but_click.click()
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
