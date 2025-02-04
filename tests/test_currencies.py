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


    # STEP 6: Click the "Currencies" tab in the menu
    currencies_tab_locator = '//*[@id="main-menu"]/li[3]/ol/li[4]/a'
    base_page.click_element_by_selector(currencies_tab_locator)
    print("STEP 6: Clicked 'Currencies' tab")
    time.sleep(3)

    # STEP 7: Click the "USDCAD" from list
    usdcad_tab_locator = "div.symbol.ets-bold.ets-info:text('USDCAD')"
    base_page.click_element_by_selector(usdcad_tab_locator)
    print("STEP 7: Clicked 'USDCAD' position")
    time.sleep(3)

    # STEP 8: Changing period 1D-MAX
    periods = [
        "1D", "1W", "1M", "6M", "1Y", "3Y", "MAX"
    ]
    for period in periods:
        period_locator = f"button.time-period.ng-star-inserted:text('{period}')"
        base_page.click_element_by_selector(period_locator)
        print(f"STEP 8: Changed chart period to {period}")
        time.sleep(1)

    # STEP 9: Select Chart button
    chart_list_locator = "text='Chart'"
    base_page.click_element_by_selector(chart_list_locator)
    print("STEP 9: Selected Chart button")
    time.sleep(3)

    # STEP 10: Click Chart type list:
    chart_tp_locator='div.chip-icon.icon-stocks'
    # '<div _ngcontent-ng-c1361437874="" class="chip-icon icon-stocks"></div>'
    base_page.click_element_by_selector(chart_tp_locator)
    print('STEP 10: Click Chart type list')
    time.sleep(2)

    # STEP 11: Select Hi-lo chart:
    hilo_locator = "div.ets-selection-text:text('Hi-Lo')"
    base_page.click_element_by_selector(hilo_locator)
    print('STEP 11: Selected Hi-Lo chart')
    time.sleep(2)

    # STEP 12: Select Chart button
    overview_locator = "text='Overview'"
    base_page.click_element_by_selector(overview_locator)
    print("STEP 12: Selected Overview tab")
    time.sleep(2)

    # STEP 13: Scroll page down
    base_page.scroll_page_steps(2,500,1)
    print("STEP 13: Scroll page down")
    time.sleep(2)

    # STEP 14: SELECT EURGBP
    eurgbp_locator = "span.name-main.ets-bold.ng-star-inserted:text('EURGBP')"
    base_page.click_element_by_selector(eurgbp_locator)
    print("STEP 14: SELECT EURGBP")
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
