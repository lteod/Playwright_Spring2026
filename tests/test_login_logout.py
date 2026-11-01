import re
from playwright.sync_api import Page, expect

def test_valid_login_and_logout(page: Page, menu):
    page.goto("/")
    menu.user_menu.goto_login()
    page.get_by_label("Email:").fill("user.shopper@yopmail.com")
    page.get_by_label("Password:").fill("user9900")
    page.get_by_role("button", name="Log in").click()

    expect(menu.user_menu.link_my_account).to_be_visible()
    expect(menu.user_menu.link_logout).to_be_visible()


    menu.user_menu.goto_logout()
    expect(menu.user_menu.link_login).to_be_visible()
    expect(page.locator(".ico-account", has_text="My account")).to_have_count(0)



    # Expect a title "to contain" a substring.
    # expect(page).to_have_title(re.compile("Playwright"))
