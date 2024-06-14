import pytest
from playwright.sync_api import Page, expect



@pytest.mark.ok
def test_radiobutton(page: Page):
    page.goto('https://letcode.in/radio')

    page.locator("#one").check()
    expect(page.locator("#one")).to_be_checked()
    expect(page.locator("#two")).not_to_be_checked()

    page.locator("#two").check()
    expect(page.locator("#one")).not_to_be_checked()
    expect(page.locator("#two")).to_be_checked()
