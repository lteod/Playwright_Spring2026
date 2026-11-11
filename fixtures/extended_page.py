from dataclasses import dataclass
from playwright.sync_api import Page as PlaywrightPage

from pages.login_page import LoginPage
from pages.my_account_add_address import AddAddressPage
from pages.my_account_addresses import AddressesPage
from pages.register_page import RegisterPage
from pages.my_account_customer_info_page import CustomerInfo


@dataclass
class MyAccount:
    customer_info_page: CustomerInfo
    addresses_page: AddressesPage
    add_address_page: AddAddressPage


class Page(PlaywrightPage):
    """Typed wrapper around Playwright Page with attached page objects for IDE autocomplete."""

    def __init__(self, page: PlaywrightPage):
        self._page = page
        self.login_page: LoginPage = LoginPage(page)
        self.register_page: RegisterPage = RegisterPage(page)
        self.my_account: MyAccount = MyAccount(
            customer_info_page=CustomerInfo(page),
            addresses_page=AddressesPage(page),
            add_address_page=AddAddressPage(page)
        )

    def __getattr__(self, name: str):
        """Delegate all other attribute access to the underlying Playwright page."""
        return getattr(self._page, name)