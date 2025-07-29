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

browser.get("https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D0%BB%D0%BD%D0%B5%D1%87%D0%BD%D0%B0%D1%8F_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0")
time.sleep(5)
browser.save_screenshot("prepare.png")
print("Страница загружена:", browser.title)

paragraphs = browser.find_elements(By.TAG_NAME, "p")
#Для перебора пишем цикл
for paragraph in paragraphs:
    print(paragraph.text)
    if input() == "q":
        break

hatnotes = []
for element in browser.find_elements(By.TAG_NAME, "div"):
    #Чтобы искать атрибут класса
    cl = element.get_attribute("class")
    if cl == "hatnote navigation-not-searchable ts-main":
        hatnotes.append(element)

print(hatnotes)
hatnote = random.choice(hatnotes)

#Для получения ссылки мы должны найти на сайте тег "a" внутри тега "div"
link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
browser.get(link)
time.sleep(5)
browser.save_screenshot("randomHatNote.png")
print("Страница загружена:", browser.title)



browser.quit()
