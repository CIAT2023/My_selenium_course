from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://stepik.org/lesson/236895/step/1"

browser = webdriver.Chrome()
browser.get(link)