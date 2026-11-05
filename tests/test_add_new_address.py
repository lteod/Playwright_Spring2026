import re
from playwright.sync_api import Page, expect
from fixtures.api_fixtures import api_auth
from utils.helpers import generate_address_data, generate_user_registration_data


def test_add_new_first_address(api_auth: Page):
    user = generate_user_registration_data()
    address = generate_address_data()

    page = api_auth

    page.my_account.addresses.goto()
    page.my_account.addresses.goto_new_address()

    page.my_account.add_address.fill_address_details(
        user.first_name, user.last_name, user.email,
        address.city, address.street, address.zip_code, user.phone)

    page.get_by_role("button", name="Save").click()


    pass


