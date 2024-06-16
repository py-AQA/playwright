import pytest
from playwright.sync_api import Page, Download, expect, Position


def test_slider(page: Page):
    # целое или 0.5 только / через ввод числа непосредственно
    page.goto("https://the-internet.herokuapp.com/horizontal_slider")
    # page.pause()
    page.get_by_role("slider").fill("3")


def test_slider2(page: Page):
    # целое или 0.5 только. 90pcs = 3.5 / перемещение по пикселям
    page.goto("https://the-internet.herokuapp.com/horizontal_slider")
    # page.pause()
    page.locator('[type="range"]').click(position=Position(x=90, y=0))
    page.pause()


def test_slider3(page: Page):
    # целое или 0.5 только. 90pcs = 3.5 / не работает
    page.goto("https://the-internet.herokuapp.com/horizontal_slider")
    page.locator('[type="range"]').click(position=Position(x=90, y=0))
    page.locator('[type="range"]').hover(position=Position(x=30, y=0))
    # page.mouse.click(300, 300, delay=50, button="right")
    page.locator('[type="range"]').click()
    page.pause()


def test_hover(page: Page):
    page.goto("https://the-internet.herokuapp.com/hovers")
    page.get_by_role("img", name="User Avatar").nth(1).hover()
    expect(page.get_by_text("name: user2")).to_be_visible()
    # page.pause()


def test_shadow_root(page:Page):
    page.goto("https://the-internet.herokuapp.com/shadowdom")
    page.get_by_text("In a list!").click()
    expect(page.get_by_text("In a list!")).to_be_visible()


def test_shadow_root2(page:Page):
    page.goto("https://the-internet.herokuapp.com/shadowdom")
    page.locator('//*[@id="content"]/my-paragraph[2]/ul/li[2]').click()
    expect(page.get_by_text("In a list!")).to_be_visible()

