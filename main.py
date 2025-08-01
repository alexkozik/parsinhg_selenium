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

import textwrap
import os


def get_console_width():
    try:
        # Получаем ширину консоли (для Unix и Windows)
        return os.get_terminal_size().columns
    except:
        # Если не удалось определить, возвращаем стандартную ширину (80 символов)
        return 80


def print_wrapped(text, width=None):
    if width is None:
        width = get_console_width() - 4  # Оставляем небольшой отступ

    # Разбиваем текст на абзацы и обрабатываем каждый отдельно
    paragraphs = text.split('\n')
    for para in paragraphs:
        if para.strip():  # Пропускаем пустые строки
            # Переносим текст с учетом ширины консоли
            wrapped_lines = textwrap.wrap(para, width=width)
            for line in wrapped_lines:
                print(line)
        else:
            print()  # Печатаем пустую строку для разделения абзацев

# Настройки для Selenium с Firefox
gecko_driver_path = "/snap/bin/geckodriver"  # Укажите путь к geckodriver
service = Service(gecko_driver_path)
options = Options()
options.add_argument("--headless")  # Запуск в фоновом режиме (без открытия браузера)

#Если мы работаем с Firefox
browser = webdriver.Firefox(service=service, options=options)

print("Добрый день!\nВас приветствует программа консольного поиска информации в Википедии." )
user_input = input("Что вы хотите найти? - ")

browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")

assert "Википедия" in browser.title

search_box = browser.find_element(By.ID,"searchInput")
time.sleep(5)
search_box.send_keys(user_input)
search_box.send_keys(Keys.RETURN)
# if not search_box.exists():
#         print("Страница не найдена. Попробуйте другой запрос.")
#         return
time.sleep(5)

note_heading = browser.find_element(By.CLASS_NAME,"mw-search-result-heading")


a = note_heading.find_element(By.TAG_NAME, "a")
a.click()
time.sleep(5)
browser.save_screenshot("start_page.png")

current_page = browser


while True:
    print("\nТекущая статья:", current_page.title)
    print("Выберите действие:")
    print("1. Листать параграфы текущей статьи")
    print("2. Перейти на одну из связанных страниц")
    print("3. Выйти из программы")

    page_content = browser.find_element(By.ID,"mw-content-text")

    # Формируем списки параграфов и связанных страниц
    paragraphs = page_content.find_elements(By.TAG_NAME, "p")
    para_list = []
    links_list = []
    for para in paragraphs:
        if para.text.strip():  # Пропускаем пустые параграфы
            para_list.append(para)
            links = para.find_elements(By.TAG_NAME, "a")
            for link in links:
                if link.get_attribute("title").strip():  # Пропускаем ссылки без названия
                    links_list.append(link)

    choice = input("Ваш выбор (1/2/3): ")

    if choice == '1':
        # Вывод параграфов текущей статьи
        print("\nПараграфы статьи:")
        for i, para in enumerate(para_list):
            print(f"{i + 1}. {para.text[:100]}...")  # Выводим первые 100 символов

        para_choice = input("\nВведите номер параграфа для подробного просмотра (или Enter чтобы вернуться): ")
        if para_choice.isdigit() and 0 < int(para_choice) <= len(para_list):
            print_wrapped("\n" + para_list[int(para_choice) - 1].text,100)
    elif choice == '2':
        if not links_list:
            print("Нет связанных страниц.")
            continue

        print("\nСвязанные страницы:")
        for i, link in enumerate(links_list[:20]):  # Ограничим вывод 20 ссылками
            print(f"{i + 1}. {link.get_attribute("title")}")

        link_choice = input("\nВведите номер связанной страницы для перехода (или Enter чтобы вернуться): ")
        if link_choice.isdigit() and 0 < int(link_choice) <= len(links_list):
            selected_link = links_list[int(link_choice) - 1]
            selected_link.click()
            time.sleep(5)
            browser.save_screenshot("linked_page.png")
            current_page = browser
            print(f"\nПереход на страницу: {current_page.title}\n")
    elif choice == '3':
        break
#
# paragraphs = browser.find_elements(By.TAG_NAME, "p")
# #Для перебора пишем цикл
# for paragraph in paragraphs:
#     print(paragraph.text.strip())
#     if input() == "q":
#         break
#
# links = []
# for element in paragraph.find_elements(By.TAG_NAME, "a"):
#     link = element.get_attribute("href")
#     links.append(link)
#
# print(links)

browser.quit()
