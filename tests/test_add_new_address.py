from playwright.sync_api import expect
from fixtures.extended_page import Page
from fixtures.api_fixtures import api_auth
from utils.helpers import generate_address_data, generate_user_registration_data


def test_add_new_first_address(api_auth: Page):
    user = generate_user_registration_data()
    address = generate_address_data()

    page = api_auth

    page.my_account.addresses_page.goto()
    page.my_account.addresses_page.wait_to_load()

    page.my_account.addresses_page.goto_add_new()

    page.my_account.add_address_page.fill_address_details(
        user.first_name, user.last_name, user.email, address.country, address.state,
        address.city, address.street, address.zipcode, user.phone)

    expect(page.my_account.addresses_page.li_email.last).to_contain_text(f"Email: {user.email}")
    expect(page.my_account.addresses_page.li_phone_number.last).to_contain_text(f"Phone number: {user.phone}")
    expect(page.my_account.addresses_page.li_city_state_zip.last).to_contain_text(
        f"{address.city}, {address.state}, {address.zipcode}")
    expect(page.my_account.addresses_page.li_name.last).to_contain_text(f"{user.first_name} {user.last_name}")
