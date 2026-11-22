from components.category_sidebar import CategorySidebar
from components.product_grid import ProductGrid
from pages.base_page import BasePage
from playwright.sync_api import Page



class CategoryPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.sidebar = CategorySidebar()
        self.product_grid = ProductGrid()

