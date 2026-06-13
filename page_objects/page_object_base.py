import playwright
from playwright.sync_api import expect


class PageObject:
    def __init__(self, page, logger):
        self.page = page
        self.logger = logger

        self.PAGE_URL:str =""
        self.PAGE_INDICATOR = ""

    def should_be_open(self):
        expect(self.page).to_have_url(self.PAGE_URL)
        expect(self.PAGE_INDICATOR).to_be_visible()

