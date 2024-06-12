import math
import time

from playwright.sync_api import Page, expect, Dialog, FileChooser, Download


def handle_manage_alert(d: Dialog):
    print("\n", d.message.split()[-1])
    d.accept()


def test_summ(page: Page):
    page.goto("https://suninjuly.github.io/selects1.html")
    page.on("dialog", handle_manage_alert)
    summ = int(page.locator("#num1").inner_text()) + int(page.locator("#num2").inner_text())
    page.select_option('#dropdown', label=str(summ))
    expect(page.locator(".btn.btn-default")).to_be_enabled()
    expect(page.locator(".btn.btn-default")).to_be_visible()
    page.locator(".btn.btn-default").click()



def test_abs(page: Page):
    page.goto("https://suninjuly.github.io/execute_script.html")
    page.on("dialog", handle_manage_alert)
    result = str(math.log(abs(12*math.sin(int(page.locator("#input_value").inner_text())))))
    page.evaluate("window.scrollBy(0, 150)")
    page.locator("#answer").fill(result)
    page.locator("#robotCheckbox").check()
    page.locator("#robotsRule").check()
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

