# webdriver это и есть набор команд для управления браузером
from selenium import webdriver
# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import Select
import time
import math

link = "https://ppb-stg-01.ciat.net.ua"

browser = webdriver.Chrome()
browser.get(link)


try:
    browser.implicitly_wait(5)

    input1 = browser.find_element(By.NAME, "login")
    input1.send_keys("CIAT")

    input2 = browser.find_element(By.NAME, "password")
    input2.send_keys("CIAT1985")

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    user_pick = browser.find_element(By.CLASS_NAME, "fa-user")

    print("_____all right__________")
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()