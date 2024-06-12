from playwright.sync_api import Page, expect


def test_checkbox(page: Page):
    page.goto('https://zimaev.github.io/checks-radios/')
    # page.pause()
    page.locator("text=Default checkbox").check()
    page.locator("text=Checked checkbox").check()
    page.locator("text=Default radio").check()
    page.locator("text=Default checked radio").check()
    page.locator("text=Checked switch checkbox input").check()


def test_checkbox2(page):
    page.goto('https://zimaev.github.io/checks-radios/')
    page.locator("text=Default checkbox").click()
    page.locator("text=Checked checkbox").click()
    page.locator("text=Default radio").click()
    page.locator("text=Default checked radio").click()
    page.locator("text=Checked switch checkbox input").click()


def test_checkbox_checking(page: Page):
    page.goto('https://zimaev.github.io/checks-radios/')
    # page.pause()
    page.locator('#flexCheckDefault').check()
    first = page.locator('#flexCheckDefault')
    expect(first).to_be_checked()

    page.locator("text=Checked checkbox").check()
    second = page.locator("text=Checked checkbox")
    expect(second).to_be_checked()

    page.locator("text=Default radio").click()
    third = page.locator("text=Default radio")
    expect(third).to_be_checked()

    page.locator("text=Default checked radio").click()
    fourth = page.locator("text=Default checked radio")
    expect(fourth).to_be_checked()

    page.locator("text=Checked switch checkbox input").click()
    switch = page.locator("text=Checked switch checkbox input")
    expect(switch).to_be_checked()
