from selenium.webdriver.common.by import By
from pages.base_page import Page


class SigninPage(Page):
    EMAIL_FIELD = (By.ID, 'ap_email')
    SIGNIN_TEXT = (By.XPATH, "//h1[@class='a-spacing-small']")

    def signin_opens(self):
        self.verify_element_text('Sign in', self.SIGNIN_TEXT)
        assert self.driver.find_element(*self.EMAIL_FIELD), 'Email field not shown'
