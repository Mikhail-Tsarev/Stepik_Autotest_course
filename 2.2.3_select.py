from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x1_element = browser.find_element_by_id("num1")
    x1 = x1_element.text
    x2_element = browser.find_element_by_id("num2")
    x2 = x2_element.text
    s = str(int(x1) + int(x2))

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(s)

    # Отправляем заполненную форму
    button = browser.find_element_by_xpath('//button[@type="submit"]')
    button.click()

finally:
    time.sleep(8)
    browser.quit()
