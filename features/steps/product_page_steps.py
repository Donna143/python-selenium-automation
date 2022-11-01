from selenium.webdriver.common.by import By
from behave import given, when, then

ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
COLOR_OPTIONS = (By.CSS_SELECTOR, '#variation_color_name li')
CURRENT_COLOR = (By.CSS_SELECTOR, '#variation_color_name .selection')
PRODUCT_NAME = (By.ID, 'productTitle')


@given('Open Amazon product {product_id} page')
def open_amazon_product(context, product_id):
    context.app.product_page.open_amazon_product(f'dp/{product_id}/')


@when('Hover over New Arrivals')
def hover_new_arrivals(context):
    context.app.product_page.hover_new_arrivals()


@when('Click Add to Cart button')
def click_add_to_cart(context):
    # context.driver.find_element(*ADD_TO_CART_BTN).click()
    context.app.product_page.click_add_to_cart()


@then('Verify user sees New Arrival options')
def verify_new_arrival_options(context):
    context.app.product_page.verify_new_arrival_options()


@then('Verify user can click through colors')
def verify_can_click_colors(context):
    expected_colors = ['Army Green', 'Black', 'Blue', 'Brown', 'Burgundy', 'Caramel', 'Dark Blue', 'Denim Blue', 'Gray', 'Green']
    actual_colors = []
    colors = context.driver.find_elements(*COLOR_OPTIONS)
    for color in colors[:10]:
        color.click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text
        actual_colors += [current_color]

    assert expected_colors == actual_colors, \
        f'Expected colors {expected_colors} did not match actual {actual_colors}'
