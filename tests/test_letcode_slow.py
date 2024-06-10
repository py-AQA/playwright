from playwright.sync_api import Page, expect

base_url = 'https://letcode.in/radio'


def test_radiobutton(page: Page):
    page.goto(base_url)
    # page.wait_for_timeout(3000)
    page.locator("#one").check()
    page.locator("#two").check()
    # page.get_by_label("Remember me").uncheck()
    radio_loct = page.locator("#two")
    # page.pause()
    expect(radio_loct).to_be_checked()
