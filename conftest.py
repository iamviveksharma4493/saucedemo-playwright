import pytest
from playwright.sync_api import sync_playwright
from utils.env_reader import get_env_variable

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as playwright:
        yield playwright

@pytest.fixture(scope="function")
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=False, slow_mo=1000) # slow_mo - slow motion execution
    context = browser.new_context()
    page = context.new_page()
    page.goto(get_env_variable("BASE_URL")) # Added to use url from .env file
    yield page
    context.close()
    browser.close()

@pytest.fixture(scope="session")
def credentials():
    return {
        "username": get_env_variable("STANDARD_USER"),
        "password": get_env_variable("PASSWORD"),
        "first_name": get_env_variable("FIRST_NAME"),
        "last_name": get_env_variable("LAST_NAME"),
        "postal_code": get_env_variable("POSTAL_CODE")
    }

# Old file

# import pytest
# from playwright.sync_api import sync_playwright

# @pytest.fixture(scope="session")
# def browser_context():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False, slow_mo=1000)
#         context = browser.new_context()
#         yield context
#         context.close()
#         browser.close()