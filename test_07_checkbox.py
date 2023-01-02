from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome("E:\Selenium\chromedriver")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

chkbox = driver.find_elements(By.XPATH,"//input[@type='checkbox']")

for i in chkbox:
    i.click()

print(len(chkbox))
