import pytest
from playwright.sync_api import Page, expect


@pytest.mark.ok
def test_shadow_root(page: Page):
    page.goto("https://the-internet.herokuapp.com/shadowdom")
    page.get_by_text("In a list!").click()
    expect(page.get_by_text("In a list!")).to_be_visible()


@pytest.mark.ok
def test_shadow_root2(page: Page):
    page.goto("https://the-internet.herokuapp.com/shadowdom")
    page.locator('//*[@id="content"]/my-paragraph[2]/ul/li[2]').click()
    expect(page.get_by_text("In a list!")).to_be_visible()
