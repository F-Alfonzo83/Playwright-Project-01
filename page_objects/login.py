import re

from playwright.sync_api import expect
from configurations.config import Config
from page_objects.dashboard import DashboadPage
from page_objects.forgot_password import ForgotPassword
from page_objects.page_object_base import PageObject
from page_objects.registration import RegistrationPage

config = Config()

class LoginPage(PageObject):
    """Page Object Model for the Login Page.

    Contains a  list of interactive elements for easier use  and access
    """
    def __init__(self, page, logger):
        """Initializes the Login Page: Child of PageObject.

        Args:
            page (Page): Page from Playwright. Inherits from PageObject.
            logger (Logger): Logger object. Inherits from PageObject.

        Attributes:
            PAGE_URL (str): Expected Page URL on  regex format.
            PAGE_INDICATOR : Playwright Locator used to validate the page is open
        """
        super().__init__(page, logger)

        #Constants
        self.PAGE_URL = re.compile(r".*/client/#/auth/login")
        self.PAGE_INDICATOR = self.page.get_by_role("heading", name= "Log in")

        #Page Interactive Required Elements.
        self.email_field = self.page.get_by_role("textbox", name="email@example.com")
        self.password_field = self.page.get_by_role("textbox", name="enter your passsword")
        self.login_button = self.page.get_by_role("button", name="Login")

    def should_show_login_form(self):
        """Softly verifies that the login page fields are shown and visible."""

        expect.soft(self.email_field).to_be_visible()
        expect.soft(self.password_field).to_be_visible()
        expect.soft(self.login_button).to_be_visible()

    def navigate(self):
        self.logger.info("Navigating to the login page")
        self.page.goto(config.get_rahul_url_login())

    def fill_form(self,username,password):
        """Fills the login page with username and password.

        Args
            username (str): Username to login with.
            password (str): Password to login with.
        """
        self.logger.info("Filling email on form")
        self.email_field.fill(username)
        self.logger.info("Filling password on form")
        self.password_field.fill(password)

    def submit_login(self):
        """Completes login.

        Navigates to the Dashboard page after a successful login

        Returns:
            dashboard_page (DashboadPage): Dashboard page object.
        """
        self.logger.info("Submitting the Login form -> Goingto the Dashboard page")
        self.login_button.click()
        dashboard_page = (DashboadPage(self.page, self.logger))
        dashboard_page.should_be_open()
        return dashboard_page

    def register_new(self):
        """Navigates to the Registration page from the login.

        Returns:
            registration_page (RegistrationPage): Registration page object.
        """

        self.page.get_by_text("Register here").click()
        registration_page = RegistrationPage(self.page, self.logger)
        registration_page.should_be_healthy()
        return registration_page

    def forgot_password(self):
        """Transitions to the "Forgot Password" page from the login.

        Returns:
            forgot_password_page (ForgotPassword): Forgot Password page object.
        """
        self.page.get_by_role("link", name="Forgot password?").click()
        forgot_password_page = ForgotPassword(self.page)
        forgot_password_page.should_be_open()
        return forgot_password_page
        
        

