from configurations.config import Config
from page_objects.dashboard import DashboadPage

config = Config()

class LoginPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto(config.get_rahul_url_login())

    def login(self, username, password):
        ## Fill Credentials
        self.page.get_by_role("textbox", name="email@example.com").fill(username)
        self.page.get_by_role("textbox", name="enter your passsword").fill(password)
        ## LOGIN
        self.page.get_by_role("button", name="Login").click()
        ## NOTE:
        # I know that this will take me to the "Dashboard" page.
        # The idea is to return the page object after the login
        return DashboadPage(self.page)