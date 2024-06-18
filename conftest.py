import pytest
from playwright.sync_api import Dialog, sync_playwright, Page


@pytest.fixture(scope="session")
def browser_context_args():
    return {
        # "record_video_dir": "videos/",
        # "record_video_size": {"width": 640, "height": 480},
        "viewport": {"width": 800, "height": 800}
        # "viewport": {
        #     "width": 1920,
        #     "height": 1080,
        # }
    }

@pytest.fixture
def my_page() -> Page:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        context.add_init_script("localStorage.setItem('accessToken', {'token': 666, 'isFirstUser': true})")
        page = context.new_page()
        yield page
        page.close()
        browser.close()
