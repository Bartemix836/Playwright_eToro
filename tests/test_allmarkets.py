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

    # STEP 5: Click the "All Markets" option in the menu
    stocks_locator = "a[href='/discover/markets']"
    base_page.click_element_by_selector(stocks_locator)
    print("STEP 5: Clicked 'All Markets' option")
    time.sleep(1)

    # STEP 6: Click the "Stocks" tab in the menu
    stocks_tab_locator = "div.tab-name:text('Stocks')"
    base_page.click_element_by_selector(stocks_tab_locator)
    print("STEP 6: Clicked 'Stocks' tab")
    time.sleep(1)

    # STEP 7: Click the "Crypto" tab in the menu
    crypto_tab_locator = "div.tab-name:text('Crypto')"
    base_page.click_element_by_selector(crypto_tab_locator)
    print("STEP 7: Clicked 'Crypto' tab")
    time.sleep(1)

    # STEP 8: Click the "Indices" tab in the menu
    indices_tab_locator = "div.tab-name:text('Indices')"
    base_page.click_element_by_selector(indices_tab_locator)
    print("STEP 8: Clicked 'Indices' tab")
    time.sleep(1)

    # STEP 9: Click USDOLLAR position
    usdollar_locator = "div[automation-id='trade-item-name']:text('USDOLLAR')"
    base_page.click_element_by_selector(usdollar_locator)
    print("STEP 9: Clicked 'USDOLLAR' position")
    time.sleep(1)

    # STEP 10: Click to Chart mode
    chart_locator = "a[automation-id='et-tab-chart']:text('Chart')"
    base_page.click_element_by_selector(chart_locator)
    print("STEP 10: Switched to Chart mode")
    time.sleep(1)

    # STEP 11: Changing period 1m-1W
    periods = [
        "1m", "5m", "10m", "15m", "30m", "1h", "4h", "1D", "1W"
    ]
    for period in periods:
        period_locator = f"button.period-picker-chips.ets-chip.ets-chip-period.ng-star-inserted:text('{period}')"
        base_page.click_element_by_selector(period_locator)
        print(f"STEP 11: Changed chart period to {period}")
        time.sleep(1)

    # STEP 12: List kind of chart
    chart_list_locator = "div.chip-icon.icon-stocks"
    base_page.click_element_by_selector(chart_list_locator)
    print("STEP 12: Opened chart type list")
    time.sleep(3)

    # STEP 13: 'Column chart - position'
    column_locator = "div.ets-selection-text:text('Column')"
    base_page.click_element_by_selector(column_locator)
    print("STEP 13: Selected 'Column' chart type")
    time.sleep(1)

    # STEP 14: Back to Indices page
    indices_locator = "a[automation-id='breadcrumbs-name-indices']"
    base_page.click_element_by_selector(indices_locator)
    print("STEP 14: Returned to 'Indices' page")
    time.sleep(2)

    # STEP 15: Select SPX500 indicate
    spx500_locator = "div[automation-id='trade-item-name']:text('SPX500 ')"
    base_page.click_element_by_selector(spx500_locator)
    print("STEP 15: Selected 'SPX500' position")
    time.sleep(1)

    # STEP 16: Details - chart
    chart_locator_1 = "a[automation-id='et-tab-chart']:text('Chart')"
    base_page.click_element_by_selector(chart_locator_1)
    print("STEP 16: Switched to Chart mode for SPX500")
    time.sleep(1)

    # STEP 17: Select List kind of chart
    chart_list_locator1 = "div.chip-icon.icon-stocks"
    base_page.click_element_by_selector(chart_list_locator1)
    print("STEP 17: Opened chart type list for SPX500")
    time.sleep(3)

    # STEP 18: 'Baseline chart - position'
    baseline_locator = "div.ets-selection-text:text('Baseline')"
    base_page.click_element_by_selector(baseline_locator)
    print("STEP 18: Selected 'Baseline' chart type")
    time.sleep(1)

    print("Test case completed successfully - positive result.")

@pytest.fixture(scope="function")
def playwright_context():
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
    pytest.main(["-v", "--html=reports/test_allmarkets_report.html", "--self-contained-html"])
