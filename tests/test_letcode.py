# import re
# from playwright.sync_api import Page, expect
#
# base_url = 'https://letcode.in/radio'
#
#
# def test_radiobutton(page: Page):
#     page.goto(base_url)
#     # page.wait_for_timeout(3000)
#     page.locator("#one").check()
#     page.locator("#two").check()
#     # page.get_by_label("Remember me").uncheck()
#     radio_loct = page.get_by_text("#two")
#     expect(radio_loct).to_be_checked()

from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(viewport={"width":800,"height":600})
    page = context.new_page()
    page.goto("https://letcode.in/radio")
    page.locator("#one").check()
    page.get_by_label("Remember me").uncheck()
    page.locator("#two").check()
    page.locator("#one").check()
    page.locator("#two").check()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
