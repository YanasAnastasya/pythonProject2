from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
"""
Открыть страницу http://suninjuly.github.io/selects1.html
Посчитать сумму заданных чисел
Выбрать в выпадающем списке значение равное расчитанной сумме
Нажать кнопку "Отправить"
"""

browser = webdriver.Chrome()

link = 'http://suninjuly.github.io/selects1.html'
browser.get(link)

num1 = int(browser.find_element(By.ID, "num1").text)
num2 = int(browser.find_element(By.ID, "num2").text)

answer = num1 + num2

select = Select(browser.find_element(By.CLASS_NAME, "custom-select"))
select.select_by_value(str(answer))

button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
button.click()

time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()