from playwright.async_api import Page

base_url = 'https://naveenautomationlabs.com/opencart/'


def test_page(page: Page):

    page.goto(base_url)
    page.get_by_placeholder('Search').fill('search')
    page.locator('.input-group-btn').click()
    print(page.url)
    print(page.video.path())

# def test_page_error(page: Page):
#
#     page.goto(base_url)
#     page.get_by_placeholder('Search').fill('search')
#     page.locator('.input-group-btn1').click()
#     print(page.url)
#     # page.pause()


def handle_page(page):
    page.wait_for_load_state()
    print(page.title())
#
# context.on("page", handle_page)