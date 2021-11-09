from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.headless = True
options.add_argument("--disable-gpu")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
driver = webdriver.Chrome("/usr/bin/chromedriver", options=options)
driver.get("https://google.com/")
print(driver.title)
driver.quit()
