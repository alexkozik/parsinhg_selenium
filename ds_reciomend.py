from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time


# Настройки для Selenium с Firefox
gecko_driver_path = "/snap/bin/geckodriver"  # Укажите путь к geckodriver
service = Service(gecko_driver_path)
options = Options()
options.add_argument("--headless")  # Запуск в фоновом режиме (без открытия браузера)
browser = webdriver.Firefox(service=service, options=options)

browser.get("https://en.wikipedia.org/wiki/Document_Object_Model")
print("Страница загружена:", browser.title)
time.sleep(5)
browser.quit()