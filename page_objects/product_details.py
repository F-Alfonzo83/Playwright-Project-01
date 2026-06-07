from configurations.config import Config

class ProductDetails:
    """Page Object Model for the Product Details  Page"""
    def __init__(self, page, product_name):
        """Initialization of the Product Details Page Object.

        Args:
            page: Page Object
            product_name (str): Name of the Product
        Attributes
            product_id = Unique ID of the item
        """
        self.page = page
        self.product_name = product_name
        self.product_id = self.page.url.split("/")[-1]

    def should_be_open(self):
        """Validates the Product Details Page is properly opened

        Returns:

        """
        # Product Name
        self.page.locator("app-product-details h2").wait_for(state="visible")
        # Product Price
        self.page.locator("div.col-lg-6.rtl-text h3").wait_for(state="visible")

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
