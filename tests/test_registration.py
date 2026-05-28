import pytest
from playwright.sync_api import Playwright
from page_objects.login import LoginPage


def test_register_user(playwright: Playwright,browser_instance):
    login_page = LoginPage(browser_instance)
    login_page.navigate()
    register_page =login_page.register_new()
    register_page.fill_form(first_name="Frist Name",
                            last_name="Last Name",
                            email="Test@email.com",
                            phone_number="1234567890",
                            password="Password"
                            )
    register_page.submit_registration()

def test_register_user_success_page(playwright: Playwright, browser_instance):
    login_page = LoginPage(browser_instance)
    login_page.navigate() ## This goes to register  page.
    register_page = login_page.register_new()
    register_page.should_be_open()
    register_page.fill_form(first_name="FirstName",
                            last_name="LastName",
                            email="Test-1983-2@email.com",
                            phone_number="1234567890",
                            password="FJAA1983.rahul"
                            )
    register_page.page.route("**/api/ecom/auth/register",
                        lambda route: route.fulfill(
                            status=200,
                            body='{"message":"Registered Successfully"}',
                            content_type="application/json"
                        ))
    register_page.submit_registration()
    register_page.verify_registration_success()

@pytest.mark("negative_scenario")
def test_register_same_user(playwright: Playwright, browser_instance):
    login_page = LoginPage(browser_instance)
    login_page.navigate()
    register_page = login_page.register_new()
    register_page.fill_form(first_name="FirstName",
                            last_name="LastName",
                            email="franciscoj.anguloa@gmail.com",
                            phone_number="1234567890",
                            password="ASDF.1233-abc")
    register_page.submit_registration()
    register_page.verify_registration_failure()
