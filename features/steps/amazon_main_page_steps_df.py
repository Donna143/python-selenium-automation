from time import sleep

from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

HAM_MENU = (By.ID, 'nav-hamburger-menu')
FOOTER_LINKS = (By.CSS_SELECTOR, '.navFooterDescItem a')
BEST_SELLERS = (By.CSS_SELECTOR, "[href='/gp/bestsellers/?ref_=nav_cs_bestsellers']")
SIGN_IN = (By.CSS_SELECTOR, '#nav-signin-tooltip .nav-action-button')


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


@when('Click on cart')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, '#nav-cart').click()


@when('Click on button from SignIn popup')
def click_sign_in(context):
    e = context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN), message='Sign in not clickable')
    e.click()


@when('Wait for {sec} sec')
def wait_sec(context, sec):
    sleep(int(sec))


@then('Verify Sign In is clickable')
def verify_sign_in_clickable(context):
    context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN), message='Sign in not clickable')


@then('Verify Sign In disappears')
def verify_sign_in_btn_disappear(context):
    context.driver.wait.until(EC.invisibility_of_element_located(SIGN_IN), message='Sign in is still visible')
    # context.driver.wait.until_not(EC.presence_of_element_located(SIGN_IN), message='Sign in is still visible')


@then('Verify hamburger menu is present')
def verify_ham_menu_present(context):
    context.driver.find_element(*HAM_MENU)


@then('Verify that footer has {expected_link_count} links')
def verify_link_count(context, expected_link_count):
    expected_link_count = int(expected_link_count)
    links = context.driver.find_elements(*FOOTER_LINKS)
    assert len(links) == expected_link_count, f'Expected {expected_link_count} links, but got {len(links)}'


@when('Click on Best Sellers')
def click_best_sellers(context):
    context.driver.find_element(*BEST_SELLERS).click()
