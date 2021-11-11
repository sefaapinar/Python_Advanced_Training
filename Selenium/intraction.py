from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


chrome_driver_path = "C:\pydriver\chromedriver"

driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://tr.wikipedia.org/wiki/Anasayfa")

articleCountBtn = driver.find_elements_by_css_selector("#articlecount a")[1].get_attribute("href")
tumPortallar = driver.find_element_by_link_text("Tüm portallar")

#tumPortallar.click()

# searchInput = driver.find_element_by_name("search")
# searchInput.send_keys("Python")

# # articleCountBtn.click()
# # time.sleep(1)
# searchInput.send_keys(Keys.ENTER)
login = driver.find_element_by_css_selector("#pt-login a ")
login.click()

time.sleep(1)

username = driver.find_element_by_id("wpName1")
username.send_keys("sefaapinar")


password = driver.find_element_by_id("wpPassword1")
password.send_keys("1234")

remember = driver.find_element_by_id("wpRemember")
remember.click()

btn = driver.find_element_by_id("wpLoginAttempt")

btn.click()






driver.close()
   