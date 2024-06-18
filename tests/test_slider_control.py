import pytest
from playwright.sync_api import Page, expect, Position


@pytest.mark.ok
def test_slider_by_fill(page: Page):
    # целое или 0.5 только / через ввод числа непосредственно
    page.goto("https://the-internet.herokuapp.com/horizontal_slider")
    # page.pause()
    page.get_by_role("slider").fill("3")
    expect(page.locator("#range")).to_contain_text("3")


@pytest.mark.ok
def test_slider_by_click_with_position(page: Page):
    # целое или 0.5 только. 90pcs = 3.5 / перемещение по пикселям
    page.goto("https://the-internet.herokuapp.com/horizontal_slider")

    width = page.locator('[type="range"]').bounding_box()["width"]
    print("slider width", width, "px")
    page.locator('[type="range"]').click(position=Position(x=width / 3, y=0))

    expect(page.locator("#range")).to_contain_text("1.5")


@pytest.mark.ok
def test_slider_drag_with_mouse(page: Page):
    # целое или 0.5 только. 90pcs = 3.5
    page.goto("https://the-internet.herokuapp.com/horizontal_slider")

    page.locator('[type="range"]').click(position=Position(x=90, y=0))
    expect(page.locator("#range")).to_contain_text("3.5")

    page.locator('[type="range"]').click(position=Position(x=0, y=0))
    expect(page.locator("#range")).to_contain_text("0")

    slider = page.locator('[type="range"]').bounding_box()
    page.mouse.move(slider["x"], slider["y"])
    page.mouse.down()
    page.mouse.move(slider["x"] + slider["width"], slider["y"], steps=200)
    page.mouse.up()
    expect(page.locator("#range")).to_contain_text("5")