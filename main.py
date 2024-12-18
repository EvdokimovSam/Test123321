# from selenium import webdriver
# from time import sleep
#
# driver = webdriver.Chrome()
#
# driver.get('http://www.saucedemo.com/')
# driver.maximize_window()
#
# sleep(5)

#
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time
#
# # Настройка веб-драйвера для Chrome
# driver = webdriver.Chrome()  # Убедитесь, что chromedriver находится в PATH
#
# try:
#     # Открываем сайт
#     driver.get("http://www.saucedemo.com/")
#     driver.maximize_window()
#     # Ищем поле для логина и вводим данные
#     username_field = driver.find_element(By.ID, "user-name")
#     username_field.send_keys("standard_user")  # Пример логина
#     time.sleep(3)
#     # Ищем поле для пароля и вводим данные
#     password_field = driver.find_element(By.ID, "password")
#     password_field.send_keys("secret_sauce")  # Пример пароля
#     time.sleep(3)
#     # Имитация нажатия клавиши Enter (по желанию)
#     password_field.send_keys(Keys.RETURN)
#
#     # Пауза для визуального контроля
#     time.sleep(3)
#
# finally:
#     # Закрытие браузера
#     driver.quit()


# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# # Запускаем браузер
# driver = webdriver.Chrome()
#
# try:
#     # Открываем тестовый сайт
#     driver.get("http://www.saucedemo.com/")
#

#     # Поиск поля логина с помощью XPath
#     username_field = driver.find_element(By.XPATH, "//input[@id='user-name']")
#     username_field.send_keys("standard_user")
#     time.sleep(3)
#     # Поиск поля пароля с помощью XPath
#     password_field = driver.find_element(By.XPATH, "//input[@id='password']")
#     password_field.send_keys("secret_sauce")
#     time.sleep(3)
#     # Поиск кнопки Login и клик по ней
#     login_button = driver.find_element(By.XPATH, "//input[@type='submit']")
#     login_button.click()
#     time.sleep(3)
# finally:
#     # Закрытие браузера
#     driver.quit()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
#
# # Настройка WebDriver
# driver = webdriver.Chrome()
#
# try:
#     # Открываем тестовый сайт
#     driver.get("https://www.saucedemo.com/")
#
#     # Ввод логина
#     driver.find_element(By.ID, "user-name").send_keys("standard_user")
#     time.sleep(3)
#     # Ввод пароля
#     driver.find_element(By.ID, "password").send_keys("secret_sauce")
#     time.sleep(3)
#     # Нажатие на кнопку Login
#     driver.find_element(By.ID, "login-button").click()
#     time.sleep(3)
#     # Явное ожидание загрузки страницы
#     WebDriverWait(driver, 10).until(
#         EC.url_to_be("https://www.saucedemo.com/inventory.html")
#     )
#
#     # Проверка URL
#     correct_url = "https://www.saucedemo.com/inventory.html"
#     current_url = driver.current_url
#     assert correct_url == current_url, "URL тест провален: редирект на неверную страницу"
#     print("URL тест пройден: пользователь успешно перенаправлен на страницу каталога")
#     time.sleep(3)
#     # Проверка текста "Products" на странице
#     header = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, '//*[@id="header_container"]/div[2]/span'))
#     ).text
#     correct_text = "Products"
#     assert header == correct_text, "Текстовый тест провален: заголовок неверный"
#     print("Текстовый тест пройден: заголовок страницы верный")
#     time.sleep(3)
# finally:
#     # Закрытие браузера
#     driver.quit()
#

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Настройка опций браузера
chrome_options = Options()
chrome_options.add_argument("--headless")  # Включение headless-режима
chrome_options.add_argument("--disable-gpu")  # Отключение GPU для стабильности (необязательно)
chrome_options.add_argument("--window-size=1920,1080")  # Установка размера окна браузера

# Запуск браузера в headless-режиме
driver = webdriver.Chrome(options=chrome_options)

try:
    # Открытие страницы
    driver.get("http://www.saucedemo.coчm/")

    # Получение заголовка страницы
    print("Заголовок страницы:", driver.title)

finally:
    # Закрытие браузера
    driver.quit()

