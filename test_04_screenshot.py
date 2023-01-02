import time

from selenium import webdriver



driver = webdriver.Chrome("E:\Selenium\chromedriver")
driver.get("https://www.w3schools.com/html/default.asp")
driver.maximize_window()

driver.get_screenshot_as_file("D:/test_04.jpg")
time.sleep(2)

driver.close()