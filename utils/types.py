from typing import Union
from playwright.sync_api import Page as PlaywrightPage

from conftest import MyAccount
from pages.login_page import LoginPage
from pages.register_page import RegisterPage


class AllPages:
    login_page: LoginPage
    register_page: RegisterPage
    my_account: MyAccount

Page: Union[PlaywrightPage, AllPages]