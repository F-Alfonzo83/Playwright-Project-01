import re

from page_objects.order_details import OrderDetails
from page_objects.page_object_base import PageObject


class OrderHistory(PageObject):
    def __init__(self, page, logger):
        super().__init__(page, logger)

        self.PAGE_URL = re.compile(r".*/client/#/dashboard/myorders")
        self.PAGE_INDICATOR = self.page.get_by_text(re.compile(r"Your Orders", re.IGNORECASE))


    def select_order(self, order_id:str):
        row = self.page.locator("css=tbody>tr").filter(has_text=order_id)
        row.get_by_role("button", name="View").click()
        return OrderDetails(self.page, self.logger, order_id)