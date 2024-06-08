from playwright.sync_api import expect

from luma.pages.saucedemo_page import *


def add_item_to_basket(page: Page):
    # page.pause()
    log_in(page)
    page.locator("[data-test=\"add-to-cart-sauce-labs-bike-light\"]").click()
    page.locator("[data-test=\"add-to-cart-sauce-labs-bolt-t-shirt\"]").click()


def test_log_in(page: Page):
    page.goto(main_page_link)
    # page.pause()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"username\"]").click()
    password_input = page.locator("[data-test=\"password\"]")
    password_input.fill("secret_sauce")
    password_input.click()
    page.locator("[data-test=\"login-button\"]").click()
    expect(page).not_to_have_url("https://www.saucedemo.com/")


def test_add_item_to_basket(page: Page):
    log_in(page)
    page.locator("[data-test=\"add-to-cart-sauce-labs-bike-light\"]").click()
    page.locator("[data-test=\"add-to-cart-sauce-labs-bolt-t-shirt\"]").click()
    # page.pause()
    bike_light_del = page.locator("[data-test=\"remove-sauce-labs-bike-light\"]")
    bolt_t_shirt_del = page.locator("[data-test=\"remove-sauce-labs-bolt-t-shirt\"]")
    expect(bolt_t_shirt_del).to_have_text("Remove")
    expect(bike_light_del).to_have_text("Remove")


def test_sort_filter(page: Page):
    log_in(page)
    # page.pause()
    drop_down = page.locator("[data-test=\"product-sort-container\"]")
    page.locator("[data-test=\"product-sort-container\"]").select_option("za")
    expect(drop_down).to_have_value("za")

    page.locator("[data-test=\"product-sort-container\"]").select_option("lohi")
    expect(drop_down).to_have_value("lohi")

    page.locator("[data-test=\"product-sort-container\"]").select_option("hilo")
    expect(drop_down).to_have_value("hilo")

    page.locator("[data-test=\"product-sort-container\"]").select_option("az")
    expect(drop_down).to_have_value("az")


def test_redirection_cart_page(page: Page):
    add_item_to_basket(page)
    # page.pause()
    page.locator("[data-test=\"shopping-cart-link\"]").click()
    expect(page).not_to_have_url("https://www.saucedemo.com/inventory.html")


def test_checking_the_availability_of_item_in_the_cart(page: Page):
    redirection_cart_page(page)
    # page.pause()
    bike_light = page.locator("[data-test=\"item-0-title-link\"]")
    bolt_t_shirt = page.locator("[data-test=\"item-1-title-link\"]")
    expect(bike_light).to_be_visible()
    expect(bolt_t_shirt).to_be_visible()
