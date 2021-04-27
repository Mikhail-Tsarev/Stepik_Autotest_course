# Попробуем теперь написать программу, которая будет бронировать нам дом для отдыха
# по строго заданной цене. Более высокая цена нас не устраивает, а по более низкой
# цене объект успеет забронировать кто-то другой.
#
# В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:
#
# Открыть страницу http://suninjuly.github.io/explicit_wait2.html
# Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
# Нажать на кнопку "Book"
# Решить уже известную нам математическую задачу (используйте ранее написанный код)
# и отправить решение

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import pyperclip as pc

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    # запускаем браузер
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
                                    )
    button = browser.find_element_by_id("book")
    button.click()

    # считываем значение х и вычисляем результат
    x_element = browser.find_element_by_css_selector('[id="input_value"]')
    x = x_element.text
    y = calc(x)

    # вводим ответ в форму
    input1 = browser.find_element_by_css_selector('[id="answer"]')
    input1.send_keys(y)

    # отправляем ответ
    button = browser.find_element_by_css_selector('[id="solve"]')
    button.click()

    # считываем ответ из alert
    alert = browser.switch_to.alert
    ans = alert.text.split(": ")[-1]
    time.sleep(1)
    alert.accept()

    # копируем значение в буфер обмена
    pc.copy(ans)

finally:
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()