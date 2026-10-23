from playwright.sync_api import Page, expect


def test_change_password_successfully(page: Page, get_shopper):
    page.goto("https://nop-qa.portnov.com/")


    user_email = get_shopper[0]
    user_pswd = get_shopper[1]

    page.goto('/login')
    page.get_by_label("Email:").fill(user_email)
    page.get_by_label("Password:").fill(user_pswd)
    page.get_by_role("button", name="Log in").click()

    page.locator('.header-links .ico-account').click()
    page.get_by_role("link", name="Change password").click()

    page.get_by_label("Old password").fill(user_pswd)
    page.get_by_label("New password").fill('123Pass')
    page.get_by_label("Confirm password").fill('123Pass')
    page.get_by_role("button", name="Change password").click()

    expect(page.get_by_text('Password was changed')).to_be_visible()
    expect(page.locator('#bar-notification').get_by_text('Password was changed')).to_be_visible()

    page.get_by_title("Close").click()

    page.get_by_role("link", name = "Log out").click()
    expect(page.get_by_role("link", name = "Log in")).to_be_visible()

    page.get_by_role("link", name="Log in").click()
    page.get_by_label("Email:").fill(user_email)
    page.get_by_label("Password:").fill('123Pass')
    page.get_by_role("button", name="Log in").click()

    expect(page.get_by_role("link", name = "My account").first).to_be_visible()
    expect(page.get_by_role("link", name = "Log out").first).to_be_visible()