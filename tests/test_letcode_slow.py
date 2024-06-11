import time

from playwright.sync_api import Page, expect


base_url = 'https://letcode.in/radio'


def test_radiobutton(page: Page):
    page.goto(base_url)
    # page.wait_for_timeout(3000)
    page.locator("#one").check()
    page.locator("#two").check()
    # page.get_by_label("Remember me").uncheck()
    radio_loct = page.locator("#two")
    expect(radio_loct).to_be_checked()


def test_edit_button(page: Page):
    page.goto('https://letcode.in/edit')
    input = page.locator("//input[@id='fullName']")
    expect(input).to_be_editable()
    input.fill("Test")
    second_input = page.locator("#join")
    expect(second_input).to_be_visible()
    expect(second_input).not_to_be_empty()
    second_input.press("End")
    second_input.type(" new")
    second_input.press("Tab")
    expect(page.locator("#getMe")).to_have_value("ortonikc")
    page.locator("#clearMe").clear()
    expect(page.locator("#clearMe")).to_be_empty()
    expect(page.locator("#noEdit")).to_be_disabled()
    expect(page.locator("#dontwrite")).not_to_be_editable()


def test_drag_drop(page: Page):
    page.goto('https://letcode.in/draggable')
    page.locator("#sample-box").hover()
    page.mouse.down()
    page.mouse.move(300, 300, steps=10)
    page.mouse.up()
    time.sleep(5)


def test_drag_to_target(page: Page):
    page.goto('https://letcode.in/dropable')
    page.drag_and_drop("#draggable", "#droppable")







