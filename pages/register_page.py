from datetime import datetime

from playwright.async_api import Page

from pages.base_page import BasePage
from pages.forms.personal_details_form import PersonalDetailsForm


class RegisterPage(BasePage, PersonalDetailsForm):
    def __init__(self, page: Page):
        super().__init__(page)
        PersonalDetailsForm.__init__(self, page)
        self.path = "/register"

        # self.radio_female = page.get_by_text("Female")
        # self.radio_male = page.get_by_text("Male").first
        # self.fld_first_name = page.get_by_label("First name:")
        # self.fld_last_name = page.get_by_role("textbox", name="Last name:")
        # self.fld_email = page.get_by_role("textbox", name="Email:")
        #
        # self.select_birth_day = page.get_by_role('combobox').filter(has_text='Day')
        # self.select_birth_month = page.get_by_role('combobox').filter(has_text='Month')
        # self.select_birth_year = page.get_by_role('combobox').filter(has_text='Year')

        self.fld_company = page.get_by_role("textbox", name="Company name:")
        self.chk_newsletter = page.get_by_role("checkbox", name="Newsletter")
        self.fld_password = page.get_by_role("textbox", name="Password:", exact=True)
        self.fld_confirm_password = page.get_by_role("textbox", name="Confirm password:")
        self.btn_register = page.get_by_role("button", name="Register")


    def fill_registration_details(self, first_name, last_name, email, password,
                                  gender=None, birth_date: datetime.date=None,
                                  company=None, newsletter=True, re_password=None):
        if gender.lower() == 'female':
            self.radio_female.click()
        else:
            self.radio_male.click()

        self.fld_first_name.fill(first_name)
        self.fld_last_name.fill(last_name)

        if birth_date:
            self.select_birth_day.select_option(str(birth_date.day))
            self.select_birth_month.select_option(str(birth_date.month))
            self.select_birth_year.select_option(str(birth_date.year))

        self.fld_email.fill(email)
        self.fld_company.fill(company)
        if self.chk_newsletter.is_checked() and newsletter is False:
            self.chk_newsletter.uncheck()
        elif not self.chk_newsletter.is_checked() and newsletter is True:
            self.chk_newsletter.check()
        self.fld_password.fill(password)
        re_password = password if re_password is None else re_password
        self.fld_confirm_password.fill(re_password)

        self.btn_register.click()