from selenium import webdriver
import time 



chrome_driver_path = "C:\pydriver\chromedriver"

driver = webdriver.Chrome(chrome_driver_path)
url="https://github.com/"


driver.get(url)
time.sleep(2)
driver.maximize_window()
driver.save_screenshot("github.png")

driver.get(url + "sefaapinar" )
print(driver.title)

driver.back()

driver.close()