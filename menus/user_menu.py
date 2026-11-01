from playwright.sync_api import Page

class UserMenu():
    def __init__(self, page: Page):
        self.page = page

        self.link_register = page.get_by_role("link", name="Register")
        self.link_wishlist = page.get_by_role("link", name="Wishlist (0)")
        self.link_shopping_cart = page.get_by_role("link", name="Shopping cart (0)")
        self.link_login = page.get_by_role("link", name="Log in")
        self.fld_search_store = page.get_by_role("textbox", name="Search store")
        self.btn_search = page.get_by_role("button", name="Search")
        self.link_my_account = page.get_by_role("link", name="My account").first
        self.link_logout = page.get_by_role("link", name="Log out")


    def goto_login(self):
        self.link_login.click()
        self.page.wait_for_load_state("networkidle")

    def goto_register(self):
        self.link_register.click()
        self.page.wait_for_load_state("networkidle")

    def goto_logout(self):
        self.link_logout.click()
        self.page.wait_for_load_state("networkidle")

    def goto_my_account(self):
        self.link_my_account.click()
        self.page.wait_for_load_state("networkidle")

    # def goto_wishlist(self):
    #     self.link_wishlist.click()
    #     self.page.wait_for_load_state("networkidle")