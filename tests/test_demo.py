from playwright.async_api import Page

base_url = 'https://naveenautomationlabs.com/opencart/'


def test_page(page: Page):

    page.goto(base_url)
    page.get_by_placeholder('Search').fill('search')
    page.locator('.input-group-btn').click()
    print(page.url)
    # page.pause()
