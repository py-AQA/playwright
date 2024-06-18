import pytest
from playwright.sync_api import Page, expect


@pytest.mark.ok
def test_input_field_key_press_and_type(page: Page):
    page.goto('https://letcode.in/edit')

    input = page.locator("//input[@id='fullName']")
    expect(input).to_be_editable()

    input.fill("Test")
    second_input = page.locator("#join")
    expect(second_input).to_be_visible()
    expect(second_input).not_to_be_empty()

    second_input.press("End")
    second_input.type(" new")
    second_input.press("Tab")

    expect(page.locator("#getMe")).to_have_value("ortonikc")

    page.locator("#clearMe").clear()
    expect(page.locator("#clearMe")).to_be_empty()

    expect(page.locator("#noEdit")).to_be_disabled()

    expect(page.locator("#dontwrite")).not_to_be_editable()
