from playwright.sync_api import Page, expect


def test_checkbox(page: Page):
    page.goto('https://letcode.in/edit')
    input_field_1 = page.locator('//input[@id="fullName"]')
    input_field_1.fill("LastName")
    expect(input_field_1).to_have_text("LastName")
