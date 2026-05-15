from playwright.sync_api import expect


class RegistrationPage:
    def __init__(self, page):
        self.page = page

    def fill_form(self,
                  first_name:str=None,
                  last_name:str=None,
                  email:str=None,
                  phone_number:str=None,
                  password:str=None):

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
        self.page.get_by_role("button", name="Register").click()

    def verify_registration_success(self):
        expect(self.page.get_by_role("heading", name="Account Created Successfully")).to_be_visible()
        expect(self.page.get_by_role("button", name="Login")).to_be_visible()
        expect(self.page.get_by_role("link", name="Register")).to_be_visible()





