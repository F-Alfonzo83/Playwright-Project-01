import pytest
from playwright.sync_api import Playwright
from configurations.config import  Config
from page_objects.dashboard import DashboadPage
from plawright_clients.auth_client import AuthClient
from plawright_clients.base_client import BaseClient
from page_objects.login import LoginPage

config = Config()
user_mail,user_pass = config.get_credentials_main()
user_credentials_list = config.get_all_credentials()

def login(playwright: Playwright, user_credentials):
    loginClient = AuthClient(playwright=playwright)
    login=loginClient.auth(email=user_credentials["email"],
                          password=user_credentials["password"])
    print(f"Bearer Token: {login}")
    return login

def create_order(playwright: Playwright, user_credentials):
    payload = {
                "orders": [
                    {
                    "country": "Antarctica",
                    "productOrderedId": "6960ea76c941646b7a8b3dd5"
                    }
                        ]
                }
    token = login(playwright, user_credentials)
    orderClient = BaseClient(playwright=playwright)
    place_order= orderClient._post(url ="api/ecom/order/create-order",
                                   data=payload,
                                   headers= {"Authorization": token})
    assert place_order.ok
    orderId = place_order.json()["orders"][0]
    print(f"Created Order ID: {orderId}")
    return orderId

## "user_credentials" is a PARAMETER. user_credentials_list is a variable (stores the credentials)
@pytest.mark.parametrize("user_credentials", user_credentials_list)
## To the Test, you pass "user_credentials" as a FIXTURE (do not confuse with the parameter on top)
## IMPORTANT: The "user_credentials" fixture must return the parameter for "user_credentials"
def test_create_order_api(playwright: Playwright, browser_instance, user_credentials):
    user_mail = user_credentials["email"]
    user_pass = user_credentials["password"]

    ##Browser is provided by browserInstance fixture.

    ## We will Create the Order via API
    order_id = create_order(playwright=playwright, user_credentials=user_credentials)

    ### PAGE OBJECT MODEL
    login_page= LoginPage(browser_instance) #Here you pass the fixture. It returns the page.
    login_page.navigate() ## This will take you to the login page.
    login_page.login(username=user_mail, password= user_pass)

    dashboard_page = login_page.login(username=user_mail, password= user_pass)
    orders_page = dashboard_page.go_to_orders()
    order_details = orders_page.select_order(order_id=order_id)
    order_details.verify_order_message()





