import pytest
from playwright.sync_api import Page, expect


@pytest.mark.ok
def test_evil_tables(page: Page):
    # выдает все элементы таблицы подряд, без разбиения на колонки и строки
    page.goto("https://testpages.eviltester.com/styled/tag/table.html")
    page.get_by_role("cell", name="Name")
    next_row = page.locator("td:below(th:text('Name'))")
    for item in next_row.all():
        print(item.inner_text())


@pytest.mark.ok
def test_evil_tables_correct_variant(page: Page):
    page.goto("https://testpages.eviltester.com/styled/tag/table.html")

    # нахожу колонку слева от колонки с именем Amount
    next_row = page.locator("td:left-of(th:text('Amount'))")
    print(next_row.all_inner_texts())
    # print(next_row.nth(2).inner_text())
    expect(next_row).to_have_count(4)

    # нахожу сумму по второй колонке
    next_row = page.locator("td:right-of(th:text('Name'))")
    print("итерировать тексты", sum([float(amm) for amm in next_row.all_inner_texts()]))
    print("итерировать веб элементы", sum([float(elem.inner_text()) for elem in next_row.all()]))


@pytest.mark.ok
def test_dynamic_table(page: Page):
    # вставить строку в таблицу
    page.goto("https://testpages.eviltester.com/styled/tag/dynamic-table.html")
    page.get_by_text("Table Data").click()
    cells_before = page.get_by_role("cell").count()
    page.locator("#jsondata").fill(
        '[{"name" : "Bob", "age" : 20}, {"name": "new_name", "age": 150}, {"name": "George", "age" : 42}]')
    page.get_by_role("button", name="Refresh Table").click()
    # проверяю, что таблица увеличилась на 2 ячейки
    expect(page.get_by_role("cell")).to_have_count(cells_before + 2)
    # одно из значений имеет значение new_name
    expect(page.get_by_role("cell", name="new_name")).to_be_visible()


def test_table_filter(page: Page):
    page.goto('https://devexpress.github.io/devextreme-reactive/react/grid/docs/guides/filtering/')
    # page.pause()
    page.frame_locator("iframe >> nth=0").get_by_placeholder("Filter...").first.fill("l")

    next_row = page.frame_locator("iframe >> nth=0").locator("tr:below(span:text('Name'))")
    [[print(item.inner_text()) for item in next_row.nth(i).all()] for i in range(next_row.count())]
    # expect(next_row).to_have_count(1)

    # next_row = page.locator("tr:right-of(th:text('Name'))")
    # print(next_row.all_inner_texts())
