import math
import time

from playwright.sync_api import Page, expect, Dialog, FileChooser


def test_find_the_sum(page: Page):
    page.goto("https://suninjuly.github.io/selects1.html")
    # page.pause()
    num_1 = page.locator('id="num1"')
    num_2 = page.locator('id="num2"')
    result =int()