from selenium.webdriver.common.by import By
from behave import given, when, then

CATEGORY_TILES = (By.CSS_SELECTOR, ".issue-card-container")
CUSTOMER_SERVICE = (By.XPATH, "//a[@href='/gp/help/customer/display.html?nodeId=508510&ref_=nav_cs_customerservice']")
RECOMMENDED_TOPICS = (By.XPATH, "//*[@class='help-topics-list-wrapper']")
SEARCH_FIELD = (By.ID, "hubHelpSearchInput")
SEARCH_HEADER = (By.XPATH, "//h2[text()='Search our help library']")
TOPICS_HEADER = (By.XPATH, "//h2[text()='All help topics']")
WELCOME_HEADER = (By.XPATH, "//h1[text()='Welcome to Amazon Customer Service']")


@when('Click on Customer Service')
def click_customer_service(context):
    context.driver.find_element(*CUSTOMER_SERVICE).click()


@then('Verify UI elements present')
def ui_elements_present(context):
    context.driver.find_element(*WELCOME_HEADER)
    context.driver.find_element(*CATEGORY_TILES)
    context.driver.find_element(*SEARCH_HEADER)
    context.driver.find_element(*SEARCH_FIELD)
    context.driver.find_element(*TOPICS_HEADER)
    context.driver.find_element(*RECOMMENDED_TOPICS)


