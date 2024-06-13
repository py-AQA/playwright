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
    page.goto("https://SunInJuly.github.io/execute_script.html.")
    page.on("dialog", handle_stepik_alert)
    x = page.locator('#input_value').inner_text()
    calc(x)

