"""
Base Page Object
Provides common functionality for all page objects.
"""

from playwright.sync_api import Page

import config


class BasePage:
    """
    Base class for all page objects.
    Implements common page interactions and waits.
    """

    def __init__(self, page: Page):
        self.page = page
        self.base_url = config.get_base_url()
        self.path = ""

    @property
    def url(self) -> str:
        """Return full URL for this page."""
        return self.base_url + self.path

    def goto(self) -> "BasePage":
        """Navigate to this page."""
        self.page.goto(self.path)
        return self

    def wait_to_load(self) -> "BasePage":
        """Wait for page to fully load."""
        self.page.wait_for_load_state("networkidle")
        return self