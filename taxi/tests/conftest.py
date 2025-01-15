import pytest
from playwright.sync_api import Playwright, Page


pytest_plugins = [
   "taxi.tests.steps.steps"
]


@pytest.fixture
def setup_browser(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    print("Launching browser page...")
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://localhost:8000/")
    yield page
    context.close()
    browser.close()
    print("Closing browser page...")
