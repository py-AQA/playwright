from playwright.sync_api import Page
from playwright.sync_api import expect

from luma.pages import mini_cart


def test_redirection_magento_store_notes(page: Page):
    page.goto("https://magento.softwaretestingboard.com")
    # page.pause()
    page.get_by_role("link", name="Notes").click()
    with page.context.expect_page() as tab:
        new_tab = tab.value
    assert new_tab.url == ("https://softwaretestingboard.com/magento-store-notes/?utm_source=magento_store&utm_medium"
                           "=banner&utm_campaign=notes_promo&utm_id=notes_promotion")

    header = new_tab.locator('[class="alignwide wp-block-post-title"]')
    assert header.is_visible()
    expect(header).to_have_text("Magento 2 Store(Sandbox site) – Notes")


def test_add_item(page: Page):
    page.goto(mini_cart.main_page_link)
    # page.pause()
    mini_cart.add_item(page, name_item="Hero Hoodie", size="S", color="Gray")
    mini_cart.add_qty(page, qty_items="1")
    # qty_counter = page.locator('//*[@class="counter-number"]')
    # time.sleep(4)
    # print(qty_counter.inner_html(), type(qty_counter))
    # print(qty_counter.text_content(), type(qty_counter))
    # print(qty_counter.all_inner_texts(), type(qty_counter))
    # print(qty_counter.inner_text(), type(qty_counter))
    # print(qty_counter, type(qty_counter))
    # expect(qty_counter).to_have_text("1")


