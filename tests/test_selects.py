import pytest
from playwright.sync_api import Page, expect

from utils.stepik import handle_stepik_alert


@pytest.mark.ok
def test_section2_lesson2_step3_select_by_label(page: Page):
    page.on("dialog", handle_stepik_alert)

    page.goto("https://suninjuly.github.io/selects1.html")

    summ = int(page.locator("#num1").inner_text()) + int(page.locator("#num2").inner_text())
    page.select_option('#dropdown', label=str(summ))
    expect(page.locator(".btn.btn-default")).to_be_enabled()
    expect(page.locator(".btn.btn-default")).to_be_visible()

    page.locator(".btn.btn-default").click()


@pytest.mark.ok
def test_section2_lesson2_step3_select_by_value(page: Page):
    page.on("dialog", handle_stepik_alert)

    page.goto("https://suninjuly.github.io/selects1.html")

    result = int(page.locator("#num1").inner_text()) + int(page.locator("#num2").inner_text())
    page.select_option("#dropdown", value=str(result))

    page.get_by_role("button", name="Submit").click()


@pytest.mark.ok
def test_section2_lesson2_step3_select_by_value_on_page_selects2(page: Page):
    page.on("dialog", handle_stepik_alert)

    page.goto("https://suninjuly.github.io/selects2.html")

    result = int(page.locator("#num1").inner_text()) + int(page.locator("#num2").inner_text())
    page.select_option("#dropdown", value=str(result))

    page.get_by_role("button", name="Submit").click()
