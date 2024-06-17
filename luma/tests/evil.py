from playwright.sync_api import Page, expect, Dialog, FileChooser, Download


def test_upload_a_file(page: Page):
    page.goto("https://testpages.eviltester.com/styled/file-upload-test.html")
    # page.pause()
    page.locator("#fileinput").set_input_files("realistichnaya-rusalka.jpg")
    page.get_by_label("Image").check()
    page.get_by_role("button", name="Upload").click()
    expect(page.locator("#uploadedfilename")).to_contain_text("realistichnaya-rusalka.jpg")


def test_basic_ajax_example(page: Page):
    page.goto("https://testpages.eviltester.com/styled/basic-ajax-test.html")
    page.get_by_label("Category:").select_option("2")
    page.get_by_label("Language:").select_option("13")
    page.get_by_role("button", name="Code In It").click()
    expect(page.locator("#back_to_form")).to_contain_text("Go back to the form")


def test_drag_and_drop_examples(page: Page):
    page.goto("https://testpages.eviltester.com/styled/drag-drop-javascript.html")
    page.drag_and_drop("#draggable1", "#droppable1")
    page.drag_and_drop("#draggable2", "#droppable2")
    # page.pause()
    expect(page.locator("#droppable1")).to_contain_text("Dropped!")
    expect(page.locator("#droppable2")).to_contain_text("Dropped!")


def test_table(page: Page):
    page.goto("https://testpages.eviltester.com/styled/tag/table.html")

    next_row = page.locator("td:left-of(th:text('Amount'))")

    print(next_row.all_inner_texts())
    print(next_row.nth(2).inner_text())
    expect(next_row).to_have_count(4)


def test_evil_tables2(page: Page):
    page.goto("https://testpages.eviltester.com/styled/tag/table.html")
    page.get_by_role("cell", name="Name")
    # нахожу колонку слева от колонки с именем Amount
    next_row = page.locator("td:left-of(th:text('Amount'))")
    print(next_row.all_inner_texts())
    # print(next_row.nth(2).inner_text())
    expect(next_row).to_have_count(4)
    # нахожу сумму по второй колонке
    summ = 0
    next_row = page.locator("td:right-of(th:text('Name'))")
    for txt in next_row.all_inner_texts():
        summ += float(txt)
    print(summ)
