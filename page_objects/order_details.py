import re

from playwright.sync_api import expect

from page_objects.page_object_base import PageObject

class OrderDetails(PageObject):
    def __init__(self, page, logger, order_id:str):
        self.order_id = order_id
        super().__init__(page, logger)

        self.PAGE_INDICATOR = self.page.get_by_text(re.compile(r"order summary", re.IGNORECASE))
        self.PAGE_URL = re.compile(rf"/client/#/dashboard/order-details/{order_id}")

    def verify_order_message(self):
        expect(self.page.locator("css=.tagline")).to_contain_text("Thank you for Shopping With Us")