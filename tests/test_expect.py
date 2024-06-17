from playwright.sync_api import Page, expect

from utils.stepik import handle_stepik_alert, calc


def test_section2_lesson4_step8_expect(page: Page):
    page.goto('http://suninjuly.github.io/explicit_wait2.html')

    # expect(page.locator("#price")).to_contain_text("$100", timeout=20000)
    page.wait_for_selector("//h5[@id='price' and contains(text(),'$100')]")

    page.get_by_role("button", name="Book").click()

    x = page.locator("#input_value").inner_text()
    result = calc(x)
    page.locator("#answer").fill(result)

    page.on("dialog", handle_stepik_alert)

    page.get_by_role("button", name="Submit").click()
