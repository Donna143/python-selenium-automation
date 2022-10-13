from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


@then('Sign in page opens')
def signin_page_opens(context):
    expected_text = 'Sign in'
    actual_text = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
    assert actual_text == expected_text, f'Expected {expected_text} but got {actual_text}'
    assert context.driver.find_element(By.ID, 'ap_email'), 'Email field not shown'


@then('Verify Sign in page opened')
def verify_sign_in_opened(context):
    context.driver.wait.until(EC.url_contains('ap/signin'), message='SignIn URL did not open')
