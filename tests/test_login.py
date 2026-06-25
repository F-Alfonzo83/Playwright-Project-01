from playwright.sync_api import Playwright

from configurations.config import Config
from page_objects.login import LoginPage

config = Config()
user_mail,user_pass = config.get_credentials_main()


def test_login_user(browser_instance, session_logger):
    login_page = LoginPage(browser_instance, session_logger)
    login_page.navigate()
    login_page.should_be_open()
    login_page.fill_form(username=user_mail, password=user_pass)
    login_page.submit_login()


def test_forgot_password(browser_instance, session_logger):
    login_page = LoginPage(browser_instance, session_logger)
    login_page.navigate()
    forgot_password_page = login_page.forgot_password()
    forgot_password_page.should_be_open()
    forgot_password_page.fill_form(email=user_mail, new_password=user_pass, password_confirmation=user_pass)
    forgot_password_page.submit_form()

def test_negative_forgot_password_not_match(browser_instance, session_logger):
    login_page = LoginPage(browser_instance, session_logger)
    login_page.navigate()
    login_page.should_be_open()
    forgot_password_page = login_page.forgot_password()
    forgot_password_page.should_be_open()
    forgot_password_page.fill_form(email=user_mail, new_password=user_pass,
                                   password_confirmation=(f"{user_pass}bla"))
    forgot_password_page.submit_form()
    forgot_password_page.validate_error()
