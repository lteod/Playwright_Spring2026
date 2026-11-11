from playwright.sync_api import Page

from pages.base_page import BasePage


class AddAddressPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.path = "/customer/addressadd"

        self.fld_first_name = page.get_by_label("First name:")
        self.fld_last_name = page.get_by_label("Last name:")
        self.fld_email = page.get_by_label("Email:")
        self.fld_city = page.get_by_label("City")
        self.fld_street = page.get_by_label("Address 1:")
        self.fld_zipcode = page.get_by_label("Zip / postal code:")
        self.fld_phone_number = page.get_by_label("Phone number:")
        self.btn_save = page.get_by_role("button", name="Save")

    def fill_address_details(self, first_name, last_name, email, country, state, city, street, zipcode, phone_number):
        self.page.wait_for_load_state("load")
        self.fld_first_name.fill(first_name)
        self.fld_last_name.fill(last_name)
        self.fld_email.fill(email)
        self.page.get_by_label('Country:').select_option(country)
        self.page.get_by_label("State / province:").select_option(state)
        self.fld_city.fill(city)
        self.fld_street.fill(street)
        self.fld_zipcode.fill(zipcode)
        self.fld_phone_number.fill(phone_number)

        self.btn_save.click()