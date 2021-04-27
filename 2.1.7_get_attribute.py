from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    print('Все по плану!')

    input1 = browser.find_element_by_css_selector('[id="answer"]')
    input1.send_keys(y)
    time.sleep(0.1)

    button = browser.find_element_by_css_selector("[id='robotCheckbox']")
    button.click()
    time.sleep(0.1)

    button = browser.find_element_by_css_selector("[id='robotsRule']")
    button.click()
    time.sleep(0.1)

    # Отправляем заполненную форму
    button = browser.find_element_by_xpath('//button[@type="submit"]')
    button.click()
    print('Все по плану!')
finally:
    time.sleep(8)
    browser.quit()
