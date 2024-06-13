import pytest
from playwright.sync_api import Page


def test_drag_drop(page: Page):
    page.goto('https://letcode.in/draggable')
    page.locator("#sample-box").hover()
    page.mouse.down()
    page.mouse.move(300, 300, steps=10)
    page.mouse.up()


@pytest.mark.ok
def test_drag_to_target(page: Page):
    page.goto('https://letcode.in/dropable')
    page.drag_and_drop("#draggable", "#droppable")
