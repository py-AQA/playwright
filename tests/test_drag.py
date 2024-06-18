import pytest
from playwright.sync_api import Page


@pytest.mark.ok
def test_drag_drop(page: Page):
    page.goto('https://letcode.in/draggable')
    box_draggable = page.locator("#sample-box").bounding_box()
    abs_x = box_draggable['x'] + box_draggable['width'] / 2
    abs_y = box_draggable['y'] + box_draggable['height'] / 2
    page.mouse.move(abs_x, abs_y)
    page.mouse.down()
    page.mouse.move(abs_x + 50, abs_y + 50, steps=300)
    page.mouse.up()


@pytest.mark.ok
def test_drag_to_target(page: Page):
    page.goto('https://letcode.in/dropable')
    page.drag_and_drop("#draggable", "#droppable")
