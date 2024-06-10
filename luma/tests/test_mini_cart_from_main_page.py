from playwright.async_api import Page
from playwright.sync_api import expect

from luma.pages import mini_cart
from luma.pages.locators import ProductLocators as PL, ShoppingCart as SC


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
    mini_cart.add_item(page, name_item="Argus All-Weather Tank", size="M", color="Gray", qty_items="1")
    # qty_counter = page.locator('//*[@class="counter-number"][text()="1"]')
    # expect(qty_counter).to_have_text("1")




# def test_go_to_mini_cart(page: Page):
#     page.goto(mini_cart.main_page_link)
#     # page.pause()
#     mini_cart.add_item(page, name_item="Argus All-Weather Tank", size="M", color="Gray")
    # page.get_by_role("link", name=" My Cart 1 1 items").click()

# def test_color_and_clickability_of_view_and_edit_cart_link_in_the_mini_cart():
#     go_to_mini_cart()
#     # mini_cart = BasketPage(browser, main_page_link)
#     mini_cart.check_color_of_view_and_edit_cart_link_in_the_mini_cart()
#     mini_cart.check_clickability_of_view_and_edit_cart_link_in_the_mini_cart()
#
#
# def test_checking_the_link_opens_the_cart_page():
#     go_to_mini_cart()
#     mini_cart.checking_the_link_opens_checkout_cart_page()
#
#
# def test_size_color_and_product_name_are_correct():
#     go_to_mini_cart()
#     mini_cart.checking_the_size_color_and_product_name_are_correct("M", "Gray", "Argus All-Weather Tank")
#
#
# def test_checking_present_price_item_and_cart_subtotal_in_the_mini_cart():
#     go_to_mini_cart()
#     mini_cart.checking_present_price_item_and_cart_subtotal_in_the_mini_cart("$22.00", "$22.00")
#
#
# def test_change_quantity_of_an_item_and_changes_price_in_cart_subtotal_mini_cart():
#     go_to_mini_cart()
#     mini_cart.should_be_success_message("You added Argus All-Weather Tank to your shopping cart.")
#     mini_cart.change_qty("7")
#     mini_cart.should_be_quantity_change("7")
#     mini_cart.should_be_change_subtotal("$22.00", "$154.00")
