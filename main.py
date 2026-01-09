import selectors

from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://google.com")

    search_input = page.locator('//div[@class="RNNXgb"]//textarea')
    search_input.fill('zdarova balbesi')

    search_button = page.locator('//div[@class="FPdoLc lJ9FBc"]//input[1]')
    search_button.click()

    page.wait_for_timeout(5000)