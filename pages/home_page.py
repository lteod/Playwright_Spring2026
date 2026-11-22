from playwright.sync_api import Page

from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.welcome_message = page.get_by_role("heading", name="Welcome to our store")
        self.featured_products = page.locator('.product-item')
        self.news = page.locator('.news-item')
        self.header_menu = page.locator(".header-menu")

    def category(self, category_name):
        return self.header_menu.get_by_role("link", name=category_name, exact=True)

    def select_category(self, category_name):
        self.category(category_name).click()


    def open_first_featured_product(self):
        self.featured_products.first.click()
        self.page.wait_for_load_state("networkidle")

    def open_first_news(self):
        self.news.first.click()
        self.page.wait_for_load_state("networkidle")