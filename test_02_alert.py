from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome("E:\Selenium\chromedriver")
driver.get("https://www.way2automation.com/way2auto_jquery/alert.php#load_box")
driver.maximize_window()

driver.switch_to.frame(driver.find_element(By.XPATH, "(//iframe[@class='demo-frame'])[1]"))
driver.find_element(By.XPATH, "//button[text()='Click the button to display an alert box:']").click()
time.sleep(2)
driver.switch_to.alert.accept()

time.sleep(2)
driver.close()