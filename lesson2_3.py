import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

"""Задание: принимаем alert
В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:
Открыть страницу http://suninjuly.github.io/alert_accept.html
Нажать на кнопку
Принять confirm
На новой странице решить капчу для роботов, чтобы получить число с ответом
"""

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()


    confirm = browser.switch_to.alert
    confirm.accept()


    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(calc(x))
    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()