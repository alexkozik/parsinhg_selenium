import time
#С помощью time мы можем делать задержки в программе


from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

options = Options()
options.binary_location = "/usr/bin/firefox"  # Путь к Firefox (проверьте `which firefox`)

# driver = webdriver.Firefox(options=options)

#Если мы работаем с Firefox
browser = webdriver.Firefox(options=options)
browser.get("https://en.wikipedia.org/wiki/Document_Object_Model")
#В кавычках указываем URL сайта, на который нам нужно зайти
time.sleep(10)
#Задержка в 10 секунд
browser.quit()
#Закрываем браузер