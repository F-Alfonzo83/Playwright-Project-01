from page_objects.order_details import OrderDetails


class OrderHistory:
    def __init__(self, page):
        self.page = page

    def select_order(self, order_id:str):
        row = self.page.locator("css=tbody>tr").filter(has_text=order_id)
        row.get_by_role("button", name="View").click()
        return OrderDetails(self.page)