import pytest
from utils.helpers import generate_user_registration_data
from playwright.sync_api import Page
from playwright.sync_api import expect

@pytest.fixture
def get_shopper(page: Page):
    user = generate_user_registration_data()

    page.goto("/register")

    page.get_by_label("First name:").fill(user.first_name)
    page.get_by_role("textbox", name="Last name:").fill(user.last_name)
    page.get_by_role("textbox", name="Email:").fill(user.email)
    page.get_by_role("checkbox", name="Newsletter").uncheck()
    page.get_by_role("textbox", name="Password:", exact=True).fill(user.password)
    page.get_by_role("textbox", name="Confirm password:").fill(user.password)

    page.get_by_role("button", name="Register").click()

    expect(page).not_to_have_url('/registerresult')

    return user.email, user.password