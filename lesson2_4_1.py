import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

"""
Открыть страницу http://suninjuly.github.io/redirect_accept.html
Нажать на кнопку
Переключиться на новую вкладку
Пройти капчу для робота и получить число-ответ
"""

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()


    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(calc(x))


    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()