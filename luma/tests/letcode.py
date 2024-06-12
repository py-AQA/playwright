from playwright.sync_api import Page, expect


def test_letcode_playwright(page: Page):
    page.goto('https://letcode.in/edit')
    page.locator('//input[@id="fullName"]').fill("LastName")
    expect(page.locator('#fullName')).not_to_be_empty()

    input_2 = page.locator("#join")
    input_2.click()
    input_2.type(" Any")
    input_2.press("Tab")

    expect(page.locator("#getMe")).to_have_value("ortonikc")
    page.locator("#clearMe").clear()
    expect(page.locator("#clearMe")).to_be_empty()
    expect(page.locator('#noEdit')).to_be_disabled()
    expect(page.locator('#dontwrite')).not_to_be_editable()
