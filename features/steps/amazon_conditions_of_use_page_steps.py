from time import sleep

from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


PRIVACY_NOTICE = (By.CSS_SELECTOR, "a[href='https://www.amazon.com/privacy']")


@given('Open Amazon T&C page')
def open_conditions_of_use(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')


@when('Store original windows')
def store_windows(context):
    context.original_window = context.driver.current_window_handle
    print('Original: ', context.original_window)


@when('Click on Amazon Privacy Notice link')
def click_privacy_notice(context):
    context.driver.find_element(*PRIVACY_NOTICE).click()


@when('Switch to the newly opened window')
def switch_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    current_windows = context.driver.window_handles
    print('Current windows: ', current_windows)
    context.driver.switch_to.window(current_windows[1])


@then('Verify Amazon Privacy Notice page is opened')
def verify_privacy_notice_opened(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/help/customer/display.html'))


@then('User can close new window and switch back to original')
def close_window_and_switch_back(context):
    context.driver.close()
    context.driver.switch_to.window(context.original_window)

