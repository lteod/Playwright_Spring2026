from playwright.async_api import Page

from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.path = "/login"

        self.fld_email = page.get_by_label("Email:")
        self.fld_password = page.get_by_label("Password:")
        self.btn_login = page.get_by_label("Login:")

    def authenticate(self, email, password):
        self.fld_email.fill(email)
        self.fld_password.fill(password)
        self.btn_login.click()