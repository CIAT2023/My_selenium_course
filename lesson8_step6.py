# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
import time
import math

link = "https://SunInJuly.github.io/execute_script.html"

browser = webdriver.Chrome()
browser.get(link)

def calc (x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    el_1 = browser.find_element(By.ID, "input_value")
    x = el_1.text
    y = calc(x)

   #button = browser.find_element(By.TAG_NAME, "button")
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    input2 = browser.find_element(By.ID, "robotCheckbox")
    input2.click()

    input3 = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input3)
    input3.click()

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

