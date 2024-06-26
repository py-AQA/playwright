from datetime import date

from playwright.sync_api import Locator


def set_date(calendar: Locator, day: date):
    month_number = {"июнь": 6, "июль": 7}
    month_name = {6: "июня", 7: "июля"}

    calendar_date = calendar.locator("button.react-calendar__navigation__label span").inner_text()
    month, year = month_number[calendar_date.split()[0]], int(calendar_date.split()[1])

    if delta := abs(day.month - month):
        calendar.get_by_role("button", name="›" if day.month > month else "‹").click(click_count=delta)
    if delta := abs(day.year - year):
        calendar.get_by_role("button", name="»" if day.year > year else "«").click(click_count=delta)
    name = f"{day.day} {month_name[day.month]} {day.year} г."
    calendar.get_by_role("button", name=name, exact=True).click()