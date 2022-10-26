import os
from selenium import webdriver
from selenium.webdriver.common.by import By

"""Задание: загрузка файла
Открыть страницу http://suninjuly.github.io/file_input.html
Заполнить текстовые поля: имя, фамилия, email
Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
Нажать кнопку "Отправить"
"""

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/file_input.html')

input1 = browser.find_element(By.NAME, "firstname")
input1.send_keys("Ivan")
input2 = browser.find_element(By.NAME, "lastname")
input2.send_keys("Petrov")
input3 = browser.find_element(By.NAME, "email")
input3.send_keys("test@test.ru")


current_dir = os.path.abspath(os.path.dirname(__file__))   # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла


file_input = browser.find_element(By.CSS_SELECTOR, 'input[name="file"]')
file_input.send_keys(file_path)
browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()