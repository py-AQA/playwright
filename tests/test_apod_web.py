import re

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
    page.locator("li").filter(has_text="Зациклить«‹июнь 2024").locator("path").first.click()

    page.get_by_text("Выберите время").last.click()
    page.get_by_text("04:30").click()

    page.get_by_text("Сохранить").click()
    expect(page.locator('[testid="alertTitle"]')).to_have_text("Успех")
    page.get_by_text("Принять").click()


def test_main_settings(page_my: Page):
    page = page_my
    page.goto("https://apod-dev-d.osora.ru/settings")
    page.get_by_text("Стандартный по РФ").click()
    page.get_by_text("Индивидуально").click()
    page.get_by_role("button", name="3 июня 2024 г.", exact=True).click()
    page.get_by_role("button", name="10 июня 2024 г").click()
    page.get_by_text("Сохранить").nth(1).click()
    page.locator("div").filter(has_text=re.compile(r"^Начало рабочего дняВыберите время$")).locator("div").click()
    page.get_by_text("06:00").click()
    page.locator("div").filter(has_text=re.compile(r"^Выберите время$")).locator("svg").click()
    page.get_by_text("00:00").click()
    page.locator('(//*[@data-icon="circle-plus"])[1]').click()
    page.locator("input[name=\"availableMinutesLate\"]").fill("70")
    page.locator("input[name=\"monthMaxOverwork\"]").fill("800")
    page.locator("input[name=\"dayMaxOverwork\"]").fill("25")
    page.locator("input[name=\"vacationDays\"]").fill("-1")
    page.locator("input[name=\"vacationPeriod\"]").fill("13")
    page.locator("input[name=\"maxAbsenceDays\"]").fill("33")
    page.locator("input[name=\"nameundefined\"]").fill("Станок 1")
    page.locator("input[name=\"latitudeundefined\"]").fill("12.021")
    page.locator("input[name=\"longitudeundefined\"]").fill("22.235")
    page.locator("input[name=\"radiusundefined\"]").fill("32.251")
    page.get_by_text("Сохранить").click()

    expect(page.locator('[testid="alertSubtitle"]')).to_have_text("Настройки сохранены")


def test_employees_one_page(page_my: Page):
    page = page_my
    page.goto('https://apod-dev-d.osora.ru/employees/one')
    page.get_by_label("Close").click()

    page.get_by_placeholder("@tgnickname").click()
    page.get_by_placeholder("@tgnickname").fill("@Grom-Zadira")
    page.get_by_placeholder("ФИО").fill("За орду!")
    page.get_by_placeholder("Должность").fill("Нужно больше Золота!")
    page.get_by_placeholder("Дата трудоустройства").fill("2022-02-23")
    page.get_by_placeholder("Дата выхода").fill("2024-06-23")
    page.locator('[placeholder="Время окончания смены"]').click()
    page.locator('div:nth-child(7) > div:nth-child(2) > input').type("1745")
    page.get_by_role("link", name="Сохранить").click()
    # page.pause()
