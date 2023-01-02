import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome("E:\Selenium\chromedriver")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

option = Select(driver.find_element(By.ID, "dropdown-class-example"))
option.select_by_visible_text("Option2")
time.sleep(2)
option.select_by_visible_text("Option3")



