import time
import math

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By

link = "https://suninjuly.github.io/get_attribute.html"

page = webdriver.Chrome()
page.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
  chest = page.find_element(By.ID, "treasure")
  chest_val = int( chest.get_attribute("valuex"))

  y = calc(chest_val)

  pole = page.find_element(By.ID, "answer")
  pole.send_keys(y)

  robot = page.find_element(By.ID, "robotCheckbox")
  robot.click()

  robot1 = page.find_element(By.ID, "robotsRule")
  robot1.click()

  button = page.find_element(By.CSS_SELECTOR, ".btn")
  button.click()

finally:
  # ожидание чтобы визуально оценить результаты прохождения скрипта
  time.sleep(20)
  # закрываем браузер после всех манипуляций
  page.quit()

