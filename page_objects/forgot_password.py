class ForgotPassword:
    def __init__(self, page):
        self.page =  page

    def fill_form(self, email:str, new_password:str):
        self.page.get_by_role("texbox", name="Enter your email address").fill(email)
        self.page.get_by_role("textbox", name= "Passsword").fill(new_password)
        self.page.get_by_role("textbox", name="Confirm Passsword").fill(new_password)
    def submit_form(self):
        #Click Save Password
        self.page.get_by_role("button", name="Save New Password").click()

