from selenium.webdriver.common.by import By
from behave import given, when, then

CART_COUNT = (By.ID, 'nav-cart-count')


@then('Amazon cart is empty')
def cart_empty(context):
    assert context.driver.find_element(By.XPATH, "//*[contains(text(), 'Your Amazon Cart is empty')]").is_displayed()


@then('Verify cart has {expected_count} item(s)')
def verify_cart_count(context, expected_count):
    actual_count = context.driver.find_element(*CART_COUNT).text
    assert expected_count == actual_count, f'Expected {expected_count}, but got {actual_count}'


