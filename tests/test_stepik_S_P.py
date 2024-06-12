import math
import time

from playwright.sync_api import Page, expect, Dialog, FileChooser, Download

def calc(x: str) -> str:
    return str(math.log(abs(12 * math.sin(int(x)))))


def handle_alert(alert: Dialog):
    assert alert.message.startswith("Congrats"), "NOPE!"
    print(f"\nStepik code: {alert.message.split()[-1]}")
    alert.accept()


@pytest.mark.ok
def test_section2_lesson2_step3_select_by_label(page: Page):
    page.on("dialog", handle_alert)

    page.goto("https://suninjuly.github.io/selects1.html")
    summ = int(page.locator("#num1").inner_text()) + int(page.locator("#num2").inner_text())
    page.select_option('#dropdown', label=str(summ))
    expect(page.locator(".btn.btn-default")).to_be_enabled()
    expect(page.locator(".btn.btn-default")).to_be_visible()
    page.locator(".btn.btn-default").click()


@pytest.mark.ok
def test_section2_lesson2_step6_windows_scroll_by_execute_js_script(page: Page):
    page.on("dialog", handle_alert)

    page.goto("https://suninjuly.github.io/execute_script.html")
    page.locator("#answer").fill(calc(page.locator("#input_value").inner_text()))
    page.locator("#robotCheckbox").check()
    page.locator("#robotsRule").check()

    # + is scrolling to bottom of page, - to the top
    # page.evaluate("window.scrollBy(0, 100);")  # same as browser.execute_script("window.scrollBy(0, 100);")
    # page.mouse.wheel(0, 100)
    # page.get_by_role("button", name="Submit").scroll_into_view_if_needed()

    page.get_by_role("button", name="Submit").click()


@pytest.mark.ok
def test_section2_lesson2_step3_select_by_value(page: Page):
    page.on("dialog", handle_alert)

    page.goto("https://suninjuly.github.io/selects1.html")
    result = int(page.locator("#num1").inner_text()) + int(page.locator("#num2").inner_text())
    page.select_option("#dropdown", value=str(result))
    page.get_by_role("button", name="Submit").click()


@pytest.mark.ok
def test_section2_lesson2_step3_select_by_value_on_page_selects2(page: Page):
    page.on("dialog", handle_alert)

    page.goto("https://suninjuly.github.io/selects2.html")
    result = int(page.locator("#num1").inner_text()) + int(page.locator("#num2").inner_text())
    page.select_option("#dropdown", value=str(result))
    page.get_by_role("button", name="Submit").click()


@pytest.mark.xfail
def test_section2_lesson2_step8_upload_file_via_set_input_files_and_click(page: Page):
    page.on("dialog", handle_alert)

    page.goto("http://suninjuly.github.io/file_input.html")

    page.get_by_placeholder("Enter first name").fill("Olga")
    page.get_by_placeholder("Enter last name").fill("Olga")
    page.get_by_placeholder("Enter email").fill("tb@gmail.com")

    page.set_input_files('input[type="file"]', "test_file.txt")
    page.locator('input[type="file"]').click()

    page.get_by_role("button", name="Submit").click()


@pytest.mark.ok
def test_section2_lesson2_step8_upload_file_via_click_and_set_input_files(page: Page):
    page.on("dialog", handle_alert)

    page.goto("http://suninjuly.github.io/file_input.html")

    page.get_by_placeholder("Enter first name").fill("Olga")
    page.get_by_placeholder("Enter last name").fill("Olga")
    page.get_by_placeholder("Enter email").fill("tb@gmail.com")

    page.locator('input[type="file"]').click()
    page.set_input_files('input[type="file"]', "test_file.txt")

    page.get_by_role("button", name="Submit").click()


@pytest.mark.xfail
def test_section2_lesson2_step8_upload_file_via_set_input_files_only(page: Page):
    page.on("dialog", handle_alert)

    page.goto("http://suninjuly.github.io/file_input.html")

    page.get_by_placeholder("Enter first name").fill("Olga")
    page.get_by_placeholder("Enter last name").fill("Olga")
    page.get_by_placeholder("Enter email").fill("tb@gmail.com")

    page.set_input_files('input[type="file"]', "test_file.txt")

    page.get_by_role("button", name="Submit").click()


def handle_file(file: FileChooser):
    file.set_files("test_file.txt")


@pytest.mark.bug
def test_section2_lesson2_step8_upload_file_via_filechooser(page: Page):
    page.on("dialog", handle_alert)
    page.on("filechooser", handle_file)

    page.goto("http://suninjuly.github.io/file_input.html")

    page.get_by_placeholder("Enter first name").fill("Olga")
    page.get_by_placeholder("Enter last name").fill("Olga")
    page.get_by_placeholder("Enter email").fill("tb@gmail.com")

    page.locator('input[type="file"]').click()

    page.get_by_role("button", name="Submit").click()


def test_demo_qa_file(page: Page):
    page.goto("https://testpages.eviltester.com/styled/file-upload-test.html")
    page.set_input_files("#fileinput", "text_file.txt")
    page.get_by_label("A General File").check()
    page.get_by_role("button", name="Upload").click()
    expect(page.locator("#uploadedfilename")).to_contain_text("text_file.txt")


def handle_file(filechooser: FileChooser):
    filechooser.set_files("text_file.txt")


def test_demo_qa_file_2(page: Page):
    page.goto("https://testpages.eviltester.com/styled/file-upload-test.html")
    page.on("filechooser", handle_file)
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





def test_demo_qa_file_download(page: Page):
    page.goto("https://testpages.eviltester.com/styled/download/download.html")
    with page.expect_download() as download_info:
        page.get_by_role("button", name="Direct Link Download", exact=True).click()
    val = download_info.value
    print(val.suggested_filename)
    print(val.page.url)
    print(val.path())
    print(val.url)
    val.save_as("renamed_file.txt")


def test_demo_qa_file_server_download(page: Page):
    page.goto("https://testpages.eviltester.com/styled/download/download.html")
    with page.expect_download() as download_info:
        page.get_by_role("button", name="Server Download").click()
    val = download_info.value
    print(val.suggested_filename)
    print(val.page.url)
    print(val.path())
    print(val.url)


def handle_download(val: Download):
    print(val.suggested_filename)
    print(val.page.url)
    print(val.path())
    print(val.url)
    val.save_as("renamed_file.txt")



def test_demo_qa_file_download_4(page: Page):
    page.goto("https://testpages.eviltester.com/styled/download/download.html")
    page.on("download", handle_download)
    page.get_by_role("button", name="Direct Link Download", exact=True).click()


def test_redirect_server(page: Page):
    page.goto("https://testpages.eviltester.com/styled/download/download.html")
    page.get_by_role("button", name="POST / GET Redirect Server").click()
    expect(page.get_by_text("This is a generated text file")).to_be_visible()




def test_direct_link(page: Page):
    page.goto("https://testpages.eviltester.com/styled/download/download.html")
    page.get_by_role("button", name="Direct Link", exact=True).click()
    expect(page.get_by_text("This is a text file")).to_be_visible()

