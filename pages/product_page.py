from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import Page


class ProductPage(Page):
    ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
    NEW_ARRIVALS = (By.XPATH, "//a[@aria-label='New Arrivals']")
    NEW_ARRIVAL_OPTIONS = (By.XPATH, "//ul[@class='mm-category-list']//h3[text()='Women']")

    def click_add_to_cart(self):
        self.click(*self.ADD_TO_CART_BTN)

    def open_amazon_product(self, product_id):
        self.open_url(product_id)

    def hover_new_arrivals(self):
        new_arrivals = self.find_element(*self.NEW_ARRIVALS)
        actions = ActionChains(self.driver)
        actions.move_to_element(new_arrivals)
        actions.perform()

    def verify_new_arrival_options(self):
        self.wait_for_element_appear(*self.NEW_ARRIVAL_OPTIONS)
