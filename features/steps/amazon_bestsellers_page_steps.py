from selenium.webdriver.common.by import By
from behave import given, when, then

HEADER_LINKS = (By.CSS_SELECTOR, '#zg_header a')
HEADER_TEXT = (By.ID, 'zg_banner_text')


@then('Verify that header has {expected_link_count} links')
def verify_link_count(context, expected_link_count):
    expected_link_count = int(expected_link_count)
    links = context.driver.find_elements(*HEADER_LINKS)
    assert len(links) == expected_link_count, f'Expected {expected_link_count} links, but got {len(links)}'


@then('Click each header link and verify correct page opens')
def click_header_link_opens_correct_page(context):
    links = context.driver.find_elements(*HEADER_LINKS)
    print(links)
    for link in links:
        print(link)
        link.click()
        assert link.text in context.driver.find_element(*HEADER_TEXT).text





