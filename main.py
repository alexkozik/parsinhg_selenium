from selenium import webdriver
from selenium.webdriver import Keys
#Библиотека, которая позволяет вводить данные на сайт с клавиатуры
from selenium.webdriver.common.by import By
#Библиотека с поиском элементов на сайте
import time
#С помощью time мы можем делать задержки в программе
import random

from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

# Настройки для Selenium с Firefox
gecko_driver_path = "/snap/bin/geckodriver"  # Укажите путь к geckodriver
service = Service(gecko_driver_path)
options = Options()
options.add_argument("--headless")  # Запуск в фоновом режиме (без открытия браузера)

#Если мы работаем с Firefox
browser = webdriver.Firefox(service=service, options=options)

print("Добрый день! Вас приветствует программа консольного поиска информации в Википедии." )
user_input = input("Что вы хотите найти? - ")

browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")

assert "Википедия" in browser.title

search_box = browser.find_element(By.ID,"searchInput")
time.sleep(5)
search_box.send_keys(user_input)
search_box.send_keys(Keys.RETURN)
time.sleep(5)
note_heading = browser.find_element(By.CLASS_NAME,"mw-search-result-heading")
a = note_heading.find_element(By.TAG_NAME, "a")
a.click()
time.sleep(5)
browser.save_screenshot("note.png")
print("Страница загружена:", browser.title)

browser.quit()
