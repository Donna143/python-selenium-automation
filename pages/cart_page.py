from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):
    CART_COUNT = (By.ID, 'nav-cart-count')
    EMPTY_CART = (By.XPATH, "//*[contains(text(), 'Your Amazon Cart is empty')]")

    def cart_empty(self):
        assert self.driver.find_element(*self.EMPTY_CART).is_displayed()

    def verify_cart_count(self, expected_count):
        actual_count = self.driver.find_element(*self.CART_COUNT).text
        assert expected_count == actual_count, f'Expected {expected_count}, but got {actual_count}'
