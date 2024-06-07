

class SalePageLocators:
    GEAR_DEALS_TITLE = "//*[text()='Gear Deals']"
    BAGS_LINK = "//a[text()='Bags']"
    FITNESS_EQUIPMENT_LINK = "//a[text()='Fitness Equipment']"
    LINK_SALE = "https://magento.softwaretestingboard.com/sale.html"
    LINK_WOMEN_SALE = "https://magento.softwaretestingboard.com/promotions/women-sale.html"
    LINK_TEES_WOMEN = "https://magento.softwaretestingboard.com/women/tops-women/tees-women.html"

    BREADCRUMBS_LINKS_ON_PAGE_TEES = ['https://magento.softwaretestingboard.com/',
                                      'https://magento.softwaretestingboard.com/women.html',
                                      'https://magento.softwaretestingboard.com/women/tops-women.html']
    BREADCRUMBS_LINKS_ON_PAGE_WOMEN_SALE = ['https://magento.softwaretestingboard.com/',
                                            'https://magento.softwaretestingboard.com/sale.html']


class ProductLocators:
    RADIANT_TEE_URL = 'https://magento.softwaretestingboard.com/radiant-tee.html'
    RADIANT_TEE_SIZE = '[option-label="XS"]'
    RADIANT_TEE_COLOR = '[option-label="Orange"]'
    RADIANT_TEE_QTY = '#qty'
    ADD_TO_CART_BUTTON = '#product-addtocart-button'

    ARGUS_All_WEATHER_TANK = '[alt="Argus All-Weather Tank"]'
    ARGUS_All_WEATHER_TANK_SIZE = '//*[@title="Argus All-Weather Tank"]/../..//*[@option-label="M"]'
    ARGUS_All_WEATHER_TANK_COLOR = '//*[@title="Argus All-Weather Tank"]/../..//*[@option-label="Gray"]'
    ARGUS_All_WEATHER_TANK_ADD_TO_CARD = '//*[@title="Argus All-Weather Tank"]/../..//*[@title="Add to Cart"]'
    MINI_BASKET_WINDOW = '.action.showcart'
    VIEW_AND_EDIT_CART_LINK = "//*[text()='View and Edit Cart']"
    VIEW_AND_EDIT_CART_HREF = "[class='action viewcart']"
    SEE_DETAILS = '[data-role="title"]'
    SIZE_M = '//*[@class="product options list"]//*[text()="M"]'
    COLOR_GRAY = '//*[@class="product options list"]//*[text()="Gray"]'
    NAME_ITEM = '//*[text()="Argus All-Weather Tank"]'
    PRICE_ITEM = '//*[@class="minicart-price"]//*[@class="price"]'
    CART_SUBTOTAL = '.subtotal .price'
    QTY_FIELD = ".details-qty input"
    UPDATE = '[title="Update"]'
    SIZE_XS = '#option-label-size-143-item-166'
    COLOR_BLUE = '#option-label-color-93-item-50'
    SHOULD_CHOOSE_SIZE_AND_COLOR = '.swatch-input super-attribute-select'
    TEXT_REQUIRED_FIELD = 'This is a required field.'

    NAME_ARGUS_ALL_WEATHER_TANK_CHECKOUT_CART = '//*[@id="shopping-cart-table"] //*[text()="Argus All-Weather Tank"]'
    SIZE_M_ARGUS_ALL_WEATHER_TANK_CHECKOUT_CART = '//*[contains(text(),"M")]/../..//*[@id="shopping-cart-table"]'
    COLOR_GRAY_ARGUS_CHECKOUT_CART = '//*[@id="shopping-cart-table"]//*[contains(text(),"Gray")]'
    PRICE_ITEM_CHECKOUT_CART = '//*[@class="col price"] //*[text()="$22.00"]'
    CART_SUBTOTAL_CHECKOUT_CART = '//*[@class="col subtotal"] //*[text()="$22.00"]'
    QTY_FIELD_CHECKOUT_CART = '[class="field qty"] input'
    MINICART_COUNTER = '.counter-label'


class ShoppingCart:
    ESTIMATE_SHIPPING = '//*[@id="block-shipping"]//*[@class="title"]'
    COUNTRY_SELECT_DROP = '//*[@class="field"]//*[@name="country_id"]'
    # COUNTRY_SELECT_DROP = '//*[@class="select"]'
    # SELECT_COUNTRY = '//*[@class="field"]//*[@name="country_id"]'
    STATE_REGION_SELECT = '//*[@class="field"]//*[@name="region_id"]'

    FLAT_RATE = '[data-bind="text: $data"]'
    SUBTOTAL_VAlUE = '[class="price"][data-th="Subtotal"]'
    ORDER_TOTAL_VALUE = '[data-bind="text: getValue()"]'
    PROCESEED_TO_CHECKOUT_BUTTON = '[data-role="proceed-to-checkout"]'


class HomeLocators:
    STORE_LOGO = 'a.logo'


class NavigatorLocators:
    NAV_NEW = '#ui-id-3'
    NAV_WOMEN = '#ui-id-4'
    NAV_MEN = '#ui-id-5'
    NAV_GEAR = '#ui-id-6'
    NAV_TRAINING = '#ui-id-7'
    NAV_SALE = '#ui-id-8'


class SideBarLocators:
    BREADCRUMBS = '.breadcrumbs'
    ITEM_HOME = '.item.home a'
    SIDEBAR_MAIN = '.sidebar.sidebar-main'
    CATEGORIES_MENU = '.categories-menu'
    FILTER = '.block.filter'


class BaseLocators:
    PAGE_NAME = ".base"
    PAGE_TITLE = 'h1'
    BREADCRUMBS_LIST = ".breadcrumbs li"
    BREADCRUMBS_LINKS = '.breadcrumbs > ul  > li > a'
    PRODUCT_ITEM_IN_CATALOG = 'li.product-item'  # каждый товар на любой странице в целом
    PRODUCT_PRICE = '.price-label'
    PRODUCT_NAME = '.product-item-link'
    PRODUCT_IMAGE = '.product-image-photo'
    ALL_URL = ["https://magento.softwaretestingboard.com/",
               "https://magento.softwaretestingboard.com/what-is-new.html",
               "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html,"
               "https://magento.softwaretestingboard.com/training.html"
               ]


class SearchTermsLocators:
    LINK_SEARCH_TERMS = "https://magento.softwaretestingboard.com/search/term/popular/"
    TERMS_FOR_SEARCH_LIST_QTY = '[class="item"]'
    LIST_OF_SEARCH_TERMS = '[class="item"] a'


class LoginLocators:
    LINK_LOGIN = 'https://magento.softwaretestingboard.com/customer/account/login'
    FIELD_NAME = 'div.login-container #email'
    FIELD_PASSWORD = 'div.login-container #pass'
    BUTTON_SUBMIT = 'div.login-container #send2'
    MESSAGE_UNSUCCESSFUL = '#pass-error'
    USER_NAME_IN_WELCOME = '.logged-in'
    AUTHORIZATION_LINK = 'authorization-link'
    LINK_ACCOUNT = 'https://magento.softwaretestingboard.com/customer/account/'


class PerformanceSportswear:
    LINK_SPORT = "https://magento.softwaretestingboard.com/collections/performance-new.html"
    BUTTON_ADD_ITEM2 = '#maincontent li:nth-child(2) button'
    SUCCESS_MESSAGE = '#maincontent > div.page.messages > div:nth-child(2) > div > div > div'
    TEXT_SUCCESS_MESSAGE = 'You added Helios Endurance Tank to your shopping cart'
    IMAGE_2 = '#maincontent ol > li:nth-child(2) .product-image-container'
    ITEM_2_IN_GENERAL = 'li.product-item:nth-child(2)'
