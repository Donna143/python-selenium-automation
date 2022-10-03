from selenium.webdriver.common.by import By
from behave import given, when, then

HEADER_LINKS = (By.XPATH, "//div[contains(@class,'_p13n-zg-nav-tab-all_style_zg-tabs-li-')]")


@then('Verify that header has {expected_link_count} links')
def verify_link_count(context, expected_link_count):
    expected_link_count = int(expected_link_count)
    links = context.driver.find_elements(*HEADER_LINKS)
    assert len(links) == expected_link_count, f'Expected {expected_link_count} links, but got {len(links)}'