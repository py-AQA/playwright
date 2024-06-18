import pytest
from playwright.sync_api import Page, expect


@pytest.mark.ok
def test_hover(page: Page):
    page.goto("https://the-internet.herokuapp.com/hovers")

    page.get_by_role("img", name="User Avatar").nth(1).hover()
    expect(page.get_by_text("name: user2")).to_be_visible()


def test_page(page: Page):
    page.goto('https://naveenautomationlabs.com/opencart/')
    page.get_by_placeholder('Search').fill('search')
    page.locator('.input-group-btn').click()
    print(page.url)
