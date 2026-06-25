import re

from page_objects.page_object_base import PageObject

class ProductDetails(PageObject):
    """Page Object Model for the Product Details  Page"""
    def __init__(self, page, product_name, logger):
        """Initialization of the Product Details Page Object.

        Args:
            page: Page Object
            product_name (str): Name of the Product
        Attributes
            product_id = Unique ID of the item
        """
        super().__init__(page, logger)

        self.PAGE_URL = re.compile(rf"/client/#/dashboard/product-details/.*")
        self.PAGE_INDICATOR = self.page.get_by_text(re.compile(rf"{product_name}", re.IGNORECASE))

        self.product_name = product_name
        self.product_id = self.page.url.split("/")[-1]

    def add_item_to_cart(self):
        self.page.get_by_role("button", name = "Add to Cart").click()
        buy_toaster = self.page.get_by_role("alert", name="Product Added To Cart")
        # Toaster Shows
        buy_toaster.wait_for(state="visible", timeout=60000)
        # Toaster Fades
        buy_toaster.wait_for(state="hidden")

    def get_details(self):
        # Product Name
        product_name = self.page.locator("app-product-details h2").inner_text()
        # Product Price
        product_price = self.page.locator("div.col-lg-6.rtl-text h3").inner_text()
        return product_name, product_price
