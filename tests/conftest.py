import pytest

from configurations.config import Config
from page_objects.login import LoginPage


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chromium"
    )

@pytest.fixture(scope="session")
## Here, request functions as a method that retrieves variables from other files
def user_credentials(request):
    return request.param

@pytest.fixture()
def browser_instance(playwright, request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chromium":
        browser = playwright.chromium.launch(headless=True)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

@pytest.fixture()
def dashboard_page(browser_instance):
    conf  = Config()
    user, password = conf.get_credentials_main()
    login_page = LoginPage(browser_instance)
    login_page.navigate()
    dashboard_page = login_page.login(username=user,
                     password=password)
    dashboard_page.should_be_open()
    yield dashboard_page