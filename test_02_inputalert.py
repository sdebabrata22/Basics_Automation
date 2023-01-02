from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome("E:\Selenium\chromedriver")
driver.get("https://www.way2automation.com/way2auto_jquery/alert.php#load_box")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.XPATH, "//a[text()='Input Alert']").click()
driver.switch_to.frame(driver.find_element(By.XPATH, "(//iframe[@class='demo-frame'])[2]"))
driver.find_element(By.XPATH, "//button[text()='Click the button to demonstrate the Input box.']").click()
time.sleep(2)
driver.switch_to.alert.send_keys("dev")
time.sleep(2)
driver.switch_to.alert.accept()
#driver.switch_to.alert.dismiss()