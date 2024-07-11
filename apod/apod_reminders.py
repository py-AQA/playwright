from playwright.sync_api import Locator, expect

from apod.apod_calendar import ApodCalendar


class ApodReminder:

    def __init__(self, locator: Locator):
        self.locator = locator
        pass

    def set_comment(self, comment):
        self.locator.get_by_placeholder("Комментарий").fill(comment)

    def set_loop(self, state=True):
        checked = self.locator.get_by_text("Зациклить").is_checked()
        if state and not checked:
            self.locator.get_by_text("Зациклить").click()
        expect(self.locator.get_by_text("Зациклить")).to_be_checked()
        if not state and checked:
            self.locator.get_by_text("Зациклить").click()
        expect(self.locator.get_by_text("Зациклить")).not_to_be_checked()

    def set_date(self, date):
        ApodCalendar(self.locator.get_by_placeholder("Выберите дату")).set_date(date)

    def set_time(self, time):
        self.locator.get_by_text("Выберите время").last.click()
        self.locator.get_by_text(time).click()


class ApodReminders:
    url = "https://apod-api-dev-d.osora.ru/api/admin-panel/employees/one/reminder"

    def __init__(self, user, tab: Locator):
        self.user = user
        self.tab = tab
        self.reminder_list: [Locator] = [ApodReminder(el) for el in tab.locator("li.grid-cols-reminder").all]

    def add_reminder(self):
        self.tab.locator("add").click()
        self.reminder_list[-1].set_comment("comment here")
        self.reminder_list[-1].set_loop()
        self.reminder_list[-1].set_date("2024-01-01")
        self.reminder_list[-1].set_time("23:30")

    def save(self):
        self.tab.get_by_text("Сохранить").click()
