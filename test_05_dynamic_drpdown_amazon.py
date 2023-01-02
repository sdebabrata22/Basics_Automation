import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("E:\Selenium\chromedriver")
driver.get("https://www.amazon.in/")
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@type='text']").send_keys("a")
time.sleep(10)
item = driver.find_elements(By.XPATH, "//div[@class='s-suggestion-container']")
time.sleep(2)

for i in item:
   print(i.text)
for i in item:
    if i .text == "airpods pro":
        i.click()
    else:
        pass