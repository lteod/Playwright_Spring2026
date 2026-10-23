import re
from playwright.sync_api import Page, expect


def test_basic_store_search(page: Page):
    page.goto("https://nop-qa.portnov.com/")

    page.get_by_label("Search store").fill("macbook")
    page.get_by_role("button", name="Search").click()

    expect(page.get_by_role("heading", level=1)).to_have_text("Search")
    (expect(page.get_by_role("heading", level=2)
           .get_by_role("link"))
     .to_contain_text(re.compile("macbook", re.IGNORECASE)))
    # expect(page.get_by_role("heading", level=2).locator("a")).to_contain_text("macbook")
