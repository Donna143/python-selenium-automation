from selenium.webdriver.common.by import By
from behave import given, when, then


@then('Amazon cart is empty')
def cart_empty(context):
     assert context.driver.find_element(By.XPATH, "//*[contains(text(), 'Your Amazon Cart is empty')]").is_displayed()

