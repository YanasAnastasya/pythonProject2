from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    treasure=browser.find_element(By.ID, "treasure")
    x = treasure.get_attribute('valuex')


    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(calc(x))
    robots_rule_radio = browser.find_element(By.ID, "robotsRule")
    robots_rule_radio.click()
    radiobutton = browser.find_element(By.ID, "robotCheckbox")
    radiobutton.click()
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()