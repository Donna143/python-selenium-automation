from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com')


@when('Search for {product}')
def search_product(context, product):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys(product)
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()


@when('User clicks Returns & Orders')
def click_returns_orders(context):
    context.driver.find_element(By.CSS_SELECTOR, '#nav-orders').click()


@when('User clicks cart')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, '#nav-cart').click()
    