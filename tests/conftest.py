import pytest

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