import math
import time

from playwright.sync_api import Page, expect, Dialog, FileChooser


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


def test_select_222(page: Page):
    page.goto("https://suninjuly.github.io/selects1.html")
    page.on("dialog", handle_manage_alert)
    result = int(page.locator("#num1").inner_text()) + int(page.locator("#num2").inner_text())
    page.select_option("#dropdown", value=str(result))
    page.get_by_role("button", name="Submit").click()


def test_select_2_222(page: Page):
    page.goto("https://suninjuly.github.io/selects2.html")
    page.on("dialog", handle_manage_alert)
    result = int(page.locator("#num1").inner_text()) + int(page.locator("#num2").inner_text())
    page.select_option("#dropdown", value=str(result))
    page.get_by_role("button", name="Submit").click()


def test_upload_file(page: Page):
    page.goto("http://suninjuly.github.io/file_input.html")
    page.on("dialog", handle_manage_alert)
    page.get_by_placeholder("Enter first name").fill("Olga")
    page.get_by_placeholder("Enter last name").fill("Olga")
    page.get_by_placeholder("Enter email").fill("tb@gmail.com")
    page.locator('input[type="file"]').click()
    page.set_input_files('input[type="file"]', "test_file.txt")
    page.locator('button[type="submit"]').click()


def handle_file(file: FileChooser):
    file.set_files("test_file.txt")


def test_upload_file_2(page: Page):
    page.goto("http://suninjuly.github.io/file_input.html")
    page.on("dialog", handle_manage_alert)
    page.on("filechooser", handle_file)
    page.get_by_placeholder("Enter first name").fill("Olga")
    page.get_by_placeholder("Enter last name").fill("Olga")
    page.get_by_placeholder("Enter email").fill("tb@gmail.com")
    page.locator('input[type="file"]').click()
    page.locator('button[type="submit"]').click()








