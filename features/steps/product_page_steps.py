from selenium.webdriver.common.by import By
from behave import given, when, then

ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')


@when('Click Add to Cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()
