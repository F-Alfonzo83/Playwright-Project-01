from faker import Faker
from configurations.config import Config
from configurations.logger import _logger
from page_objects.login import LoginPage


logger = _logger(__name__)
config = Config()
fake = Faker()

user, password = config.get_credentials_main()


def test_register_user(browser_instance):
    login_page = LoginPage(browser_instance, logger)
    login_page.navigate()
    register_page = login_page.register_new()
    register_page.fill_form(first_name=fake.first_name(),
                            last_name=fake.last_name(),
                            email=fake.email(),
                            phone_number="1234567890",
                            password=password
                            )
    register_page.submit_registration()


def test_register_user_success_page(browser_instance):
    login_page = LoginPage(browser_instance, logger)
    login_page.navigate()  # This goes to register  page.
    register_page = login_page.register_new()
    register_page.should_be_open()
    register_page.fill_form(first_name=fake.first_name(),
                            last_name=fake.last_name(),
                            email=fake.email(),
                            phone_number="1234567890",
                            password=password
                            )
    register_page.page.route("**/api/ecom/auth/register",
                             lambda route: route.fulfill(
                                 status=200,
                                 body='{"message":"Registered Successfully"}',
                                 content_type="application/json"
                             ))
    register_page.submit_registration()
    register_page.verify_registration_success()


def test_register_same_user(browser_instance):
    login_page = LoginPage(browser_instance, logger)
    login_page.navigate()
    register_page = login_page.register_new()
    register_page.fill_form(first_name="FirstName",
                            last_name="LastName",
                            email=user,
                            phone_number="1234567890",
                            password=password)
    register_page.submit_registration()
    register_page.verify_registration_failure()
