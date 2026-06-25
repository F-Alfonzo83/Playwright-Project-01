import pytest
from playwright.sync_api import Playwright

from configurations.config import Config

config = Config()
user_name, user_pass = config.get_credentials_main()

def test_get_objects_for_sale(dashboard_page):
    dashboard_page.should_be_open()
    card_names = dashboard_page.get_product_cards_names()
    print(card_names)

@pytest.mark.parametrize("product_name", config.get_test_card_names())
def test_add_items_to_cart(dashboard_page, product_name):
    dashboard_page.should_be_open()
    dashboard_page.add_items_to_cart(product_name)
    dashboard_page.check_number_items_in_cart()

@pytest.mark.parametrize("product_name", config.get_test_card_names())
def test_get_item_detail(dashboard_page, product_name):
    dashboard_page.should_be_open()
    product_page = dashboard_page.view_item(product_name)
    product_page.should_be_open()
    product, price  = product_page.get_details()

    assert product_page.product_id == config.get_test_product_id(product_name)
    assert product == config.get_test_product_name(product_name)
    assert price == f"$ {config.get_test_product_price(product_name)}"
