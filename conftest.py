import json

import pytest
from playwright.sync_api import sync_playwright, Page, Route, Request


@pytest.fixture(scope="session")
def browser_context_args():
    return {
        # "record_video_dir": "videos/",
        # "record_video_size": {"width": 640, "height": 480},
        "viewport": {"width": 1280, "height": 1024}
        # "viewport": {
        #     "width": 1920,
        #     "height": 1080,
        # }
    }


def handle_login_via_telegram(route, response):
    print(">>> login attempt")
    route.fulfill(status=200, json={"token": 666, "isFirstUser": True})


def handle_get_timezone_list(route, response):
    route.fulfill(status=200, json={"id1": {"timezone": "europe/one"}, "id2": {"timezone": "europe/two"}})


def handle_post_timezone(route, response):
    route.fulfill(status=200, json={"aaaaaaaa": "aaaaa"})


def handle_set_settings(request: Request):
    if request.url.endswith("company/settings") and request.post_data:
        print(">>> company/settings", request.post_data)
        # assert "26.07.2019" in json.loads(request.post_data)["weekendsDays"]
        # assert "18.06.2024" in json.loads(request.post_data)["workingDays"]


def handle_get_settings(route, response):
    route.fulfill(status=200, json={
        "settings": {"availableMinutesLate": 15, "workingDays": ["18.06.2024", "19.06.2024"],
                     "weekendsDays": ["21.06.2024", "27.07.2019"],
                     "locations": [{"name": "name1", "latitude": 1, "longitude": 2, "radius": 3}], "schedule": "5-2",
                     "weekendsType": "customWeekends",
                     "timeSchedules": [{"id": "aMU2s5Sf", "label": "02:00-05:30", "selected": False},
                                       {"id": "x3waPrVE", "label": "02:00-05:30", "selected": False},
                                       {"id": "cdPN6eDa", "label": "02:00-05:30", "selected": False},
                                       {"id": "VyPmDLMz", "label": "02:00-01:00", "selected": False}],
                     "createdTimeSchedules": [{"id": "aMU2s5Sf", "label": "02:00-05:30", "selected": False},
                                              {"id": "x3waPrVE", "label": "02:00-05:30", "selected": False},
                                              {"id": "cdPN6eDa", "label": "02:00-05:30", "selected": False},
                                              {"id": "VyPmDLMz", "label": "02:00-01:00", "selected": False}],
                     "defaultTimeSchedule": None, "monthMaxOverwork": "16", "dayMaxOverwork": "17",
                     "vacationDays": "17", "vacationPeriod": "19", "maxAbsenceDays": "20", "deletedLocations": [],
                     "updatedLocations": [], "createdLocations": []}})


def handle_get_messages(route, response):
    route.fulfill(status=200, json={
        "data": [{"id": 1, "title": "title1", "text": "t1"},
                 {"id": 2, "title": "title2", "text": "t2"},
                 {"id": 3, "title": "title3", "text": "t3"}]})


def handle_get_employees(route, response):
    route.fulfill(status=200, json={
        "employees": [
            {"id": "one",
             "companyId": "company",
             "companyWorkplaces": [{"name": "name1", "latitude": 1, "longitude": 2, "radius": 3}],
             "fullName": "fullname one",
             "paymentSystem": "hourly",
             "schedule": "2-2",
             "specialization": "spec",
             "urlTG": "urltg"},
            {"id": "two",
             "companyId": "company",
             "companyWorkplaces": [{"name": "name1", "latitude": 1, "longitude": 2, "radius": 3}],
             "fullName": "fullName two",
             "paymentSystem": "hourly",
             "schedule": "2-2",
             "specialization": "spec",
             "urlTG": "urltg"},
            {"id": "three",
             "companyId": "company",
             "companyWorkplaces": [{"name": "name1", "latitude": 1, "longitude": 2, "radius": 3}],
             "fullName": "fullName three",
             "paymentSystem": "hourly",
             "schedule": "customSchedule",
             "specialization": "spec",
             "urlTG": "urltg"}
        ]})


def handle_bonus(route, response):
    route.fulfill(status=200, json={"bonus": "bonus"})


def handle_hourly(route, response):
    route.fulfill(status=200, json={"salary": "hourly"})


def handle_monthly(route, response):
    route.fulfill(status=200, json={"salary": "monthly"})


def handle_urltg(route, response):
    route.fulfill(status=200, json={"urltg": "urltg"})


def handle_schedule(route, response):
    route.fulfill(status=200, json={"workingDays": ["18.06.2024", "19.06.2024"]})


def handle_one(route, response):
    route.fulfill(status=200, json={"employee": {
        "id": "one",
        "username": "@sbdfkjsd1",
        "companyId": "company",
        "employmentDate": "2024-07-04",
        "exitDate": "2024-07-18",
        "workingDays": ["18.06.2024", "19.06.2024"],
        "companyWorkplaces": [{"id": "aMU2s5Sf", "name": "name1", "latitude": 1, "longitude": 2, "radius": 3},
                              {"id": "aMU2s6Sf", "name": "location1", "latitude": 1, "longitude": 2, "radius": 3}],
        "fullName": "full name above for user one",
        "timeSchedule": [{"id": "aMU3s5Sf", "label": "02:00-05:30", "selected": False}],
        "schedule": ["2-2"],
        "schedules": ["2-2"],
        "roleId": "Admin",
        "roles": [{"id": 0, "title": "Role title 1"}],
        "paymentSystem": None,
        "confirmGeo": True,
        "specialization": "spec",
        "information": ["item two", "item two", "item two", "item two", "item two"],
        "locations": [{"id": "aMU2s5Sf", "name": "name1"}],
        "endAt": "11:11",
        "urlTG": "urltg"}})


def handle_two(route, response):
    route.fulfill(status=200, json={"employee": {
        "id": "two",
        "username": "@sbdfkjsd2",
        "companyId": "company",
        "employmentDate": "2024-07-04",
        "exitDate": "2024-07-18",
        "workingDays": ["18.06.2024", "19.06.2024"],
        "companyWorkplaces": [{"id": "aMU1s6Sf", "name": "name1", "latitude": 1, "longitude": 2, "radius": 3},
                              {"id": "aMU2s6Sf", "name": "location1", "latitude": 2, "longitude": 2, "radius": 3},
                              {"id": "aMU3s6Sf", "name": "location2", "latitude": 3, "longitude": 2, "radius": 3}],
        "fullName": "fntwo",
        "timeSchedule": [{"id": "aMU3s5Sf", "label": "02:00-05:30", "selected": False}],
        "schedule": ["2-2"],
        "schedules": ["2-2"],
        "roleId": 2,
        "roles": [{"id": 1, "title": "title1"}],
        "paymentSystem": "monthly",
        "confirmGeo": False,
        "specialization": "spec",
        "information": ["item one", "item two"],
        "locations": [],
        "endAt": "12:22",
        "urlTG": "urltg"}})


def handle_3(route, response):
    route.fulfill(status=200, json={"employee": {
        "id": "three",
        "username": "@sbdfkjsd3",
        # "companyId": "company",
        "employmentDate": "2024-07-04",
        "exitDate": "2024-07-18",
        # "workingDays": ["18.06.2024", "19.06.2024"],
        "companyWorkplaces": [
            {"id": "100", "name": "name1", "title": "you", "latitude": 1, "longitude": 2, "radius": 3},
            {"id": "200", "name": "location1", "latitude": 2, "longitude": 2, "radius": 3},
            {"id": "300", "name": "location2", "latitude": 3, "longitude": 2, "radius": 3}],
        "fullName": "full name three above",

        "schedule": [
            {"id": 1, "label": "08:00-10:00"},
            {"id": 2, "label": "13:00-15:00"},
            {"id": 3, "label": "16:00-18:00"}
        ],

        "roleId": 3,
        "roles": [{"id": 0, "title": "title0"},
                  {"id": 1, "title": "title1"},
                  {"id": 2, "title": "title2"},
                  {"id": 3, "title": "title3"}],

        # "paymentSystem": "hourly",
        "specialization": "spec three above",
        "information": ["item one", "item two", "item two", "item two", "item two", "item two", "item two", "item two"],
        "locations": [{"id": "100", "name": "name1"}, {"id": "200", "name": "location1"}],
        "confirmGeo": True,
        "endAt": "12:33",
        # "urlTG": "urltg"
    }})


def handle_archive(route, response):
    route.fulfill(status=200, json={
        "title_of_period": [
            {"type": "Отгул", "period": "2024-06-21"},
            {"type": "Отгул", "period": "2024-06-22"},
            {"type": "Отгул", "period": "2024-07-22"}
        ],
        "title_of_period_two": [
            {"type": "Отгул", "period": "2023-06-21"},
            {"type": "Отгул", "period": "2023-06-22"},
            {"type": "Отгул", "period": "2023-07-22"}
        ],
        "title_of_period_three": [
            {"type": "Отгул", "period": "2023-06-21"},
            {"type": "Отгул", "period": "2023-06-22"},
            {"type": "Отгул", "period": "2023-07-22"}
        ]
    })


def handle_statistic(route, response):
    route.fulfill(status=200, json=[{"period": "", "label": "", "day": ""}])


def handle_reminder(route, response):
    route.fulfill(status=200, json={"reminders": [
        {"comment": "first reminder", "reminderDate": "2024-06-20", "reminderTime": "23:30", "loop": False},
        {"comment": "second reminder", "reminderDate": "2024-06-21", "reminderTime": "23:30", "loop": True},
        # {"status": "status", "comment": "string", "date": "string", "startAt": "string", "endAt": "string", "minutesLate": 12},
        # {"loop": True, "reminderDate": "", "reminderTime": "11:11"}
    ]})


def handle_store(route, response):
    route.fulfill(status=200, json={"ok": "ok"})


def handle_timesheet_search(route, response):
    route.fulfill(status=200, json={"ok": "ok"})


def handle_update(route, response):
    route.fulfill(status=200, json={"ok": "ok"})


def handle_absence(route, response):
    route.fulfill(status=200, json={"dates": ["2024-01-01", "2024-02-01"]})


def handle_absence_common(route, response):
    route.fulfill(status=200, json={"dates": ["2024-01-01", "2024-02-01", "2024-03-01"]})


def handle_absence_common_closest(route, response):
    route.fulfill(status=200, json={"dates": ["2024-01-01", "2024-02-01", "2024-03-01"]})


def handle_absence_medical_closest(route, response):
    route.fulfill(status=200, json={"dates": ["2023-01-01", "2023-02-01", "2023-03-01"]})


def handle_absence_medical(route, response):
    route.fulfill(status=200, json={"dates": ["2024-01-01", "2024-02-01", "2024-03-01"]})


def handle_timesheet(route, response):
    route.fulfill(status=200, json={"timesheet": [
        {"id": "on0", "date": "2024-01-01", "status": "Прогул", "startAt": "03:57", "endAt": "03:58", "comment": "c1"},
        {"id": "on1", "date": "2024-01-01", "status": "Отгул", "startAt": "04:57", "endAt": "04:58", "comment": "c2"},
        {"id": "on2", "date": "2024-01-01", "status": "Больничный", "startAt": "05:57", "endAt": "06:00", "comment": "c3"},
        {"id": "on3", "date": "2024-01-01", "status": "На pаботе", "startAt": "07:57", "endAt": "08:58", "comment": "c4"},
        {"id": "on3", "date": "2025-01-01", "status": "На pаботе", "startAt": "07:57", "endAt": "08:58",
         "comment": "c5"},
        {"id": "on3", "date": "2026-01-01", "status": "На pаботе", "startAt": "07:57", "endAt": "08:58",
         "comment": "c6"},
    ]})


def handle_vacation_closest(route, response):
    route.fulfill(status=200, json={"dates": ["2024-01-01", "2024-02-01", "2024-03-01"]})


def handle_export(route, response):
    route.fulfill(status=200, json={"export": "export"})


def on_web_socket(ws):
    print(f"WebSocket opened: {ws.url}")
    ws.on("framesent", lambda payload: print("Frame sent:", payload))
    ws.on("framereceived", lambda payload: print("Frame received:", payload))
    ws.on("close", lambda payload: print("WebSocket closed"))


@pytest.fixture
def page_my() -> Page:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(
            locale='ru-RU'
        )

        context.route("**/api/admin-panel/login-via-telegram/apod-dev-d", handle_login_via_telegram)

        context.route("**/api/admin-panel/timezone-list*", handle_get_timezone_list)
        context.route("**/api/admin-panel/timezone", handle_post_timezone)

        context.route("**/api/admin-panel/company/settings", handle_set_settings)
        context.route("**/api/admin-panel/company/settings", handle_get_settings)
        context.route("**/api/admin-panel/company/settings/messages", handle_get_messages)

        context.route("**/api/admin-panel/employees", handle_get_employees)
        context.route("**/api/admin-panel/employees?search=*", handle_get_employees)

        context.route("**/api/admin-panel/employees/csv", handle_export)
        context.route("**/api/admin-panel/employees/one", handle_one)
        context.route("**/api/admin-panel/employees/two", handle_two)
        context.route("**/api/admin-panel/employees/three", handle_3)

        context.route("**/api/admin-panel/employees/urltg", handle_urltg)
        context.route("**/api/admin-panel/employees/*/schedule/working-days", handle_schedule)
        context.route("**/api/admin-panel/employees/*/archive", handle_archive)
        context.route("**/api/admin-panel/employees/*/statistic?*", handle_statistic)
        context.route("**/api/admin-panel/employees/*/reminder", handle_reminder)
        context.route("**/api/admin-panel/employees/*/timesheet/*/store", handle_store)
        context.route("**/api/admin-panel/employees/*/timesheet?search=*", handle_timesheet_search)

        context.route("**/api/admin-panel/employees/*/update", handle_update)

        context.route("**/api/admin-panel/employees/*/absence", handle_absence)
        context.route("**/api/admin-panel/employees/*/absence/common", handle_absence_common)
        context.route("**/api/admin-panel/employees/*/absence/common/closest", handle_absence_common_closest)
        context.route("**/api/admin-panel/employees/*/absence/medical/closest", handle_absence_medical_closest)
        context.route("**/api/admin-panel/employees/*/absence/medical", handle_absence_medical)

        context.route("**/api/admin-panel/employees/*/timesheet", handle_timesheet)

        context.route("**/api/admin-panel/employees/*/payment/bonus", handle_bonus)
        context.route("**/api/admin-panel/employees/*/payment/hourly", handle_hourly)
        context.route("**/api/admin-panel/employees/*/payment/monthly", handle_monthly)

        context.route("**/api/admin-panel/employees/*/vacation/closest", handle_vacation_closest)

        context.add_init_script("localStorage.setItem('accessToken', '{\"token\": 777}')")
        context.add_init_script("localStorage.setItem('isFirstUser', true)")

        page = context.new_page()
        # page.on("websocket", on_web_socket)
        page.on("request", handle_set_settings)

        yield page
        page.close()
        browser.close()
