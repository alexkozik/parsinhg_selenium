from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import time

options = Options()
options.binary_location = "/usr/bin/firefox"  # Проверенный путь

# Явно указываем путь к geckodriver
service = Service(executable_path="/usr/local/bin/geckodriver")

options.add_argument("--headless")  # Добавьте эту строку перед созданием driver
options.add_argument("--disable-gpu")  # На некоторых системах требуется
options.add_argument("--no-sandbox")  # Для Linux-систем
options.add_argument("--disable-dev-shm-usage")  # Ограничение памяти

browser = webdriver.Firefox(service=service, options=options)
browser.get("https://en.wikipedia.org/wiki/Document_Object_Model")
print("Страница загружена:", browser.title)
time.sleep(5)
browser.quit()