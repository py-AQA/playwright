import math

from playwright.sync_api import Page, expect, Dialog


def handle_stepik_alert(alert: Dialog):
    assert alert.message.startswith("Congrats"), "NOPE!"
    print(f"\nStepik code: {alert.message.split()[-1]}")
    alert.accept()


def calc(x: str) -> str:
    return str(math.log(abs(12 * math.sin(int(x)))))


# "stepik/part2/lesson/2/step/3"
"""  Steps:
1)Открыть страницу https://suninjuly.github.io/selects1.html
2)Посчитать сумму заданных чисел
3)Выбрать в выпадающем списке значение равное расчитанной сумме
4)Нажать кнопку "Submit" """


def test_find_the_sum(page: Page):
    page.goto("https://suninjuly.github.io/selects1.html")
    page.on("dialog", handle_stepik_alert)
    num_1 = page.locator('[id="num1"]')
    num_2 = page.locator('[id="num2"]')
    result = int(num_1.inner_text()) + int(num_2.inner_text())
    print(result)
    page.select_option('[id="dropdown"]', label=str(result))

    button = page.locator('[class="btn btn-default"]')
    expect(button).to_be_enabled()
    expect(button).to_be_visible()
    button.click()


"=================================================================================================================="

# stepik/part2/lesson/2/step/6
"""         steps:
1)Открыть страницу https://SunInJuly.github.io/execute_script.html.
2)Считать значение для переменной x.
3)Посчитать математическую функцию от x.
4)Проскроллить страницу вниз.
5)Ввести ответ в текстовое поле.
6)Выбрать checkbox "I'm the robot".
7)Переключить radiobutton "Robots rule!".
8)Нажать на кнопку "Submit"."""


def test_execute_script(page: Page):
    page.goto("https://suninjuly.github.io/execute_script.html")
    page.on("dialog", handle_stepik_alert)
    x = page.locator('#input_value').inner_text()
    calc(x)
    page.locator("#answer").fill(calc(x))
    # page.locator("form div").filter(has_text="I'm the robot").click()
    page.get_by_label("I'm the robot").check()
    page.get_by_label("Robots rule").check()
    page.locator('[class="btn btn-primary"]').click()
    # page.pause()


"====================================================================================================================="

# stepik/part2/lesson/2/step/8
"""         steps:
1)Открыть страницу http://suninjuly.github.io/file_input.html
2)Заполнить текстовые поля: имя, фамилия, email
3)Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
4)Нажать кнопку "Submit"."""


def test_upload_file(page: Page):
    page.goto("https://suninjuly.github.io/file_input.html")
    page.on("dialog", handle_stepik_alert)
    page.get_by_placeholder("Enter first name").fill("Avenging")

    page.get_by_placeholder("Enter last name").fill("Angelo")
    page.get_by_placeholder("Enter email").fill("Avenging_Angelo.pru")
    page.set_input_files("[for='file']", "for test.txt")
    page.locator('[class="btn btn-primary"]').click()


"==================================================================================================================="
# stepik/part2/lesson/3/step/4
"""        Задание: принимаем alert
                 steps:
1)Открыть страницу http://suninjuly.github.io/alert_accept.html
2)Нажать на кнопку
3)Принять confirm
4)На новой странице решить капчу для роботов, чтобы получить число с ответом."""


def test_alert(page: Page):
    page.goto("http://suninjuly.github.io/alert_accept.html")

    page.on("dialog", lambda dialog: dialog.accept())
    # page.pause()
    page.locator('[type="submit"]').click()
    page.on("dialog", handle_stepik_alert)
    x = page.locator('#input_value').inner_text()
    calc(x)
    page.locator("#answer").fill(calc(x))
    page.locator('[class="btn btn-primary"]').click()


"==================================================================================================================="

# stepik/part2/lesson/3/step/6
"""        steps:
1)Открыть страницу http://suninjuly.github.io/redirect_accept.html
2)Нажать на кнопку
3)Переключиться на новую вкладку
4)Пройти капчу для робота и получить число-ответ"""

"""click(force=True) ДЕЛАЕТ ВОЗМОЖНЫМ кликнуть на Динамическую кнопку"""


def test_redirection(page: Page):
    page.goto("http://suninjuly.github.io/redirect_accept.html")
    # page.pause()
    with page.context.expect_page() as tab:
        page.get_by_text("I want to go on a magical journey!").click(force=True)

    new_tab = tab.value
    new_tab.on("dialog", handle_stepik_alert)
    x = new_tab.locator('#input_value').inner_text()
    calc(x)
    new_tab.locator("#answer").fill(calc(x))
    new_tab.locator('[class="btn btn-primary"]').click()


# stepik/part2/lesson/4/step/8
"""        steps:
1)Открыть страницу http://suninjuly.github.io/explicit_wait2.html
2)Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
3)Нажать на кнопку "Book"
4)Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение"""

"""click(force=True) ДЕЛАЕТ ВОЗМОЖНЫМ кликнуть на Динамическую кнопку"""


def test_expeted(page: Page):
    page.goto("http://suninjuly.github.io/redirect_accept.html")
    # page.pause()