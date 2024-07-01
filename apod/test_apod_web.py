import re

from playwright.sync_api import Page, expect, Request

from apod.apod_calendar import ApodCalendar


def test_pause(page_my: Page):
    page_my.goto("https://apod-dev-d.osora.ru/settings")
    page_my.pause()


def test_choose_employee_statistics_display_date_period(page_my: Page):
    """Выбрать период - NB: тут календарь закрывается сам при выборе второго конца периода"""
    page_my.goto("https://apod-dev-d.osora.ru/employees/one/timesheet")
    page_my.get_by_text("Статистика").click()

    page_my.get_by_placeholder("Выберите период").click()
    ApodCalendar(page_my.get_by_placeholder("Выберите период")).set_period('2019-07-07', '2020-06-17')

    # page_my.pause()


def test_calendar_add_archive(page_my: Page):
    """Выбрать период - NB: тут календарь НЕ закрывается сам при выборе второго конца периода - добавил close"""
    page_my.goto("https://apod-dev-d.osora.ru/employees/one/calendar")
    page_my.get_by_text("Добавить архивные записи").click()

    page_my.get_by_text("Выберите статус периода").click()
    page_my.locator("li").filter(has_text="Больничный").locator("span").click()

    page_my.get_by_placeholder("Выберите период").click()
    ApodCalendar(page_my.get_by_placeholder("Выберите период")).set_period('2019-07-07', '2020-06-17')

    # page_my.pause()

    page_my.get_by_text("Добавить", exact=True).click()
    expect(page_my.locator('[testid="alertTitle"]')).to_have_text("Успех")
    page_my.get_by_text("Принять").click()


def test_add_reminder(page_my: Page):
    """Выбрать одну дату - NB: тут календарь НЕ закрывается автоматически после выбора одной даты - но должен"""
    page_my.goto("https://apod-dev-d.osora.ru/employees/one/timesheet")
    page_my.get_by_text("Напоминания").click()
    page_my.get_by_text("+ добавить напоминание").click()

    page_my.get_by_placeholder("Выберите дату").last.click()
    ApodCalendar(page_my.get_by_placeholder("Выберите дату").last).set_date('2019-07-27')

    # page_my.pause()

    page_my.get_by_text("Сохранить").click()
    expect(page_my.locator('[testid="alertTitle"]')).to_have_text("Успех")
    page_my.get_by_text("Принять").click()


def test_edit_first_reminder(page_my: Page):
    """Выбрать одну дату"""
    page_my.goto("https://apod-dev-d.osora.ru/employees/one/timesheet")
    page_my.get_by_text("Напоминания").click()

    page_my.get_by_placeholder("Выберите дату").first.click()
    ApodCalendar(page_my.get_by_placeholder("Выберите дату").first).set_date('2019-07-27')

    page_my.get_by_text("Сохранить").click()
    expect(page_my.locator('[testid="alertTitle"]')).to_have_text("Успех")
    page_my.get_by_text("Принять").click()


def test_calendar_plan_vacation(page_my: Page):
    """Выбрать период - not a popup"""
    page_my.goto("https://apod-dev-d.osora.ru/employees/one/calendar")

    page_my.get_by_text("Не выбрано").click()
    page_my.locator("li").filter(has_text="Отпуск").locator("span").click()

    ApodCalendar(page_my.locator("div.react-calendar")).set_period('2019-07-07', '2020-06-17')
    # page_my.pause()

    page_my.get_by_text("Запланировать").click()
    expect(page_my.locator('[testid="alertTitle"]')).to_have_text("Успех")
    page_my.pause()
    page_my.get_by_text("Принять").click()


def test_calendar_plan_medical(page_my: Page):
    """Выбрать период - not a popup"""
    page_my.goto("https://apod-dev-d.osora.ru/employees/one/calendar")

    page_my.get_by_text("Не выбрано").click()
    page_my.locator("li").filter(has_text="Больничный").locator("span").click()

    ApodCalendar(page_my.locator("div.react-calendar")).set_period('2019-07-07', '2020-06-17')
    page_my.pause()

    page_my.get_by_text("Запланировать").click()
    expect(page_my.locator('[testid="alertTitle"]')).to_have_text("Успех")
    page_my.get_by_text("Принять").click()


def test_calendar_plan_otgul(page_my: Page):
    """Выбрать несколько ОТДЕЛЬНЫХ дней с подсветкой"""
    page_my.goto("https://apod-dev-d.osora.ru/employees/one/calendar")

    page_my.get_by_text("Не выбрано").click()
    page_my.locator("li").filter(has_text="Отгул").locator("span").click()

    ApodCalendar(page_my.locator("div.react-calendar")).set_date('2020-07-22', '2020-07-24', '2020-07-26')

    page_my.get_by_text("Запланировать").click()
    expect(page_my.locator('[testid="alertTitle"]')).to_have_text("Успех")
    page_my.get_by_text("Принять").click()


def test_calendar_plan_workdays(page_my: Page):
    """Выбрать несколько дней - types: 5-2(def), 2-2, 3-1"""
    page_my.goto("https://apod-dev-d.osora.ru/employees/one/calendar")

    page_my.get_by_text("Не выбрано").click()
    page_my.locator("li").filter(has_text="Рабочий график").locator("span").click()

    ApodCalendar(page_my.locator("div.react-calendar")).set_date('2020-07-22', '2020-07-24', '2020-07-26')
    page_my.pause()
    page_my.get_by_text("Запланировать").click()
    expect(page_my.locator('[testid="alertTitle"]')).to_have_text("Успех")
    page_my.get_by_text("Принять").click()


def test_calendar_plan_workdays_ind(page_my: Page):
    """Выбрать несколько ОТДЕЛЬНЫХ дней с подсветкой - types: ind"""
    page_my.goto("https://apod-dev-d.osora.ru/employees/one/calendar")

    page_my.get_by_text("Не выбрано").click()
    page_my.locator("li").filter(has_text="Рабочий график").locator("span").click()
    page_my.get_by_text("индивидуально").click()

    ApodCalendar(page_my.locator("div.react-calendar")).set_date('2020-07-22', '2020-07-24', '2020-07-26')

    page_my.get_by_text("Запланировать").click()
    expect(page_my.locator('[testid="alertTitle"]')).to_have_text("Успех")
    page_my.get_by_text("Принять").click()


def test_payment_type_monthly_set_date(page_my: Page):
    page_my.goto("https://apod-dev-d.osora.ru/employees/one/paymentSystem")

    page_my.get_by_placeholder("Дата").click()

    ApodCalendar(page_my.get_by_placeholder("Дата")).set_date('2020-07-26')

    page_my.get_by_text("Сохранить").first.click()


def test_payment_type_hourly_set_date(page_my: Page):
    page_my.goto("https://apod-dev-d.osora.ru/employees/one/paymentSystem")

    page_my.get_by_text("Почасовая").click()

    page_my.get_by_placeholder("Дата").click()

    ApodCalendar(page_my.get_by_placeholder("Дата")).set_date('2020-07-26')

    page_my.get_by_text("Сохранить").first.click()


def test_employees_settings_calendar_set_date(page_my: Page):
    page_my.goto('https://apod-dev-d.osora.ru/settings')

    # нерабочие дни для большинства сотрудников - нет подсветки
    page_my.get_by_text("Индивидуальный").click()

    ApodCalendar(page_my.locator("div.react-calendar")).set_date('2020-07-26',
                                                                 '2019-07-25',
                                                                 '2019-07-26',
                                                                 '2019-07-27',
                                                                 '2019-07-28')

    # рабочие дни для большинства сотрудников - нет подсветки
    page_my.get_by_text("Индивидуально").click()
    ApodCalendar(page_my.locator("div.react-calendar")).set_date(*(f'2019-07-{i:02}' for i in range(1, 29)))

    page_my.get_by_text("Сохранить").click()


# def test_main(page_my: Page):
#     page_my.goto("https://apod-dev-d.osora.ru/")
#     expect(page_my.locator("div#__next>div>span")).to_contain_text("Выберите часовой пояс компании")


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
    page.pause()
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
    page.locator("input[name='availableMinutesLate']").fill("70")
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


def test_employees_one_card(page_my: Page):
    page = page_my
    page.goto('https://apod-dev-d.osora.ru/employees/three/calendar')
    page.on("request", interception)
    page.pause()
    #
    # page.get_by_label("Close").click()
    #
    # page.get_by_placeholder("@tgnickname").click()
    # page.get_by_placeholder("@tgnickname").fill("@Grom-Zadira")
    # page.get_by_placeholder("ФИО").fill("За орду!")
    # page.get_by_placeholder("Должность").fill("Нужно больше Золота!")
    # page.get_by_placeholder("Дата трудоустройства").fill("2022-02-23")
    # page.get_by_placeholder("Дата выхода").fill("2024-06-23")
    # page.locator('[placeholder="Время окончания смены"]').click()
    # # page.locator('div:nth-child(7) > div:nth-child(2) > input').type("1745")
    # page.locator('[name="endAt"]').type("1745")
    # page.get_by_role("link", name="Сохранить").click()
    # page.pause()


def interception(request: Request):
    print(request.method, request.url, request.post_data)


def test_settings(page_my: Page):
    page = page_my
    page.goto('https://apod-dev-d.osora.ru/settings')
    # Выбор даты вручную
    # page.get_by_text("Индивидуальный").click()
    # page.get_by_role("button", name="«").click()
    # page.get_by_role("button", name="«").click()
    # page.get_by_role("button", name="‹").click()
    # page.get_by_role("button", name="‹").click()
    # page.get_by_role("button", name="‹").click()
    # page.get_by_role("button", name="‹").click()
    # page.get_by_role("button", name="23 февраля 2022 г").click()
    # page.get_by_text("Сохранить").nth(1).click()

    # дата не выбирается, test passed
    page.on("request", interception)
    page.get_by_text("Индивидуальный").click()
    page.locator('[for="customWeekends"]').type("2022-02-23")
    page.locator('[for="customWeekends"]').type("11 июня 2020 г.")


def handle_work_calendar(request: Request):
    print(request.method, request.url, request.post_data)


def test_work_calendar(page_my: Page):
    page = page_my
    page.goto('https://apod-dev-d.osora.ru/employees/one/calendar')
    page.on('request', handle_work_calendar)
    page.locator("div").filter(has_text=re.compile(r"^Не выбрано$")).locator("svg").click()
    # page.locator("li").filter(has_text="Отгул").locator("span").click()
    page.locator("li").filter(has_text="Рабочий график").locator("span").click()
    page.locator("label").filter(has_text="2-").click()
    page.get_by_role("button", name="›").click()
    page.get_by_role("button", name="1 июля 2024 г.", exact=True).click()
    page.get_by_role("button", name="2 июля 2024 г.", exact=True).click()
    page.get_by_role("button", name="3 июля 2024 г.", exact=True).click()

    page.get_by_text("Запланировать").click()


def method(request: Request):
    print(request.url)
    print(request.post_data)


def test_admin_check_monthly(page_my: Page):
    page = page_my
    page.goto('https://apod-dev-d.osora.ru/employees/one/paymentSystem')
    page.on("request", method)
    page.pause()
    page.locator("input[name=\"salary\"]").fill("10000")
    page.get_by_role("spinbutton").fill("10000")
    page.locator("input[name=\"comment\"]").fill("Премия")
    page.locator("div").filter(has_text=re.compile(r"^Дата начисления$")).locator("svg").click()
    page.get_by_role("button", name="»").click()
    page.get_by_role("button", name="25 июня 2025 г").click()
    page.locator("div:nth-child(3) > div > .svg-inline--fa > path").click()
    page.get_by_text("Сохранить").nth(1).click()
    page.get_by_text("Сохранить").first.click()
    page.get_by_text("Принять").click()


def test_admin_check_hourly_payment_system(page_my: Page):
    page = page_my
    page.goto('https://apod-dev-d.osora.ru/employees/one/paymentSystem')
    page.on("request", method)
    page.get_by_text("Почасовая").click()
    page.locator("input[name=\"hourlyRate\"]").fill("1000")
    page.locator("input[name=\"overworkMultiplyRate\"]").fill("2000")
    page.get_by_text("Добавить прогрессивную ставку").click()
    page.locator("input[name=\"payRateByHour\"]").click()
    page.locator("div:nth-child(4) > div > .flex > .hover\\:cursor-pointer > div > .svg-inline--fa > path").click()
    page.get_by_text("Добавить прогрессивную ставку").click()
    page.locator("input[name=\"payRateByHour\"]").fill("15000")

    page.locator("input[name=\"bonus\"]").fill("15000")
    page.locator("input[name=\"comment\"]").fill("Премия")
    page.get_by_placeholder("Дата").click()

    page.get_by_role("button", name="30 июня 2024 г").click()

    page.locator("html").click()
    page.get_by_text("Сохранить").nth(1).click()
    page.get_by_text("Сохранить").first.click()
    page.get_by_text("Принять").click()


def test_admin_check_hourly_new_employee(page_my: Page):
    page = page_my
    page.goto('https://apod-dev-d.osora.ru/employees/newEmployee')
    page.on("request", method)
    page.pause()
    page.locator("input[name=\"username\"]").fill("darius_25")
    page.get_by_text("Почасовая").click()

    page.get_by_text("2-").click()

    page.locator("input[name=\"employmentDate\"]").fill("2015-06-22")
    page.locator("input[name=\"exitDate\"]").fill("2015-06-25")

    page.locator("input[name=\"fullName\"]").fill("Darius")

    page.locator("input[name=\"specialization\"]").fill("Engineer")
    page.get_by_text("Добавить").click()

    page.get_by_text("Принять").click()


def test_test(page_my: Page):
    page_my.goto("https://apod-dev-d.osora.ru/employees/one/calendar")
    page_my.pause()
    page = page_my
    page.locator("div").filter(has_text=re.compile(r"^Не выбрано$")).locator("svg").click()
    page.locator("li").filter(has_text="Рабочий график").locator("span").click()
    page.get_by_text("2-").click()
    page.get_by_text("-1").click()
    page.get_by_text("индивидуально").click()
    page.get_by_text("индивидуально", exact=True).click()
    page.get_by_role("button", name="›").click()
    page.get_by_role("button", name="10 июля 2024 г").click()
    page.get_by_role("button", name="11 июля 2024 г").click()
    page.get_by_role("button", name="12 июля 2024 г").click()
    page.locator(".h-1\\.5").first.click()
    page.get_by_text("Запланировать").click()
    expect(page.locator('[testid="alertTitle"]')).to_have_text("Успех")
    page.get_by_text("Принять").click()


def test_add_four_ind_days_LK(page_my: Page):
    page_my.goto("https://apod-dev-d.osora.ru/employees/one/calendar")
    page_my.pause()
    page = page_my
    page.locator("div").filter(has_text=re.compile(r"^Не выбрано$")).click()
    page.locator("li").filter(has_text="Отпуск").locator("span").click()
    page.get_by_role("button", name="›").click()
    page.get_by_role("button", name="›").click()
    page.get_by_role("button", name="6 августа 2024 г.", exact=True).click()
    page.get_by_role("button", name="7 августа 2024 г.", exact=True).click()
    page.get_by_role("button", name="8 августа 2024 г.", exact=True).click()
    page.get_by_role("button", name="9 августа 2024 г.", exact=True).click()
    page.get_by_text("Запланировать").click()
    expect(page.locator('[testid="alertTitle"]')).to_have_text("Успех")
    page.get_by_text("Принять").click()
    # page.get_by_label("Close").click()


def test_add_employee_with_5_2_LK(page_my: Page):
    page_my.goto("https://apod-dev-d.osora.ru/employees/one/calendar")
    page_my.pause()
    page = page_my
    page.locator("div").filter(has_text=re.compile(r"^импортэкспортfnonespecfntwospec$")).get_by_role("link").click()
    page.locator("input[name=\"username\"]").click()
    page.locator("input[name=\"username\"]").fill("My_Nickname")
    page.locator("input[name=\"fullName\"]").click()
    page.locator("input[name=\"fullName\"]").fill("Fname Lname")
    page.locator("input[name=\"specialization\"]").click()
    page.locator("input[name=\"specialization\"]").fill("IT")
    page.get_by_text("5-").click()
    page.locator("input[name=\"employmentDate\"]").fill("2024-07-10")
    page.locator("input[name=\"exitDate\"]").fill("2024-07-11")
    page.get_by_text("Добавить").click()
    expect(page.locator('[testid="alertTitle"]')).to_have_text("Успех")
    page.get_by_text("Принять").click()


def test_add_settings_Ind_employee_LK(page_my: Page):
    page_my.goto("https://apod-dev-d.osora.ru/employees/one/calendar")
    page_my.pause()
    page = page_my
    page.get_by_role("link", name="Настройки").click()
    page.get_by_text("Индивидуальный").click()
    page.get_by_role("button", name="›").click()
    page.get_by_role("button", name="9 июля 2024 г.", exact=True).click()
    page.get_by_role("button", name="11 июля 2024 г").click()
    page.get_by_role("button", name="12 июля 2024 г").click()
    page.get_by_text("Сохранить").nth(1).click()
    page.locator("div").filter(has_text=re.compile(r"^Начало рабочего дняВыберите время$")).locator("svg").click()
    page.get_by_text("08:00").click()
    page.locator("div").filter(has_text=re.compile(r"^Выберите время$")).locator("svg").click()
    page.get_by_text("17:00").click()
    page.locator("input[name=\"name\"]").click()
    page.locator("input[name=\"name\"]").fill("LK")
    page.locator("input[name=\"latitude\"]").click()
    page.locator("input[name=\"latitude\"]").fill("2")
    page.locator("input[name=\"longitude\"]").click()
    page.locator("input[name=\"longitude\"]").fill("4")
    page.locator("input[name=\"radius\"]").click()
    page.locator("input[name=\"radius\"]").fill("5")
    page.get_by_text("Сохранить").click()
    expect(page.locator('[testid="alertTitle"]')).to_have_text("Успех")
    page.get_by_text("Принять").click()


def test_redirect_to_employee_info(page_my: Page):
    """ Переход на страницу работника с информацией"""
    page = page_my

    page.goto("https://apod-dev-d.osora.ru/employees/one")
    page.get_by_label("Close").click()

    # Opens new page with employee info
    with page.expect_popup() as new_page:
        page.locator("ul").filter(has_text="C3").get_by_role("link").first.click()
    page1 = new_page.value
    page1.get_by_label("Close").click()

    expect(page1).to_have_url(re.compile('https://apod-dev-d.osora.ru/employees/urltg'))
    expect(page1.get_by_text("Информация по сотруднику")).to_be_visible()
    page.pause()


def test_add_new_employee(page_my: Page):
    """ Проверка создания нового сотрудника в системе (mocking) """
    page = page_my

    # Monitoring request and response packets
    page.on("request", lambda req: print(">>>: " + req.method, req.post_data))
    page.on("response", lambda res: print(" <<<: " + str(res.status), res.body()))

    page.goto("https://apod-dev-d.osora.ru/employees/newEmployee")

    # Fills forms of new employee
    page.locator("input[name='username']").fill("@vladi")
    page.locator("input[name='fullName']").fill("Le Alfonse")
    page.locator("input[name='specialization']").fill("General")
    page.locator("input[name='employmentDate']").fill("2024-06-29")

    # Keeps value of Name and Specialization fields
    full_name = page.locator("input[name='fullName']").input_value()
    spec = page.locator("input[name='specialization']").input_value()

    # Mock API request with data from a form
    page.route(
        "**/api/admin-panel/employees",
        lambda route: route.fulfill(status=200, json={"employees": [
            {
                "id": "777",
                "companyId": "89",
                "companyWorkplaces": 'null',
                "fullName": full_name,
                "specialization": spec,
                "urlTG": "@vlad"}]}))

    page.get_by_text("Добавить").click()

    expect(page.locator("[id='__next']")).to_contain_text("Сотрудник добавлен")

    page.get_by_text("Принять").click()

    expect(page.get_by_role("heading")).to_contain_text(full_name)

    page.pause()


def test_employees_calendar_set_limits(page_my: Page):
    # задать настройки для рабочего графика: ограничения
    # широту и долготу как вводить? должны быть градусы, минуты, секунды,
    # а тут только целые числа без ограничения.
    # начало и окончание рабочего дня не отображаются
    page_my.goto('https://apod-dev-d.osora.ru/settings')
    page_my.get_by_text("Стандартный по РФ").click()
    page_my.get_by_text("5-").click()
    page_my.locator("div").filter(has_text=re.compile(r"^Начало рабочего дняВыберите время$")).locator("svg").click()
    page_my.get_by_text("09:00").click()
    page_my.locator("div").filter(has_text=re.compile(r"^Выберите время$")).locator("svg").click()
    page_my.get_by_text("16:00").click()
    page_my.locator("input[name=\"availableMinutesLate\"]").fill("20")
    page_my.locator("input[name=\"monthMaxOverwork\"]").fill("12")
    page_my.locator("input[name=\"dayMaxOverwork\"]").fill("2")
    page_my.locator("input[name=\"vacationDays\"]").fill("14")
    page_my.locator("input[name=\"vacationPeriod\"]").fill("5")
    page_my.locator("input[name=\"maxAbsenceDays\"]").fill("3")
    page_my.locator("input[name=\"nameundefined\"]").fill("set1")
    page_my.locator("input[name=\"latitudeundefined\"]").fill("1000000")
    page_my.locator("input[name=\"longitudeundefined\"]").fill("25")
    page_my.locator("input[name=\"radiusundefined\"]").fill("1")
    page_my.get_by_text("Сохранить").click()
    page_my.get_by_text("Принять").click()
    page_my.pause()
