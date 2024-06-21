from playwright.sync_api import Page, expect


def test_pause(page_my: Page):
    page_my.goto("https://apod-dev-d.osora.ru/employees/one/calendar")
    page_my.pause()


def test_main(page_my: Page):
    page_my.goto("https://apod-dev-d.osora.ru/")
    expect(page_my.locator("div#__next>div>span")).to_contain_text("Выберите часовой пояс компании")


def test_timezone_select(page_my: Page):
    page_my.goto("https://apod-dev-d.osora.ru/timezone")
    expect(page_my.locator("div#__next>div>span")).to_contain_text("Выберите часовой пояс компании")


def test_bot_messages(page_my: Page):
    page_my.goto("https://apod-dev-d.osora.ru/settings/messages")
    expect(page_my.locator("div#__next nav").first).to_contain_text("СотрудникиНастройкиАналитика")
