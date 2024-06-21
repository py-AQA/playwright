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


def test_reminder(page_my: Page):
    page = page_my
    page.goto("https://apod-dev-d.osora.ru/employees/one/timesheet")
    page.get_by_text("Напоминания").click()
    page.get_by_text("+ добавить напоминание").click()


    page.get_by_placeholder("Комментарий").last.click()
    page.get_by_placeholder("Комментарий").last.fill("time")

    page.get_by_text("Зациклить").last.click()

    page.get_by_placeholder("Выберите дату").last.click()
    page.get_by_role("button", name="1 июня 2024 г.", exact=True).first.click()
    # page.get_by_placeholder("Выберите дату").nth(2).click()
    page.locator("li").filter(has_text="Зациклить«‹июнь 2024").locator("path").first.click()

    page.get_by_text("Выберите время").last.click()
    page.get_by_text("04:30").click()

    page.get_by_text("Сохранить").click()
    # page.pause()
    expect(page.locator('[testid="alertTitle"]')).to_have_text("Успех")
    page.get_by_text("Принять").click()

