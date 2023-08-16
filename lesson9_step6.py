# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

browser = webdriver.Chrome()
browser.get(link)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:

    dut = browser.find_element(By.CLASS_NAME, "btn")
    dut.click()

    browser.implicitly_wait(2)
    window_name = browser.window_handles[1]
    browser.switch_to.window(window_name)

    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    dut = browser.find_element(By.CLASS_NAME, "btn")
    dut.click()




finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()