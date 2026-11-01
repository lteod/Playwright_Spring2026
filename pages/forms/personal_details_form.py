from playwright.sync_api import Page


class PersonalDetailsForm:
    def __init__(self, page: Page):
        self.radio_female = page.get_by_text("Female")
        self.radio_male = page.get_by_text("Male").first
        self.fld_first_name = page.get_by_label("First name:")
        self.fld_last_name = page.get_by_role("textbox", name="Last name:")
        self.fld_email = page.get_by_role("textbox", name="Email:")

        self.select_birth_day = page.get_by_role('combobox').filter(has_text='Day')
        self.select_birth_month = page.get_by_role('combobox').filter(has_text='Month')
        self.select_birth_year = page.get_by_role('combobox').filter(has_text='Year')