import pytest
from playwright.sync_api import expect
from playwright.sync_api import Page, Dialog

from utils.stepik import handle_stepik_alert, calc


@pytest.mark.ok
def test_alert_robot(page: Page):
    page.goto('https://suninjuly.github.io/alert_accept.html')

    page.once("dialog", lambda dialog: print("one time allert <", dialog.message, "> accepted") or dialog.accept())
    page.get_by_role("button", name="I want to go on a magical").click()

    page.locator("#answer").fill(calc(page.locator("#input_value").inner_text()))

    page.once("dialog", handle_stepik_alert)
    page.get_by_role("button", name="Submit").click()


@pytest.mark.ok
def test_section2_lesson3_step6_redirect(page: Page):
    page.goto('https://suninjuly.github.io/redirect_accept.html')

    with page.context.expect_page() as tab:
        page.get_by_role("button", name="I want to go on a magical journey!").click(force=True)

    new_tab = tab.value
    expect(new_tab).to_have_url("https://suninjuly.github.io/redirect_page.html?")

    new_tab.on("dialog", handle_stepik_alert)

    new_tab.locator("#answer").fill(calc(new_tab.locator("#input_value").inner_text()))

    new_tab.get_by_role("button", name="Submit").click()
