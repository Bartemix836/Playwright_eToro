import sys
import os
# Dodaj główny katalog projektu do PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import time
import pytest
from playwright.sync_api import sync_playwright
from pages.base_page import TestHelper

@pytest.mark.usefixtures("playwright_context")
def test_launch_browser(playwright_context):
    """
    Test case: Launch browser and perform interactions.
    Generates HTML Report automatically using pytest and Playwright.
    """
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
    time.sleep(4)

    # STEP 7: Click select list
    selectlist_locator="et-select-header:has-text('Currencies')"
    base_page.click_element_by_selector(selectlist_locator)
    time.sleep(1)

    # STEP 8: Select ETFs position
    etfs_locator="et-select-body-option:has-text('ETFs')"
    base_page.click_element_by_selector(etfs_locator)
    time.sleep(2)

    # STEP 9: Click All select-list
    all_locator="et-select-header:has-text('All')"
    base_page.click_element_by_selector(all_locator)
    time.sleep(1)

    # STEP10: Select London position
    london_locator = "et-select-body-option[automation-id='discover-market-etf-dropdown-item']:has-text('London')"
    base_page.click_element_by_selector(london_locator)
    time.sleep(2)

    # STEp 11: Sorted list by Change
    change_locator="div[automation-id='discover-market-results-change-head']:has-text('Change')"
    base_page.click_element_by_selector(change_locator)
    time.sleep(1)

    #STEP 12: Entry text to input:
    searchinp_locator="input[automation-id='search-autocomplete-input']"
    base_page.type_text_in_field(searchinp_locator,"GOLD")
    time.sleep(2)

    #STEP 13: Click searched position 'GOLD'
    gold_searched="span[automation-id='search-result-item-name']:text('GOLD') + span[automation-id='search-result-item-fullname']:text('Gold (Non Expiry)')"
    base_page.click_element_by_selector(gold_searched)
    time.sleep(1)












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
    pytest.main(["-v", "--html=reports/test_allmarkets_report.html", "--self-contained-html"])
