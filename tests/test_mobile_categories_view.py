import pytest
from playwright.sync_api import Page, expect

import config


@pytest.mark.mobile
def test_categories_on_mobile(page: Page):
    page.goto("/")
    header_menu = page.locator(".header-menu")

    if config.get_mobile_device_type():
        page.locator('.menu-toggle', has_text='Categories').click()

    expect(header_menu.get_by_role('link', name = 'Computers')).to_be_visible()
    expect(header_menu.get_by_role('link', name='Electronics')).to_be_visible()
    expect(header_menu.get_by_role('link', name='Apparel')).to_be_visible()
    expect(header_menu.get_by_role('link', name='Digital downloads')).to_be_visible()
    expect(header_menu.get_by_role('link', name='Books')).to_be_visible()
    expect(header_menu.get_by_role('link', name='Jewelry')).to_be_visible()
    expect(header_menu.get_by_role('link', name='Gift Cards')).to_be_visible()

    header_menu.get_by_role('link', name='Computers').click()
    expect(page.get_by_role('heading', level=1)).to_have_text('Computers')

def test_categories_on_desktop(page: Page):
    page.goto("/")
    header_menu = page.locator(".header-menu")

    if config.get_mobile_device_type():
        page.locator('.menu-toggle', has_text='Categories').click()

    expect(header_menu.get_by_role('link', name = 'Computers')).to_be_visible()
    expect(header_menu.get_by_role('link', name='Electronics')).to_be_visible()
    expect(header_menu.get_by_role('link', name='Apparel')).to_be_visible()
    expect(header_menu.get_by_role('link', name='Digital downloads')).to_be_visible()
    expect(header_menu.get_by_role('link', name='Books')).to_be_visible()
    expect(header_menu.get_by_role('link', name='Jewelry')).to_be_visible()
    expect(header_menu.get_by_role('link', name='Gift Cards')).to_be_visible()

    header_menu.get_by_role('link', name='Computers').click()
    expect(page.get_by_role('heading', level=1)).to_have_text('Computers')
