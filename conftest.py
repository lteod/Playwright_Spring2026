from dataclasses import dataclass

import pytest
from playwright.sync_api import Page

import config

from fixtures.new_user import get_shopper
from fixtures.menu import menu
from pages.login_page import LoginPage
from pages.my_account_add_address import AddAddressPage
from pages.my_account_addresses import AddressesPage
from pages.my_account_customer_info_page import CustomerInfo
from pages.register_page import RegisterPage
# from utils.types import Page


@pytest.fixture(scope="session")
def browser_type(playwright):
    if config.get_browser_type().lower() == 'brave':
        return playwright.chromium

    return getattr(playwright, config.get_browser_type())

@pytest.fixture(scope="session")
def browser_type_launch_args():
    if config.get_browser_type().lower() == 'brave':
        return {
            **config.get_browser_launch_options(),
            "executable_path": ""
        }

    return config.get_browser_launch_options()

@pytest.fixture(scope="session")
def base_url():
    return config.get_base_url()

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, playwright):
    mobile = config.get_mobile_device_type()
    browser = config.get_browser_type()

    is_device = playwright.devices.get(mobile, None)

    if is_device and not browser == 'firefox':
        return{
            **browser_context_args,
            **is_device
        }

    return {
        **browser_context_args,
        "viewport": {
            "width": config.get_browser_context_options()['viewport']['width'],
            "height": config.get_browser_context_options()['viewport']['height'],
        },
    }

@dataclass
class MyAccount:
    customer_info_page: CustomerInfo
    addresses: AddressesPage
    add_address: AddAddressPage
    # change_password_page: ChangePasswordPage
    # orders_page: ChangePasswordPage


@pytest.fixture(scope="function")
def page(page: Page):
    page.login_page = LoginPage(page)
    page.register_page = RegisterPage(page)
    # page.customer_info_page = CustomerInfo(page)

    page.my_account = MyAccount(
        CustomerInfo(page),
        AddressesPage(page),
        AddAddressPage(page)
        # OrdersPAge(page),
        # ChangePasswordPage(page)
    )

    return page
