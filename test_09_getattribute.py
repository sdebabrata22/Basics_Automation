
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("E:\Selenium\chromedriver")
driver.get("https://www.facebook.com/")
driver.maximize_window()

name = driver.find_element(By.XPATH, "//img[@alt='Facebook']").get_attribute("alt")

print(name)


driver.close()