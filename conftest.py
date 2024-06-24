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
        assert "27.07.2019" in json.loads(request.post_data)["weekendsDays"]
        assert "17.06.2020" in json.loads(request.post_data)["workingDays"]


def handle_get_settings(route, response):
    route.fulfill(status=200, json={
        "settings": {"availableMinutesLate": 15, "workingDays": ["18.06.2024", "19.06.2024"],
                     "weekendsDays": ["21.06.2024"],
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
            {"id": "one", "companyId": "company", "companyWorkplaces": None, "fullName": "fnone",
             "specialization": "spec", "urlTG": "urltg"},
            {"id": "two", "companyId": "company", "companyWorkplaces": None, "fullName": "fntwo",
             "specialization": "spec", "urlTG": "urltg"}
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
    route.fulfill(status=200, json={"schedule": "schedule"})


def handle_one(route, response):
    route.fulfill(status=200, json={"one": "one"})


def handle_two(route, response):
    route.fulfill(status=200, json={"two": "two"})


def handle_archive(route, response):
    route.fulfill(status=200, json={"archive": "archive"})


def handle_statistic(route, response):
    route.fulfill(status=200, json=[{"period": "", "label": "", "day": ""}])


def handle_reminder(route, response):
    route.fulfill(status=200, json={"reminders": [
        {"status": "status", "comment": "string", "date": "string", "startAt": "string", "endAt": "string",
         "minutesLate": 12},
        {"loop": True, "reminderDate": "", "reminderTime": "11:11"}]})


def handle_store(route, response):
    route.fulfill(status=200)


def handle_timesheet_search(route, response):
    route.fulfill(status=200)


def handle_absence(route, response):
    route.fulfill(status=200, json={"absence": "absence"})


def handle_absence_common(route, response):
    route.fulfill(status=200, json={"absence_common": "absence_common"})


def handle_absence_common_closest(route, response):
    route.fulfill(status=200, json={"common_absence": "common_absence"})


def handle_absence_medical_closest(route, response):
    route.fulfill(status=200, json={"medical_absence_closest": "medical_absence_closest"})


def handle_absence_medical(route, response):
    route.fulfill(status=200, json={"medical_absence": "medical_absence"})


def handle_timesheet(route, response):
    route.fulfill(status=200, json={"timesheet": [
        {"id": "one", "date": "2024-01-01", "status": "Прогул", "endAt": "04:58", "comment": "comment1",
         "startAt": "03:57"},
        {"id": "two", "date": "2024-01-02", "status": "Отгул", "endAt": "04:58", "comment": "comment2",
         "startAt": "03:57"}]})


def handle_vacation_closest(route, response):
    route.fulfill(status=200, json={"vacation_closest": "vacation_closest"})


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
        context = browser.new_context()

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

        context.route("**/api/admin-panel/employees/urltg", handle_urltg)
        context.route("**/api/admin-panel/employees/*/schedule/working-days", handle_schedule)
        context.route("**/api/admin-panel/employees/*/archive", handle_archive)
        context.route("**/api/admin-panel/employees/*/statistic?*", handle_statistic)
        context.route("**/api/admin-panel/employees/*/reminder", handle_reminder)
        context.route("**/api/admin-panel/employees/*/timesheet/*/store", handle_store)
        context.route("**/api/admin-panel/employees/*/timesheet?search=*", handle_timesheet_search)

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
