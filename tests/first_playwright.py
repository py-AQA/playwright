from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    done = "What needs to be done?"
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_placeholder(done).click()
    page.get_by_placeholder(done).fill("Создать первый сценарий playwright")
    page.get_by_placeholder(done).press("Enter")
    page.get_by_role("checkbox", name="Toggle Todo").check()

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
