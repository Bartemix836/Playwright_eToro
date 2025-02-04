import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import time
import pytest
from playwright.sync_api import sync_playwright
from pages.base_page import TestHelper

@pytest.mark.usefixtures("playwright_context")
def test_launch_browser(playwright_context):
    # STEP 1: Launch the browser
    browser = playwright_context["browser"]
    page = playwright_context["page"]
    base_page = TestHelper(page)
    print("STEP 1: Browser launched")

    # STEP 2: Navigate to the eToro website
    page.goto("https://www.etoro.com/en")
    print("STEP 2: Navigated to eToro website")
    time.sleep(3)

    # STEP 3: Click the "Accept All" button to accept cookies
    base_page.click_element_by_text("Accept All")
    print("STEP 3: Clicked 'Accept All' button")
    time.sleep(3)

    # STEP 4: Hover over the "Top Markets" menu and click it
    element_topmarkets = "li.li-lvl-1:has(span:text('Top Markets'))"
    base_page.click_element_by_selector(element_topmarkets)
    print("STEP 4: Clicked 'Top Markets' menu")
    time.sleep(3)

    # STEP 5: Click the "Stocks" option in the menu
    stocks_locator = "a[href='/discover/markets/stocks']"
    base_page.click_element_by_selector(stocks_locator)
    print("STEP 5: Clicked 'Stocks' option")
    time.sleep(1)

    # STEP 6: Click the "Overview" tab on the Stocks page
    overview_locator = "div.tab-name-wrapper >> text='Overview'"
    base_page.click_element_by_selector(overview_locator)
    print("STEP 6: Clicked 'Overview' tab")
    time.sleep(1)

    # STEP 7: Click the "Apple" stock option
    apple_locator = "div.et-instrument-icon-info__content >> span.et-instrument-icon-info__description:has-text('Apple')"
    base_page.click_element_by_selector(apple_locator)
    print("STEP 7: Clicked 'Apple' stock option")
    time.sleep(5)

    # STEP 8: Cycle through time periods from "1D" to "MAX" for Apple stock
    time_periods = ["1D", "1W", "1M", "6M", "1Y", "3Y", "MAX"]
    for period in time_periods:
        base_page.click_element_by_text(period)
        print(f"STEP 8: Changed time period to {period}")
        time.sleep(1)

    # STEP 9: Scroll the page down in 3 steps of 700px each
    base_page.scroll_page_steps(3, 700, 1)
    print("STEP 9: Scrolled down the page")
    time.sleep(2)

    # STEP 10: Click on the "Chart" tab
    base_page.click_element_by_selector("text='Chart'")
    print("STEP 10: Clicked 'Chart' tab")
    time.sleep(2)

    # STEP 11: Click on the "Financials" tab
    base_page.click_element_by_selector("text='Financials'")
    print("STEP 11: Clicked 'Financials' tab")
    time.sleep(2)

    # STEP 12: Scroll down the Financials page in 3 steps of 700px each
    base_page.scroll_page_steps(3, 700, 1)
    print("STEP 12: Scrolled down the Financials page")
    time.sleep(2)

    # STEP 13: Locate and click the one-click switch for financial summary
    locator_switch = "//span[contains(@class, 'one-click-switch') and contains(@class, 'financial-summary')]"
    base_page.click_element_by_selector(locator_switch)
    print("STEP 13: Clicked one-click switch for financial summary")
    time.sleep(2)
    base_page.click_element_by_selector(locator_switch)
    print("STEP 13: Toggled one-click switch again")
    time.sleep(2)

    # STEP 14: Click the "Balance Sheet" tab
    balancesheet_locator = "text='Balance Sheet'"
    base_page.click_element_by_selector(balancesheet_locator)
    print("STEP 14: Clicked 'Balance Sheet' tab")
    time.sleep(2)

    # STEP 15: Click the "Cash Flow Statement" tab
    cashflow_locator = "text='Cash Flow Statement'"
    base_page.click_element_by_selector(cashflow_locator)
    print("STEP 15: Clicked 'Cash Flow Statement' tab")
    time.sleep(2)

    print("Test case completed successfully - positive result.")

@pytest.fixture(scope="function")
def playwright_context():
    """
    Creates a Playwright context with a full window and returns page and browser instances.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        screen_width = 1820
        screen_height = 980
        context = browser.new_context(
            viewport={"width": screen_width, "height": screen_height}
        )
        page = context.new_page()
        yield {"browser": browser, "page": page}
        browser.close()

if __name__ == "__main__":
    pytest.main(["-v", "--html=reports/test_etoro_report.html", "--self-contained-html"])
