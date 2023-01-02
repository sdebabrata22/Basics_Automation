import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("E:\Selenium\chromedriver")
driver.get("https://www.way2automation.com/way2auto_jquery/frames-and-windows.php#load_box")
driver.maximize_window()

driver.switch_to.frame(driver.find_element(By.XPATH, "(//iframe[@class='demo-frame'])[1]"))
driver.find_element(By.XPATH, "//a[text()='New Browser Tab']").click()
print(driver.window_handles)
time.sleep(2)
driver.switch_to.window(driver.window_handles[1])
time.sleep(2)

driver.find_element(By.XPATH, "//a[text()='New Browser Tab']").click()
print(driver.window_handles)