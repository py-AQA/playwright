import pytest
from playwright.sync_api import Page, Download, expect


def handle_download(download: Download):
    print("download.path()", download.path(), )
    print("download.suggested_filename", download.suggested_filename)
    print("download.page.url", download.page.url)
    print("download.url", download.url)
    download.save_as("new_renamed_file.txt")


# TODO why page.on doesn't catch download event
def test_demo_qa_file_download_4(page: Page):
    page.goto("https://testpages.eviltester.com/styled/download/download.html")

    page.on("download", handle_download)
    page.get_by_role("button", name="Server Download", exact=True).click()


@pytest.mark.ok
def test_demo_qa_file_download(page: Page):
    page.goto("https://testpages.eviltester.com/styled/download/download.html")

    with page.expect_download() as download_info:
        page.get_by_role("button", name="Direct Link Download", exact=True).click()

    download = download_info.value
    print("download.path()", download.path(), )
    print("download.suggested_filename", download.suggested_filename)
    print("download.page.url", download.page.url)
    print("download.url", download.url)
    download.save_as("renamed_file.txt")


@pytest.mark.ok
def test_demo_qa_file_server_download(page: Page):
    page.goto("https://testpages.eviltester.com/styled/download/download.html")

    with page.expect_download() as download_info:
        page.get_by_role("button", name="Server Download").click()

    download = download_info.value
    print("download.path()", download.path(), )
    print("download.suggested_filename", download.suggested_filename)
    print("download.page.url", download.page.url)
    print("download.url", download.url)


@pytest.mark.ok
def test_redirect_server(page: Page):
    page.goto("https://testpages.eviltester.com/styled/download/download.html")

    page.get_by_role("button", name="POST / GET Redirect Server").click()

    expect(page.get_by_text("This is a generated text file")).to_be_visible()


@pytest.mark.ok
def test_direct_link(page: Page):
    page.goto("https://testpages.eviltester.com/styled/download/download.html")

    page.get_by_role("button", name="Direct Link", exact=True).click()

    expect(page.get_by_text("This is a text file")).to_be_visible()
