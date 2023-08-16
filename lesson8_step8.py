# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
import time
import os

link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()
browser.get(link)

try:
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("sergsiat@gmail.com")
    input4 = browser.find_element(By.NAME, "file")




    current_dir = os.path.abspath(os.path.dirname("/home/psv/My_selenium_course/txt.txt"))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'txt.txt')  # добавляем к этому пути имя файла
    input4.send_keys(file_path)
    input5 = browser.find_element(By.CLASS_NAME, "btn")
    input5.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

