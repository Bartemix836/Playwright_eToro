from playwright.sync_api import Page
import time

class TestHelper:
    def __init__(self, page: Page):
        self.page = page

    def click_element_by_text(self, text_fragment: str):
        element_locator = self.page.locator(f'text={text_fragment}')

        try:
            element_locator.wait_for(timeout=3000)
            element_locator.click()
            print(f"Clicked on the element containing text: '{text_fragment}'")
        except Exception as e:
            print(f"Could not find or click the element containing text: '{text_fragment}'. Error: {e}")

    def hover_element_by_text(self, text_fragment: str):
        # Locate the element containing the text, regardless of its location
        element_locator = self.page.locator(f'text={text_fragment}')

        try:
            # Check if the element exists and is visible within a limited time
            element_locator.wait_for(timeout=3000)
            element_locator.hover()
            print(f"Hovered over the element containing text: '{text_fragment}'")
        except Exception as e:
            print(f"Could not find or hover over the element containing text: '{text_fragment}'. Error: {e}")

    def click_element_by_selector(self, selector: str):
        """
        Clicks an element based on its selector.
        :param selector: The element selector (e.g., "a[href='/discover/markets/stocks']").
        """
        element_locator = self.page.locator(selector)
        try:
            # Check if the element exists and is visible within a limited time
            element_locator.wait_for(state="visible", timeout=5000)
            element_locator.click()
            print(f"Clicked on the element with selector: '{selector}'")
        except Exception as e:
            print(f"Could not find or click the element with selector: '{selector}'. Error: {e}")

    def scroll_page_steps(self, steps: int = 3, distance: int = 700, delay: float = 1):
        """
        Scrolls the page in multiple steps.
        :param steps: Number of scrolling steps (default is 3).
        :param distance: Scrolling distance in pixels per step (default is 700).
        :param delay: Delay in seconds between scrolling steps (default is 1 second).
        """
        try:
            for i in range(steps):
                self.page.mouse.wheel(0, distance)
                time.sleep(delay)
                print(f"Scrolled step {i + 1} by {distance} pixels")
        except Exception as e:
            print(f"An error occurred while scrolling the page: {e}")

    def type_text_in_field(self, field_selector: str, text_to_type: str):
        """
        Types the specified text into the input field identified by the given selector.
        Ensures the field is ready for interaction and types text.

        Args:
            field_selector (str): The selector for the input field (e.g., CSS or XPath).
            text_to_type (str): The text to type into the input field.
        """
        try:
            # Locate the input field
            input_field = self.page.locator(field_selector)

            # Wait for the element to become visible
            input_field.wait_for(state="visible", timeout=15000)  # Increased timeout to 15s

            # Click the input field to activate it
            input_field.click()

            # Clear existing text and type new text
            input_field.fill("")  # Remove existing text
            input_field.type(text_to_type)  # Type the new text

            print(f"Typed '{text_to_type}' into the field with selector '{field_selector}'.")
        except Exception as e:
            print(f"Failed to type into the field with selector '{field_selector}'. Error: {e}")

    def type_text_using_keyboard(self, text_to_type: str):
        try:
            # Focus on the active page element to start typing
            self.page.focus("body")  # Adjust this to a specific input element if needed

            # Press each key in the given text
            for char in text_to_type:
                self.page.keyboard.press(char)
                print(f"Pressed key: {char}")
            print(f"Successfully typed the text: '{text_to_type}' using the keyboard.")
        except Exception as e:
            print(f"Failed to type text '{text_to_type}' using the keyboard. Error: {e}")

    def hover_over_element_by_selector(self, locator: str):
        """
        Hovers over an element based on the provided CSS selector with optional text filtering
        (e.g., ":text('EURGBP')").

        :param locator: CSS-style selector for the element, e.g., "span.name-main.ets-bold.ng-star-inserted:text('EURGBP')".
        """
        try:
            element = self.page.locator(locator)

            # Wait for the element to become visible
            element.wait_for(state="visible", timeout=5000)  # Set timeout to 5 seconds

            # Hover over the element
            element.hover()
            print(f"Hovered over the element: {locator}")
        except Exception as e:
            print(f"Error while hovering over element {locator}: {e}")

    def load_page(self, url: str):
        """
        Loads a webpage at the specified URL.

        :param url: The URL of the page to load.
        """
        try:
            self.page.goto(url, timeout=10000)  # Load the page with a 10-second timeout
            print(f"Loaded the page: {url}")
        except Exception as e:
            print(f"Error while loading the page: {url}. Error: {e}")
