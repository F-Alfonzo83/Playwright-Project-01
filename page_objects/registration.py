import playwright
from playwright.sync_api import expect


class RegistrationPage:
    """Page Object Model for Registration page.

    Serves as the base of operation for actions that can be executed on the registration page"""
    def __init__(self, page: playwright.page.Page) -> None:
        """Constructor for RegistrationPage

        Args:
            page (playwright.page.Page): Page Object Model
        """
        self.page = page

    def should_be_open(self):
        """Hard Validator for Registration page.

        Validates that the page loads with correct heading and url.
        Breaks in case of assertion error

        Raises:
            playwright.exceptions.AssertionError in case an assertion error occurs
        """
        expect(self.page.get_by_role("heading", name="Register")).to_be_visible()
        expect(self.page).to_have_url("https://rahulshettyacademy.com/client/#/auth/register")

    def should_show_registration_form(self):
        """Soft validator for the Registration Page.

        Softly validates that the registration form elements are visible.
        """

        expect.soft(self.page.get_by_placeholder("First Name")).to_be_visible()
        expect.soft(self.page.get_by_placeholder("Last Name")).to_be_visible()
        expect.soft(self.page.get_by_placeholder("email@example.com")).to_be_visible()
        expect.soft(self.page.get_by_placeholder("enter your number")).to_be_visible()
        expect.soft(self.page.get_by_role("textbox", name="Passsword")).to_be_visible()
        expect.soft(self.page.get_by_placeholder("Confirm Passsword")).to_be_visible()

    def should_be_healthy(self):
        """Acts like a wrapper for the Registration Page validators.

        Wraps self.should_be_open() and self.should_show_registration_form() on a single call.

        Raises:
            playwright.exceptions.AssertionError in case an assertion error occurs
        """
        self.should_be_open()
        self.should_show_registration_form()

    def fill_form(self,
                  first_name:str=None,
                  last_name:str=None,
                  email:str=None,
                  phone_number:str=None,
                  password:str=None):
        """Fills the registration page with data

        Args:
            first_name (str): First Name
            last_name (str): Last Name
            email (str): Email address
            phone_number (str): Phone number (10 Digits)
            password (str): Password
            """

        # Retrieve First name field and input first name, last name, email, phone
        self.page.get_by_placeholder("First Name").fill(first_name)
        self.page.get_by_placeholder("Last Name").fill(last_name)
        self.page.get_by_placeholder("email@example.com").fill(email)
        self.page.get_by_placeholder("enter your number").fill(phone_number)
        self.page.get_by_role("textbox", name="Passsword").fill(password)
        self.page.get_by_placeholder("Confirm Passsword").fill(password)
        #  Select Radio male or female
        self.page.get_by_role("radio",name="Male", exact=True).check()
        # Check the Checkbox
        self.page.get_by_role("checkbox").check()

    def submit_registration(self):
        """Submits the registration form."""
        self.page.get_by_role("button", name="Register").click()

    def verify_registration_success(self):
        """Verifies that the registration was successful.

        Executes hard checks to validate that the registration was successful.

        Raises:
            playwright.exceptions.AssertionError in case an assertion error occurs
        """
        expect(self.page.get_by_role("heading", name="Account Created Successfully")).to_be_visible()
        expect(self.page.get_by_role("button", name="Login")).to_be_visible()
        expect(self.page.get_by_role("link", name="Register")).to_be_visible()

    def verify_registration_failure(self):
        """Verifies that the registration was not successful.

        Executes hard checks to validate that the registration was a failure

        Raises:
            playwright.exceptions.AssertionError in case an assertion error occurs
        """
        expect(self.page.get_by_role("alert")).to_be_visible()





