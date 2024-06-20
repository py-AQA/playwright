import asyncio

from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as p:
        for browser_type in [p.chromium, p.firefox, p.webkit]:
            browser = await browser_type.launch()
            page = await browser.new_page()
            await page.goto('http://scrapingant.com/')
            await page.screenshot(path=f'scrapingant-{browser_type.name}.png')
            await browser.close()


asyncio.get_event_loop().run_until_complete(main())


def test_empty():
    """пустой тест для того чтоб при запуске из pycharm pytest не ругался"""
    pass
