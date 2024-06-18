import pytest
from playwright.sync_api import Page, FileChooser, expect

from utils.stepik import handle_stepik_alert


def handle_file(filechooser: FileChooser):
    print("file chooser event")
    filechooser.set_files("text_file.txt")


def test_section2_lesson2_step8_upload_file_via_set_input_files(page: Page):
    page.on("dialog", handle_stepik_alert)

    page.goto("http://suninjuly.github.io/file_input.html")

    page.get_by_placeholder("Enter first name").fill("Olga")
    page.get_by_placeholder("Enter last name").fill("Olga")
    page.get_by_placeholder("Enter email").fill("tb@gmail.com")

    page.set_input_files('input[type="file"]', "test_file.txt")

    page.get_by_role("button", name="Submit").click()


@pytest.mark.ok
def test_section2_lesson2_step8_upload_file_via_click_and_set_input_files(page: Page):
    page.on("dialog", handle_stepik_alert)

    page.goto("http://suninjuly.github.io/file_input.html")

    page.get_by_placeholder("Enter first name").fill("Olga")
    page.get_by_placeholder("Enter last name").fill("Olga")
    page.get_by_placeholder("Enter email").fill("tb@gmail.com")

    page.set_input_files('input[type="file"]', "test_file.txt")

    page.get_by_role("button", name="Submit").click()


def test_section2_lesson2_step8_upload_file_via_set_input_files_only(page: Page):
    page.on("dialog", handle_stepik_alert)

    page.goto("http://suninjuly.github.io/file_input.html")

    page.get_by_placeholder("Enter first name").fill("Olga")
    page.get_by_placeholder("Enter last name").fill("Olga")
    page.get_by_placeholder("Enter email").fill("tb@gmail.com")

    page.set_input_files('input[type="file"]', "test_file.txt")

    page.get_by_role("button", name="Submit").click()


def test_section2_lesson2_step8_upload_file_via_filechooser(page: Page):
    page.on("dialog", handle_stepik_alert)
    page.on("filechooser", handle_file)

    page.goto("http://suninjuly.github.io/file_input.html")

    page.get_by_placeholder("Enter first name").fill("Olga")
    page.get_by_placeholder("Enter last name").fill("Olga")
    page.get_by_placeholder("Enter email").fill("tb@gmail.com")

    page.locator('input[type="file"]').click()

    page.get_by_role("button", name="Submit").click()


def test_demo_qa_file(page: Page):
    page.goto("https://testpages.eviltester.com/styled/file-upload-test.html")

    page.set_input_files("#fileinput", "test_file.txt")
    page.get_by_label("A General File").check()
    page.get_by_role("button", name="Upload").click()

    expect(page.locator("#uploadedfilename")).to_contain_text("test_file.txt")


def test_demo_qa_file_2(page: Page):
    page.on("filechooser", handle_file)

    page.goto("https://testpages.eviltester.com/styled/file-upload-test.html")
    page.locator("#fileinput").click()
    page.get_by_label("A General File").check()
    page.get_by_role("button", name="Upload").click()

    expect(page.locator("#uploadedfilename")).to_contain_text("text_file.txt")


def test_file_upload_with(page: Page):
    page.goto("https://testpages.eviltester.com/styled/file-upload-test.html")

    with page.expect_file_chooser() as fc_info:
        page.locator('#fileinput').click()
    file_chooser = fc_info.value
    file_chooser.set_files("text_file.txt")
    page.get_by_role("button", name="Upload").click()

    expect(page.locator("#uploadedfilename")).to_contain_text("text_file.txt")
