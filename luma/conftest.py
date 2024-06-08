import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def browser_fixture():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        page.close()
        browser.close()


@pytest.fixture(scope="session")
def browser_context_args():
    return {

        "viewport": {
            "width": 1400,
            "height": 900,
        }
    }
