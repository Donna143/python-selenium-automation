from selenium.webdriver.common.by import By
from behave import given, when, then

PRODUCT_PRICE = (By.CSS_SELECTOR, '.a-spacing-top-small .a-price')
SEARCH_RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")


@then('Search results for {expected_result} are shown')
def verify_search_results(context, expected_result):
    actual_result = context.driver.find_element(*SEARCH_RESULT).text
    assert expected_result == actual_result, f'Error! Expected {expected_result}, but got {actual_result}'


@when('Click on first product')
def click_first_product(context):
    context.driver.find_element(*PRODUCT_PRICE).click()