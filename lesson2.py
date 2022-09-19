from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# driver = webdriver.Chrome(executable_path='C:/Users/thebe/Documents/Careerist/Automation/python-selenium-automation/chromedriver.exe')
service = Service(executable_path='./chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
driver = webdriver.Chrome(service=service, options=options)

driver.get('https://www.amazon.com')

driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('coffee')

driver.find_element(By.ID, 'nav-search-submit-button').click()

expected_result = '"coffee"'
actual_result = driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
assert expected_result == actual_result, f'Error! Expected {expected_result}, but got {actual_result}'

print('Test case passed')
driver.quit()

