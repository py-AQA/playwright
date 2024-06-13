import pytest
from playwright.sync_api import Page

from utils.stepik import handle_stepik_alert, calc


@pytest.mark.ok
def test_section2_lesson2_step6_windows_scroll_by_execute_js_script(page: Page):
    page.on("dialog", handle_stepik_alert)

    page.goto("https://suninjuly.github.io/execute_script.html")

    page.locator("#answer").fill(calc(page.locator("#input_value").inner_text()))
    page.locator("#robotCheckbox").check()
    page.locator("#robotsRule").check()

    # + is scrolling to bottom of page, - to the top
    # page.evaluate("window.scrollBy(0, 100);")  # same as browser.execute_script("window.scrollBy(0, 100);")
    # page.mouse.wheel(0, 100)
    # page.get_by_role("button", name="Submit").scroll_into_view_if_needed()

    page.get_by_role("button", name="Submit").click()
