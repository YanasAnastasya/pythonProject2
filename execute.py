from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

"""Задание на execute_script
Открыть страницу http://SunInJuly.github.io/execute_script.html.
Считать значение для переменной x.
Посчитать математическую функцию от x.
Проскроллить страницу вниз.
Ввести ответ в текстовое поле.
Выбрать checkbox "Подтверждаю, что являюсь роботом".
Переключить radiobutton "Роботы рулят!".
Нажать на кнопку "Отправить".
"""


try:
    browser = webdriver.Chrome()
    link = "http://SunInJuly.github.io/execute_script.html"
    browser.get(link)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    answer = calc(x)

    answer_input = browser.find_element(By.ID, "answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer_input)
    answer_input.send_keys(calc(x))
    robots_rule_radio = browser.find_element(By.ID, "robotsRule")
    robots_rule_radio.click()
    radiobutton = browser.find_element(By.ID, "robotCheckbox")
    radiobutton.click()
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()