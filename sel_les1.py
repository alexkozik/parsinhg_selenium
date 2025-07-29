import time
#С помощью time мы можем делать задержки в программе


from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

# Настройки для Selenium с Firefox
gecko_driver_path = "/snap/bin/geckodriver"  # Укажите путь к geckodriver
service = Service(gecko_driver_path)
options = Options()
options.add_argument("--headless")  # Запуск в фоновом режиме (без открытия браузера)

#Если мы работаем с Firefox
browser = webdriver.Firefox(service=service, options=options)

browser.get("https://en.wikipedia.org/wiki/Document_Object_Model")
browser.save_screenshot("dom.png")
print("Страница загружена:", browser.title)
time.sleep(5)
browser.get("https://ru.wikipedia.org/wiki/Selenium")
browser.save_screenshot("selenium.png")
print("Страница загружена:", browser.title)
time.sleep(3)
browser.refresh()

browser.quit()
#Закрываем браузер