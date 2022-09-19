from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='C:/Users/thebe/Documents/Careerist/Automation/python-selenium-automation/chromedriver.exe')

# by XPATH
driver.find_element(By.XPATH, "//a[@href='/ref=nav_logo']")
driver.find_element(By.XPATH, "//a[@class='nav-logo-link nav-progressive-attribute']")

# by tag only
driver.find_element(By.XPATH, "//input")

# by attribute only
driver.find_element(By.XPATH, "//*[@href='/ref=nav_logo']")
driver.find_element(By.XPATH, "//*[@class='nav-logo-link nav-progressive-attribute']")

# by text
driver.find_element(By.XPATH, "//a[text()='Back to School']")
# by multiple attributes
driver.find_element(By.XPATH, "//a[@class='nav-a   ' and @href='/backtoschool?ref_cs_bts']")
# by multiple attributes and text
driver.find_element(By.XPATH, "//a[@class='nav-a   ' and @href='/backtoschool?ref_cs_bts' and text()='Back to School']")

# by partial text / attribute => contains
driver.find_element(By.XPATH, "//a[contains(text(), 'Back to')]")

# by multiple nodes
driver.find_element(By.XPATH, "//div[@id='nav-xshop-container']//a[contains(@href, 'new-releases')]")