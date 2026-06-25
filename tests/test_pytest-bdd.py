from playwright.sync_api import Playwright
from pytest_bdd import given, when, then, parsers, scenarios
from configurations.config import Config
from page_objects.dashboard import DashboadPage
from page_objects.login import LoginPage
from page_objects.order_details import OrderDetails
from page_objects.order_history import OrderHistory
from plawright_clients.orders_client import OrdersClient
from dataclasses import dataclass

scenarios(str(Config.scenario_file))

# APPROACH USING A DATACLASS


@dataclass
class OrderTransaction:
    order_id: str = None
    login_page: LoginPage = None
    dashboard_page: DashboadPage = None
    orders_page: OrderHistory = None
    order_details: OrderDetails = None

# Order Transaction Feature


@given(parsers.parse("Place the item order with {username} and {password} using the API"))
def place_item_order(playwright: Playwright, username: str, password: str):
    order_id = OrdersClient(playwright).place_order(username, password)
    OrderTransaction.order_id = order_id
    print(f"Order Transaction saved with value: {OrderTransaction.order_id}")


@given("the user is on the landing page")
def user_is_on_landing_page(browser_instance):
    login_page = LoginPage(browser_instance)  # Here you pass the fixture. It returns the page.
    login_page.navigate()  # This will take you to the login page.
    OrderTransaction.login_page = login_page


@when(parsers.parse("I Login to portal with {username} and {password}"))
def login(username: str, password: str):

    login_page = OrderTransaction.login_page
    login_page.fill_form(username, password)
    dashboard_page = login_page.submit_login()
    OrderTransaction.dashboard_page = dashboard_page


@when("Navigate to orders page")
def navigate_to_orders_page():
    dashboard_page = OrderTransaction.dashboard_page
    orders_page = dashboard_page.go_to_orders()
    OrderTransaction.orders_page = orders_page


@when("Select the order with the correct order Id")
def select_order():
    orders_page = OrderTransaction.orders_page
    print(f"Calling Order ID from Dataclass with Value: {OrderTransaction.order_id}")
    order_details = orders_page.select_order(order_id=OrderTransaction.order_id)
    OrderTransaction.order_details = order_details


@then("order message is successfully displayed")
def validate_order_message():
    order_details = OrderTransaction.order_details
    order_details.verify_order_message()
