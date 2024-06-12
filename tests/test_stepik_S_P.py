import math
import time

from playwright.sync_api import Page, expect, Dialog


def handle_manage_alert(d: Dialog):
    print("\n", d.message.split()[-1])
    d.accept()


def test_summ(page: Page):
    page.goto("https://suninjuly.github.io/selects1.html")
    page.on("dialog", handle_manage_alert)
    summ = int(page.locator("#num1").inner_text()) + int(page.locator("#num2").inner_text())
    page.select_option('#dropdown', label=str(summ))
    expect(page.locator(".btn.btn-default")).to_be_enabled()
    expect(page.locator(".btn.btn-default")).to_be_visible()
    page.locator(".btn.btn-default").click()





def test_abs(page: Page):
    page.goto("https://suninjuly.github.io/execute_script.html")
    page.on("dialog", handle_manage_alert)
    result = str(math.log(abs(12*math.sin(int(page.locator("#input_value").inner_text())))))
    page.evaluate("window.scrollBy(0, 150)")
    page.locator("#answer").fill(result)
    page.locator("#robotCheckbox").check()
    page.locator("#robotsRule").check()
    page.get_by_role("button", name="Submit").click()



