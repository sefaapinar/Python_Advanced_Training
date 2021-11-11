from selenium import webdriver


chrome_driver_path = "C:\pydriver\chromedriver"

driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://www.trendyol.com/mavi/mont-kurk-yakali-010211-900-p-31435670?boutiqueId=587368&merchantId=63")

title = driver.find_element_by_class_name("pr-new-br").text
price = driver.find_element_by_class_name("product-price-container").find_element_by_class_name("pr-bx-w").text


print(title)
print(price)



driver.close()