# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"
link2 = "http://suninjuly.github.io/selects2.html"

def calk(var1, var2):
    return var1 + var2

page = webdriver.Chrome()
page.get(link)

try:
    var1 = int(page.find_element(By.ID, "num1").text)
    var2 = int(page.find_element(By.ID, "num2").text)
    rez = str(calk(var1, var2))

    select = Select(page.find_element(By.ID, "dropdown"))
    select.select_by_value(rez)

    button = page.find_element(By.CLASS_NAME, "btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    page.quit()

