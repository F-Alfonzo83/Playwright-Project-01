from playwright.sync_api import expect

from configurations.config import Config
from page_objects.dashboard import DashboadPage
from page_objects.forgot_password import ForgotPassword
from page_objects.registration import RegistrationPage

config = Config()

class LoginPage:
    """Page Object Model for the Login Page."""
    def __init__(self, page):
        """Initializes the Login Page.

        Args:
            page (Page): Page Object Model for the Login Page.

        Attributes:
            email_field (Locator): Locator for the email field.
            password_field (Locator): Locator for the password field.
        """

        self.page = page

        self.email_field = self.page.get_by_role("textbox", name="email@example.com")
        self.password_field = self.page.get_by_role("textbox", name="enter your passsword")

        self.login_button = self.page.get_by_role("button", name="Login")

    def should_be_open(self):
        """Validates that the login page is open.

        Also allows the items in the page to load
        """
        expect(self.page).to_have_url("https://rahulshettyacademy.com/client/#/auth/login")
        expect(self.page.get_by_role("heading", name= "Log in")).to_be_visible()

    def should_show_login_form(self):
        """Softly verifies that the login page fields are shown and visible."""

        expect.soft(self.email_field).to_be_visible()
        expect.soft(self.password_field).to_be_visible()
        expect.soft(self.login_button).to_be_visible()

    def navigate(self):
        self.page.goto(config.get_rahul_url_login())

    def fill_form(self,username,password):
        """Fills the login page with username and password.

        Args
            username (str): Username to login with.
            password (str): Password to login with.
        """
        self.email_field.fill(username)
        self.password_field.fill(password)

    def submit_login(self):
        """Completes login.

        Navigates to the Dashboard page after a successful login

        Returns:
            dashboard_page (DashboadPage): Dashboard page object.
        """
        self.login_button.click()
        dashboard_page = (DashboadPage(self.page))
        dashboard_page.should_be_open()
        return dashboard_page

    def register_new(self):
        """Navigates to the Registration page from the login.

        Returns:
            registration_page (RegistrationPage): Registration page object.
        """

        self.page.get_by_text("Register here").click()
        registration_page = RegistrationPage(self.page)
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
        
        

