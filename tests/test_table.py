import time

from playwright.sync_api import Page, expect


def test_checkbox(page: Page):
    page.goto('https://devexpress.github.io/devextreme-reactive/react/grid/docs/guides/filtering/')
    # page.pause()
    page.frame_locator("iframe >> nth=0").get_by_placeholder("Filter...").first.fill("l")

    next_row = page.frame_locator("iframe >> nth=0").locator("tr:below(span:text('Name'))")
    [[print(item.inner_text()) for item in next_row.nth(i).all()] for i in range(next_row.count())]
    # expect(next_row).to_have_count(1)

    # next_row = page.locator("tr:right-of(th:text('Name'))")
    # print(next_row.all_inner_texts())