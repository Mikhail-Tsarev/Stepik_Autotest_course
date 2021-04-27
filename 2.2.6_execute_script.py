from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector('[id="input_value"]')
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_css_selector('[id="answer"]')
    input1.send_keys(y)
    time.sleep(0.1)

    button = browser.find_element_by_css_selector("[for='robotCheckbox']")
    button.click()
    time.sleep(0.1)

    button = browser.find_element_by_css_selector("[for='robotsRule']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    time.sleep(0.1)


    button = browser.find_element_by_tag_name("button")

    # Убираем футер
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # Отправляем заполненную форму
    button.click()
    print('Все по плану!')
finally:
    time.sleep(8)
    browser.quit()