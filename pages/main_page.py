from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from pages.base_page import Page


class MainPage(Page):
    CART = (By.CSS_SELECTOR, '#nav-cart')
    DEPARTMENT_SELECTION = (By.ID, 'searchDropdownBox')
    LANG_SELECTION = (By.CSS_SELECTOR, ".icp-nav-flag-us")
    RETURNS = (By.CSS_SELECTOR, '#nav-orders')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SPANISH_LANG = (By.CSS_SELECTOR, '#nav-flyout-icp [href="#switch-lang=es_US"]')

    def open_main(self):
        self.open_url()

    def search_product(self, product):
        self.input_text(product, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_BTN)

    def click_returns(self):
        self.click(*self.RETURNS)

    def click_cart(self):
        self.click(*self.CART)

    def hover_lang(self):
        language_selection = self.find_element(*self.LANG_SELECTION)
        actions = ActionChains(self.driver)
        actions.move_to_element(language_selection)
        actions.perform()

    def select_department(self, selection_value):
        select = Select(self.find_element(*self.DEPARTMENT_SELECTION))
        select.select_by_value(f'search-alias={selection_value}')

    def verify_lang(self):
        self.wait_for_element_appear(*self.SPANISH_LANG)


