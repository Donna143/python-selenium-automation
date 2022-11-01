from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


@then('Sign in page opens')
def signin_page_opens(context):
    context.app.signin_page.signin_opens()


@then('Verify Sign in page opened')
def verify_sign_in_opened(context):
    context.driver.wait.until(EC.url_contains('ap/signin'), message='SignIn URL did not open')
