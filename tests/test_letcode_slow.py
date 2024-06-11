from playwright.sync_api import Page, expect
from selenium.webdriver import Keys

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

    text = second_input.input_value()
    print(text)
    print("hi")
    # page.pause()
