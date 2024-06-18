from playwright.sync_api import Playwright, sync_playwright, Page, Request, Response


def handle_page(page: Page):
    page.wait_for_load_state()
    print(">>> context page load handler ", page.url)


def handle_request(req: Request):
    print(">>> request: ", req.method, req.headers)


def handle_response(resp: Response):
    print(">>> response: ", resp.status, resp.status_text, resp.headers)


def run_radio_buttons(playwright: Playwright) -> None:
    print("\n---BEGIN run_radio_buttons---\n")
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
    print("\n---END run_radio_buttons---\n")


def run_handle_check(playwright: Playwright) -> None:
    print("\n---BEGIN run_handle_check---\n")
    done = "What needs to be done?"
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context(
        record_video_dir="videos/",
        record_video_size={"width": 640, "height": 480})
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
    print("\n---END run_handle_check---\n")


with sync_playwright() as playwright_context_manager:
    run_radio_buttons(playwright_context_manager)
    run_handle_check(playwright_context_manager)


def test_empty():
    """пустой тест для того чтоб при запуске из pycharm pytest не ругался"""
    pass