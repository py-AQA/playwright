from playwright.sync_api import Page, expect

main_page_link = "https://magento.softwaretestingboard.com"


def add_item(page: Page, name_item, size, color):
    page.locator("ol div").filter(has_text="name_item")
    # print(page.locator("ol div").filter(has_text=name_item).get_by_label(size).last.get_attribute("outerHTML"))

    page.locator("ol div").filter(has_text=name_item).get_by_label(size).last.click()
    page.locator("ol div").filter(has_text=name_item).get_by_label(color).click()
    # page.pause()
    page.locator("ol div").filter(has_text=name_item).get_by_role("button").click()


def add_qty(page: Page, qty_items):
    qty_counter = page.locator('//*[@class="counter-number"]')
    # print(qty_items, type(qty_items))
    expect(qty_counter).to_have_text(qty_items)
