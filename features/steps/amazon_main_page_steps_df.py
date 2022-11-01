from time import sleep
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

BEST_SELLERS = (By.CSS_SELECTOR, "[href='/gp/bestsellers/?ref_=nav_cs_bestsellers']")
CART = (By.CSS_SELECTOR, '#nav-cart')
FOOTER_LINKS = (By.CSS_SELECTOR, '.navFooterDescItem a')
HAM_MENU = (By.ID, 'nav-hamburger-menu')
RETURNS = (By.CSS_SELECTOR, '#nav-orders')
SIGN_IN = (By.CSS_SELECTOR, '#nav-signin-tooltip .nav-action-button')


@given('Open Amazon page')
def open_amazon(context):
    # context.driver.get('https://www.amazon.com')
    context.app.main_page.open_main()


@when('Search for {product}')
def search_product(context, product):
    context.app.main_page.search_product(product)


@when('User clicks Returns & Orders')
def click_returns_orders(context):
    context.app.main_page.click_returns()


@when('Click on cart')
def click_cart(context):
    context.app.main_page.click_cart()


@when('Click on button from SignIn popup')
def click_sign_in(context):
    e = context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN), message='Sign in not clickable')
    e.click()


@when('Wait for {sec} sec')
def wait_sec(context, sec):
    sleep(int(sec))


@when('Hover over language options')
def hover_lang(context):
    context.app.main_page.hover_lang()


@when('Select department by value {selection_value}')
def select_department(context, selection_value):
    context.app.main_page.select_department(selection_value)


@when('Click on Best Sellers')
def click_best_sellers(context):
    context.driver.find_element(*BEST_SELLERS).click()


@then('Verify {department} department is selected')
def verify_department(context, department):
    context.app.search_results_page.verify_department(department)


@then('Verify Spanish option present')
def verify_lang(context):
    context.app.main_page.verify_lang()


@then('Verify Sign In is clickable')
def verify_sign_in_clickable(context):
    context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN), message='Sign in not clickable')


@then('Verify Sign In disappears')
def verify_sign_in_btn_disappear(context):
    context.driver.wait.until(EC.invisibility_of_element_located(SIGN_IN), message='Sign in is still visible')


@then('Verify hamburger menu is present')
def verify_ham_menu_present(context):
    context.driver.find_element(*HAM_MENU)


@then('Verify that footer has {expected_link_count} links')
def verify_link_count(context, expected_link_count):
    expected_link_count = int(expected_link_count)
    links = context.driver.find_elements(*FOOTER_LINKS)
    assert len(links) == expected_link_count, f'Expected {expected_link_count} links, but got {len(links)}'



