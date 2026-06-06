from playwright.sync_api import expect

class ForgotPassword:
    """Page Object Model for the Forgot Password Page."""
    def __init__(self, page):
        self.page =  page

    def should_be_open(self):
        """Verifies that the Forgot Password page is open."""
        expect(self.page).to_have_url("https://rahulshettyacademy.com/client/#/auth/password-new")
        expect(self.page.get_by_role("heading", name="Enter New Password")).to_be_visible()

    def fill_form(self, email:str, new_password:str, password_confirmation:str):
        """Fills the forgotten password for with the provided information.

        Args:
            email (str): The email address of the user to enter the forgotten password.
            new_password (str): The new password to enter the forgotten password.
            password_confirmation (str): The confirmation password to enter the forgotten password. Allows for broader testing
        """
        self.page.get_by_placeholder("Enter your email address") .fill(email)
        self.page.get_by_role("textbox", name= "Passsword").fill(new_password)
        self.page.get_by_placeholder("Confirm Passsword").fill(password_confirmation)

    def submit_form(self):
        """Submits the form"""
        #Click Save Password
        self.page.get_by_role("button", name="Save New Password").click()

    def validate_error(self):
        expect(self.page.get_by_text("Password and Confirm Password must match with each other.")).to_be_visible()

