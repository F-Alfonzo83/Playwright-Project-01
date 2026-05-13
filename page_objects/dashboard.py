from page_objects.order_history import OrderHistory


class DashboadPage:
    def __init__(self, page):
        self.page = page

    def go_to_orders(self):
        ## GO TO ORDERS PAGE
        self.page.get_by_role("button", name="ORDERS").click()
        return OrderHistory(self.page)