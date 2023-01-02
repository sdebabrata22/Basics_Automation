from selenium import webdriver

driver = webdriver.Chrome("E:\Selenium\chromedriver")
driver.get("https://www.google.com/")    #to call a page
driver.maximize_window()        #to maximize the window
print(driver.title)             #to print tittle of page
print(driver.current_url)       #to print url of page
print(driver.page_source)       #to print html code of this page

#driver.quit()             #to close the open driver
#driver.close()           #to close the browser

