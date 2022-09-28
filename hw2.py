from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service(executable_path='./chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()

driver.get('https://www.amazon.com')
# driver.refresh()

driver.find_element(By.ID, 'nav-orders').click()

assert driver.find_element(By.XPATH, "//*[@class='a-spacing-small']").is_displayed()
assert driver.find_element(By.ID, 'ap_email').is_enabled()

# expected_text = 'Sign in'
# actual_text = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
# assert actual_text == expected_text, f'Expected {expected_text} but got {actual_text}'
# assert driver.find_element(By.ID, 'ap_email'), 'Email field not shown'

print('Test case passed')
driver.quit()

