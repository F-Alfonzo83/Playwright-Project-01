from playwright.sync_api import expect
from configurations.config import Config
from page_objects.order_history import OrderHistory
from page_objects.page_object_base import PageObject
from page_objects.product_details import ProductDetails


class DashboadPage(PageObject):
    """Page Object Model  for the Dashboard page."""
    def __init__(self, page, logger):
        super().__init__(page, logger)
        """Initialize the Dashboard Page Object.

        Args:
            page (Page): Playwright Page Object

        Attributes
            self.product_cards (Playwright Selector): Contains the collection of item product cards
            self.orders_btn (Playwright  selector button): Points to the orders  button
        """

        self.config = Config()
        self.product_cards =  self.page.locator("section#products>div.container div.row div.card")
        self.orders_btn = self.page.get_by_role("button", name="ORDERS")

        self.PAGE_URL = "https://rahulshettyacademy.com/client/#/dashboard/dash"
        self.PAGE_INDICATOR = self.page.get_by_role("heading", name="AUTOMATION")

    def go_to_orders(self):
        """Takes the user to the "Order History" page.

        Returns:
            Order History Page Object
        """
        self.logger.info("Clicking Orders button -> Transition to Order History")
        self.orders_btn.click()
        return OrderHistory(self.page, self.logger)

    def get_product_cards_names(self):
        """Retrieves the names of the products cards.

        Returns:
            card_names (list[str]): Contains the names of the products cards
        """
        self.logger.info("Retrieving the names of the products cards")
        card_names = self.product_cards.locator("h5").all_inner_texts()
        return card_names

    def add_items_to_cart(self, product_name: str):
        """Adds a specific item to the shopping cart.

        Receiving the name of the product, uses it to filter through the item cards and adds it to the cart.
        """
        self.logger.info(f"Locating Item {product_name}")
        product_card = self.product_cards.filter(has_text=product_name)
        self.logger.info("Adding item to cart")
        product_card.get_by_role("button",name = "Add to cart").click()
        self.logger.info("Awaiting item confirmation")
        buy_toaster = self.page.get_by_role("alert",name="Product Added To Cart")
        #Toaster Shows
        buy_toaster.wait_for(state="visible", timeout=60000)
        #Toaster Fades
        buy_toaster.wait_for(state="hidden")

    def view_item(self, item_name:str):
        """Views a specific item from the dashboard.

        Receives the product name, uses it to filter through the item
        """
        self.logger.info(f"Locating Item {item_name}")
        item_card = self.product_cards.filter(has_text=item_name)
        self.logger.info(f"Navigating to {item_name} Product Detail page")
        item_card.get_by_role("button",name = "View").click()
        return ProductDetails(self.page, item_name, self.logger)

    def check_number_items_in_cart(self):
        """Retrieves the number of items in the cart at the moment."""
        self.logger.info("Retrieving the number of items in the cart")
        number_items = self.page.locator("button.btn.btn-custom>label").text_content()
        return number_items


