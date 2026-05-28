from playwright.sync_api import Playwright

from configurations.config import Config
from page_objects.login import LoginPage

config = Config()
user_mail,user_pass = config.get_credentials_main()


def test_login_user(playwright: Playwright, browser_instance):
    login_page = LoginPage(browser_instance)
    login_page.navigate()
    login_page.login(username=user_mail, password=user_pass)

def test_forgot_password(playwright: Playwright, browser_instance):
    login_page = LoginPage(browser_instance)
    login_page.navigate()
    forgot_password_page = login_page.forgot_password()
    forgot_password_page.fill_form(email=)
    forgot_password_page.submit_form()
