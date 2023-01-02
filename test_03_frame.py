from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome("E:\Selenium\chromedriver")
driver.get("https://www.way2automation.com/way2auto_jquery/frames-and-windows.php#load_box")
driver.maximize_window()

driver.find_element(By.XPATH, "//a[text()='Frameset']" ).click()

#then we have to find full xpath of this frame to enter into this frame set
driver.switch_to.frame(driver.find_element(By.XPATH, "(//iframe[@class='demo-frame'])[3]"))
driver.find_element(By.XPATH, "//a[text()='Open Frameset Window']").click()
