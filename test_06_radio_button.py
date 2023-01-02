import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("E:\Selenium\chromedriver")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@value='radio1']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@value='radio2']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@value='radio3']").click()
time.sleep(2)
