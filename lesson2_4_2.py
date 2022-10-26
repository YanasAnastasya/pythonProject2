from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions


"""Задание: ждем нужный текст на странице
Открыть страницу http://suninjuly.github.io/explicit_wait2.html
Дождаться, когда цена дома уменьшится до 100 (ожидание нужно установить не меньше 12 секунд)
Нажать на кнопку "Забронировать"
Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
Чтобы определить момент, когда стоимость дома уменьшится до 10000 RUR, используйте метод text_to_be_present_in_element
 из библиотеки expected_conditions.
"""


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    WebDriverWait(browser, 12).until(
        expected_conditions.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    browser.find_element(By.CSS_SELECTOR, 'button[id="book"]').click()


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


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