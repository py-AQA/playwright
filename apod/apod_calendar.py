from datetime import date

from playwright.sync_api import Locator


class ApodCalendar:
    month_number = {"январь": 1, "февраль": 2, "март": 3, "апрель": 4, "май": 5, "июнь": 6,
                    "июль": 7, "август": 8, "сентябрь": 9, "октябрь": 10, "ноябрь": 11, "декабрь": 12}
    month_name = {1: "января", 2: "февраля", 3: "марта", 4: "апреля", 5: "мая", 6: "июня",
                  7: "июля", 8: "августа", 9: "сентября", 10: "октября", 11: "ноября", 12: "декабря"}

    def __init__(self, calendar: Locator, close_icon: Locator = None):
        self.calendar = calendar.locator("../../..")

    def __refresh_date(self):
        active_date = self.calendar.locator("button.react-calendar__navigation__label span").inner_text()
        self.month, self.year = self.month_number[active_date.split()[0]], int(active_date.split()[1])

    def __set_date(self, day: str):
        try:
            day = date.fromisoformat(day)
        except (TypeError, ValueError) as e:
            print("Should be a ISO 8601 date format string [YYYY-MM-DD]:", e)

        self.__refresh_date()

        if delta := abs(day.month - self.month):
            self.calendar.get_by_role("button", name="›" if day.month > self.month else "‹").click(click_count=delta)
        if delta := abs(day.year - self.year):
            self.calendar.get_by_role("button", name="»" if day.year > self.year else "«").click(click_count=delta)

        name = f"{day.day} {self.month_name[day.month]} {day.year} г."
        self.calendar.get_by_role("button", name=name, exact=True).click()

    def set_date(self, *days: str):
        [self.__set_date(day) for day in days]
        self.close()

    def set_period(self, from_date: str, to_date: str):
        self.__set_date(from_date)
        self.__set_date(to_date)
        self.close()

    def close(self):
        if self.calendar.get_by_text("Сохранить").is_visible():
            self.calendar.get_by_text("Сохранить").click()
        elif self.calendar.locator("button.react-calendar__navigation__label span").is_visible():
            if self.calendar.locator("[data-icon='calendar-days']").is_visible():
                self.calendar.locator("[data-icon='calendar-days']").click()

    def save(self):
        self.calendar.get_by_text("Сохранить").click()
