# В этом задании после нажатия кнопки страница откроется в новой вкладке,
# нужно переключить WebDriver на новую вкладку и решить в ней задачу.
#
# Сценарий для реализации выглядит так:
#
# Открыть страницу http://suninjuly.github.io/redirect_accept.html
# Нажать на кнопку
# Переключиться на новую вкладку
# Пройти капчу для робота и получить число-ответ
# Если все сделано правильно и достаточно быстро
# (в этой задаче тоже есть ограничение по времени), вы увидите окно с числом.
# Отправьте полученное число в качестве ответа на это задание.


from selenium import webdriver
import time
import math
import pyperclip as pc

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    # запускаем браузер
    browser = webdriver.Chrome()
    browser.get(link)

    # нажимаем на кнопку, чтоы перейти на вторую страницу
    button = browser.find_element_by_tag_name("button")
    button.click()
    time.sleep(0.5)

    # переключаем вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # считываем значение х и вычисляем результат
    x_element = browser.find_element_by_css_selector('[id="input_value"]')
    x = x_element.text
    y = calc(x)

    # вводим ответ в форму
    input1 = browser.find_element_by_css_selector('[id="answer"]')
    input1.send_keys(y)
    time.sleep(0.5)

    # отправляем ответ
    button = browser.find_element_by_tag_name("button")
    button.click()
    time.sleep(0.5)

    # считываем ответ из alert
    alert = browser.switch_to.alert
    ans = alert.text.split(": ")[-1]
    alert.accept()
    time.sleep(1)

    # копируем значение в буфер обмена
    pc.copy(ans)

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
