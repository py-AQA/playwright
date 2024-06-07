import time

# from selene import browser, be, have
# from selene.support.shared.jquery_style import s, ss
from selenium.webdriver import Keys

from pages.locators import ProductLocators as PL


# from selenium.webdriver.support.color import Color

def add_to_cart_from_main_page(self):
    s(PL.ARGUS_All_WEATHER_TANK_SIZE).click()
    s(PL.ARGUS_All_WEATHER_TANK_COLOR).click()
    s(PL.ARGUS_All_WEATHER_TANK_ADD_TO_CARD).click()


def go_to_mini_cart(self):
    s(PL.MINI_BASKET_WINDOW).should(be.clickable).click()


def go_to_checkout_cart(self):
    s(PL.VIEW_AND_EDIT_CART_LINK).click()


def checkout():
    time.sleep(3)
    s('.viewcart').should(be.clickable)
    s('#top-cart-btn-checkout').should(be.clickable).click()


def check_color_of_view_and_edit_cart_link_in_the_mini_cart():
    s('a.action').should(have.css_property("color", Color.from_string("#006bb4").rgba))


def check_clickability_of_view_and_edit_cart_link_in_the_mini_cart():
    edit = s(PL.VIEW_AND_EDIT_CART_HREF)
    edit.should(have.attribute("href"))


def checking_the_link_opens_checkout_cart_page():
    s(PL.VIEW_AND_EDIT_CART_LINK).click()


def checking_the_size_color_and_product_name_are_correct(size, color, item_name):
    s(PL.SEE_DETAILS).click()
    s(PL.SIZE_M).should(have.text(size))
    s(PL.COLOR_GRAY).should(have.text(color))
    s(PL.NAME_ITEM).should(have.text(item_name))


def checking_present_price_item_and_cart_subtotal_in_the_mini_cart(price, subtotal):
    s(PL.PRICE_ITEM).should(have.text(price))
    s(PL.CART_SUBTOTAL).should(have.text(subtotal))


def change_qty(qty):
    s(PL.QTY_FIELD).should(be.clickable).send_keys(Keys.BACKSPACE + qty)
    s(PL.UPDATE).click()


def should_be_quantity_change(qty):
    s(PL.QTY_FIELD).should(have.value(qty))
    time.sleep(2)


def should_be_success_message(text):
    s(".message-success").should(be.visible)
    s(".message-success").should(have.text(text))


def should_be_change_subtotal(price, subtotal):
    s(PL.PRICE_ITEM).should(have.text(price))
    s(PL.CART_SUBTOTAL).should(have.text(subtotal))
