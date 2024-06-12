from playwright.async_api import Page
from playwright.sync_api import expect


def test_redirect_to_contact_form_from_notes(page: Page):
    page.goto("https://magento.softwaretestingboard.com/")
    with page.context.expect_page() as tab:
        page.get_by_role("link", name="Notes").click()
    new_tab = tab.value
    assert new_tab.url == "https://softwaretestingboard.com/magento-store-notes/?utm_source=magento_store&utm_medium=banner&utm_campaign=notes_promo&utm_id=notes_promotion"
    # page.pause()
    magento = new_tab.locator('h1.alignwide')
    print(magento.inner_text())
    expect(magento).to_have_text("Magento 2 Store(Sandbox site) – Notes")
