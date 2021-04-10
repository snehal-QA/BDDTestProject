from selenium import webdriver

driver=webdriver.chrome(excutable_path="/Users/snehabhi/Downloads/chromedriver")
driver.get("https://www.google.com/")
print(driver.title)