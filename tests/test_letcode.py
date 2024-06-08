from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(viewport={"width": 800, "height": 600})
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


with sync_playwright() as playwright_context_manager:
    run(playwright_context_manager)
