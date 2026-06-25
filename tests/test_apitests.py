import pytest
from playwright.sync_api import Playwright
from configurations.config import  Config
from page_objects.login import LoginPage
from plawright_clients.orders_client import OrdersClient

config = Config()
user_mail,user_pass = config.get_credentials_main()
user_credentials_list = config.get_all_credentials()

## "user_credentials" is a PARAMETER. user_credentials_list is a variable (stores the credentials)
@pytest.mark.parametrize("user_credentials", user_credentials_list)
## To the Test, you pass "user_credentials" as a FIXTURE (do not confuse with the parameter on top)
## IMPORTANT: The "user_credentials" fixture must return the parameter for "user_credentials"
def test_create_order_api(playwright: Playwright, browser_instance, user_credentials,  session_logger):
    user_mail = user_credentials["email"]
    user_pass = user_credentials["password"]

    ##Browser is provided by browserInstance fixture.

    ## We will Create the Order via API
    order_id = OrdersClient(playwright).place_order(user_mail, user_pass)

    ### PAGE OBJECT MODEL
    login_page= LoginPage(browser_instance, session_logger) #Here you pass the fixture. It returns the page.
    login_page.navigate() ## This will take you to the login page.

    login_page.fill_form(user_mail, user_pass)
    dashboard_page = login_page.submit_login()
    orders_page = dashboard_page.go_to_orders()
    orders_page.should_be_open()
    order_details = orders_page.select_order(order_id=order_id)
    order_details.verify_order_message()










