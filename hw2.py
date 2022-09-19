from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service(executable_path='./chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
driver = webdriver.Chrome(service=service, options=options)

driver.get('https://www.amazon.com')

driver.find_element(By.ID, 'nav-orders').click()

assert driver.find_element(By.XPATH, "//*[@class='a-spacing-small']").is_displayed()
assert driver.find_element(By.ID, 'ap_email').is_enabled()

print('Test case passed')
driver.quit()

