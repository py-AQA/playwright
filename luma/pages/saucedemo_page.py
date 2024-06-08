from playwright.async_api import Page

main_page_link = "https://www.saucedemo.com/"


def log_in(page: Page):
    page.goto(main_page_link)
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"username\"]").click()
    password_input = page.locator("[data-test=\"password\"]")
    password_input.fill("secret_sauce")
    password_input.click()
    page.locator("[data-test=\"login-button\"]").click()


def add_item_to_basket(page: Page):
    log_in(page)
    page.locator("[data-test=\"add-to-cart-sauce-labs-bike-light\"]").click()
    page.locator("[data-test=\"add-to-cart-sauce-labs-bolt-t-shirt\"]").click()


def redirection_cart_page(page: Page):
    add_item_to_basket(page)
    page.locator("[data-test=\"shopping-cart-link\"]").click()
