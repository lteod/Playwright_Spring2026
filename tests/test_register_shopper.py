import pytest

from fixtures.menu import Menu
from pages.my_account_customer_info_page import CustomerInfo
from pages.register_page import RegisterPage
from utils.helpers import generate_user_registration_data
from playwright.sync_api import Page, expect
from playwright.sync_api import Playwright, sync_playwright, expect



def test_register_shopper(page: Page, menu: Menu):
    user = generate_user_registration_data()

    page.goto("/")
    menu.user_menu.goto_register()

    register_page = RegisterPage(page)
    register_page.fill_registration_details(user.first_name, user.last_name, user.email, user.password,
                                            gender = 'female', newsletter=False, company=user.company,
                                            birth_date=user.birth_date)
    expect(page.get_by_text("Your registration completed")).to_be_visible()
    expect(page.locator(".registration-result-page .result")).to_contain_text("Your registration completed")
    expect(page.get_by_role("link", name="Continue")).to_be_visible()


    menu.user_menu.goto_my_account()

    customer_info_page = CustomerInfo(page)

    expect(page.my_account.customer_info_page.fld_first_name).to_have_value(user.first_name)

    expect(customer_info_page.fld_first_name).to_have_value(user.first_name)
    expect(customer_info_page.fld_last_name).to_have_value(user.last_name)
    expect(customer_info_page.select_birth_day).to_have_value(str(user.birth_date.day))
    expect(customer_info_page.select_birth_month).to_have_value(str(user.birth_date.month))
    expect(customer_info_page.select_birth_year).to_have_value(str(user.birth_date.year))
    expect(customer_info_page.fld_email).to_have_value(user.email)
    expect(customer_info_page.fld_company).to_have_value(user.company)
    expect(customer_info_page.chk_newsletter).not_to_be_checked()

# def test_user_registration_fails_with_mismatched_password():
#     pass
#
# @pytest.mark.parametrize()
# def test_user_registration_fails_with_missing_required_fields():
#     pass