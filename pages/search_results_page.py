from pages.base_page import Page
from selenium.webdriver.common.by import By


class SearchResultsPage(Page):
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.a-spacing-top-small .a-price')
    SEARCH_RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
    SELECTED_DEPARTMENT = (By.CSS_SELECTOR, '#nav-subnav[data-category="{DEPARTMENT}"]')

    def get_department_locator(self, department: str):
        return [self.SELECTED_DEPARTMENT[0], self.SELECTED_DEPARTMENT[1].replace('{DEPARTMENT}', department)]

    def verify_search_results(self, expected_result):
        self.verify_element_text(expected_result, *self.SEARCH_RESULT)

    def click_first_product(self):
        self.click(*self.PRODUCT_PRICE)

    def verify_department(self, department):
        department_locator = self.get_department_locator(department)
        self.wait_for_element_appear(*department_locator)
