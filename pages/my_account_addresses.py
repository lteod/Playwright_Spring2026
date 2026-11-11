from playwright.sync_api import Page

from pages.base_page import BasePage


class AddressesPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.path = "customer/addresses"

        self.li_name = page.locator(".info .name")
        self.li_email = page.locator(".email")
        self.li_city_state_zip = page.locator(".city-state-zip")
        self.li_phone_number = page.locator(".phone")

        self.btn_add_new = page.get_by_role("button", name="Add new")

    def goto_add_new(self):
        self.btn_add_new.click()
