import pytest
from playwright.sync_api import Page, FileChooser, expect


@pytest.mark.ok
def test_frame(page: Page):
    page.goto("https://testpages.eviltester.com/styled/frames/frames-test.html")
    expect(page.frame_locator("frame[name = 'middle']").locator("#middle8")).to_contain_text("Middle List Item 8")


@pytest.mark.ok
def test_left_frame(page: Page):
    page.goto("https://testpages.eviltester.com/styled/frames/frames-test.html")
    expect(page.frame_locator('frame[name="left"]').locator("#left0")).to_contain_text("Left List Item 0")
    expect(page.frame_locator('frame[name="left"]').locator("h1")).to_contain_text("Left")


@pytest.mark.ok
def test_iframe(page: Page):
    page.goto("https://testpages.eviltester.com/styled/iframes-test.html")
    expect(page.frame_locator('#thedynamichtml').locator('#iframe1')).to_be_visible()
    expect(page.frame_locator('#thedynamichtml').locator('li[id*="iframe"]')).to_have_count(60)
    expect(page.frame_locator('#theheaderhtml').locator('h1')).to_contain_text("example", ignore_case=True)
