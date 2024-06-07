# from selene import be
# from selene.support.shared.jquery_style import s

from pages.locators import NavigatorLocators as NL, ProductLocators as PL
from selenium.common import NoSuchElementException


class BasePage:

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.open(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

class HomePage(BasePage):

    def go_to_pages(self):
        self.navigate_to(NL.NAV_NEW)
        self.navigate_to(NL.NAV_WOMEN)
        self.navigate_to(NL.NAV_MEN)
        self.navigate_to(NL.NAV_GEAR)
        self.navigate_to(NL.NAV_TRAINING)
        self.navigate_to(NL.NAV_SALE)

    def navigate_to(self, locator):
        s(locator).click()

    def add_to_cart_from_main_page(self):
        s(PL.ARGUS_All_WEATHER_TANK_SIZE).click()
        s(PL.ARGUS_All_WEATHER_TANK_COLOR).click()
        s(PL.ARGUS_All_WEATHER_TANK_ADD_TO_CARD).click()

    def go_to_mini_cart(self):
        s(PL.MINI_BASKET_WINDOW).should(be.clickable).click()

    def go_to_checkout_cart(self):
        s(PL.VIEW_AND_EDIT_CART_LINK).click()

    def find_counter_number(self):
        return s(PL.MINICART_COUNTER)

    def is_counter_number_visible(self):
        return self.find_counter_number().should(be.visible)
