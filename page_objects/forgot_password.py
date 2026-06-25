import re

from playwright.sync_api import expect

from page_objects.page_object_base import PageObject


class ForgotPassword(PageObject):
    """Page Object Model for the Forgot Password Page."""

    def __init__(self, page, logger):
        """Initializer for the Forgot Password Page Object.

        Constains constants as  PAGE_URL and custom arguments that point to POM elements.

        Args:
            PAGE_URL (str) : The url of the page where the Forgot Password Page will be shown.
            PAGE_INDICATOR : Aims to a unique element locator that belongs to the page.
        """
        super().__init__(page, logger)

        self.PAGE_URL = re.compile(r".*/client/#/auth/password-new")
        self.PAGE_INDICATOR = self.page.get_by_role("heading", name="Enter New Password")

        self.email_field = self.page.get_by_placeholder("Enter your email address")
        self.password_field = self.page.get_by_role("textbox", name="Passsword")
        self.confirm_password_field = self.page.get_by_placeholder("Confirm Passsword")

    def fill_form(self, email: str, new_password: str, password_confirmation: str):
        """Fills the forgotten password for with the provided information.

        Args:
            email (str): The email address of the user to enter the forgotten password.
            new_password (str): The new password to enter the forgotten password.
            password_confirmation (str): The confirmation password to enter the forgotten password.
        """
        self.email_field.fill(email)
        self.password_field.fill(new_password)
        self.confirm_password_field.fill(password_confirmation)

    def submit_form(self):
        """Submits the form"""
        # Click Save Password
        self.page.get_by_role("button", name="Save New Password").click()

    def validate_error(self):
        expect(self.page.get_by_text("Password and Confirm Password must match with each other.")).to_be_visible()
