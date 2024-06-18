from playwright.sync_api import Page, expect

from utils.stepik import handle_stepik_alert, calc


def test_section2_lesson4_step8_wait_for_selector(page: Page):
    page.goto('http://suninjuly.github.io/explicit_wait2.html')

    page.wait_for_selector("//h5[@id='price' and contains(text(),'$100')]")

    page.get_by_role("button", name="Book").click()

    page.locator("#answer").fill(calc(page.locator("#input_value").inner_text()))

    page.on("dialog", handle_stepik_alert)
    # TODO why page is freezing for some time on submit
    page.get_by_role("button", name="Submit").click()


def test_section2_lesson4_step8_expect_to_contain(page: Page):
    page.goto('http://suninjuly.github.io/explicit_wait2.html')

    # TODO set lower polling interval for expect
    expect(page.locator("#price")).to_contain_text("$100", timeout=20000)

    page.get_by_role("button", name="Book").click()

    page.locator("#answer").fill(calc(page.locator("#input_value").inner_text()))

    page.on("dialog", handle_stepik_alert)
    # TODO why page is freezing for some time on submit
    page.get_by_role("button", name="Submit").click()
