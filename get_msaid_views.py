from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://github.com/Msaid1013")
if __name__ == "__main__":
    while True:
        driver.refresh()
