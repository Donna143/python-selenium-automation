from selenium.webdriver.common.by import By
from behave import given, when, then

PRODUCT_PRICE = (By.CSS_SELECTOR, '.a-spacing-top-small .a-price')
SEARCH_RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
SEARCH_RESULTS = (By.CSS_SELECTOR, "[data-component-type='s-search-result']")
PRODUCT_TITLE = (By.CSS_SELECTOR, 'h2 span.a-text-normal')
PRODUCT_IMG = (By.CSS_SELECTOR, ".s-image[data-image-latency='s-product-image']")


@then('Search results for {expected_result} are shown')
def verify_search_results(context, expected_result):
    actual_result = context.driver.find_element(*SEARCH_RESULT).text
    assert expected_result == actual_result, f'Error! Expected {expected_result}, but got {actual_result}'


@when('Click on first product')
def click_first_product(context):
    context.driver.find_element(*PRODUCT_PRICE).click()


@then('Verify that every product has a name and an image')
def verify_products_name_img(context):
    all_products = context.driver.find_elements(*SEARCH_RESULTS)
    for product in all_products:
        title = product.find_element(*PRODUCT_TITLE).text
        assert title, 'Error! Title should not be blank'
        product.find_element(*PRODUCT_IMG)
        # assert product.find_element(*PRODUCT_IMG).is_displayed(), 'Img is not found'

