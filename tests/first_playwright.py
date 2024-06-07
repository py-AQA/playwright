from playwright.sync_api import Playwright, sync_playwright, expect, Page, Response, Request


def run(playwright: Playwright) -> None:
    done = "What needs to be done?"
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    context.on("page", handle_page)
    context.on("request", handle_request)
    context.on("response", handle_response)
    page = context.new_page()
    page.on("close", lambda _: print(f"close page {page.url}"))
    page.on("load", lambda _: print(f"load page {page.url}"))
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_placeholder(done).click()
    page.get_by_placeholder(done).fill("Создать первый сценарий playwright")
    page.get_by_placeholder(done).press("Enter")
    page.get_by_role("checkbox", name="Toggle Todo").check()

    context.close()
    browser.close()


def handle_page(page: Page):
    page.wait_for_load_state()
    print(">>> context page load handler ", page.url)


def handle_request(req: Request):
    print(">>> request: ", req.method, req.headers)


def handle_response(resp: Response):
    print(">>> response: ", resp.status, resp.status_text, resp.headers)


with sync_playwright() as playwright:
    run(playwright)
