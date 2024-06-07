import pytest
from playwright.async_api import Page
from playwright.sync_api import Playwright, sync_playwright, expect
# from pages.mini_cart import *
main_page_link = "https://magento.softwaretestingboard.com"

@pytest.fixture
def browser_fixture():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        page.close()
        browser.close()


def test_go_to_mini_cart(page: Page):
    page.goto(main_page_link)
    # page.pause()
    page.locator("li").filter(has_text="Argus All-Weather Tank As low").get_by_label("M").click()
    page.locator("li").filter(has_text="Argus All-Weather Tank As low").get_by_label("Gray").click()
    page.locator("li").filter(has_text="Argus All-Weather Tank As low").get_by_role("button").click()



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
