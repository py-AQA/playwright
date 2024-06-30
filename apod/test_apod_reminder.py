import json

from playwright.sync_api import expect, Page, Request

from apod.apod_calendar import ApodCalendar


def h_request(request: Request):
    print(request.method, request.url, request.post_data)
    # if request.post_data:
    #     print(json.loads(request.post_data))


def test_add_default_reminder(page_my: Page):
    """Выбрать одну дату"""
    page_my.goto("https://apod-dev-d.osora.ru/employees/one/timesheet")
    page_my.on("request", h_request)

    page_my.get_by_text("Напоминания").click()

    page_my.get_by_text("+ добавить напоминание").click()

    page_my.get_by_placeholder("Комментарий").last.fill("comment here")
    # page_my.get_by_placeholder("Комментарий").last.clear()
    # page_my.get_by_text("Зациклить").last.click()
    # page_my.pause()

    # page_my.get_by_placeholder("Выберите дату").first.click()
    # ApodCalendar(page_my.get_by_placeholder("Выберите дату").first).set_date('2019-07-27')
    # page_my.pause()

    page_my.get_by_text("Выберите время").last.click()
    page_my.get_by_text("22:30").click()
    page_my.pause()

    page_my.get_by_text("Сохранить").click()
    expect(page_my.locator('[testid="alertTitle"]')).to_have_text("Успех")
    page_my.get_by_text("Принять").click()


def test_add_last_reminder(page_my: Page):
    """Выбрать одну дату"""
    page_my.goto("https://apod-dev-d.osora.ru/employees/one/timesheet")
    page_my.on("request", h_request)

    page_my.get_by_text("Напоминания").click()


    page_my.get_by_placeholder("Комментарий").last.fill("comment here")

    page_my.get_by_text("Зациклить").last.click()

    page_my.get_by_placeholder("Выберите дату").first.click()
    ApodCalendar(page_my.get_by_placeholder("Выберите дату").first).set_date('2019-07-27')
    page_my.pause()

    # page_my.get_by_text("Выберите время").last.click()
    # page_my.get_by_text("23:30").click()

    page_my.get_by_text("Сохранить").click()
    expect(page_my.locator('[testid="alertTitle"]')).to_have_text("Успех")
    page_my.get_by_text("Принять").click()
