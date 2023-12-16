from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import logging


class BasePage:

    def __init__(self, driver, url):
        self.driver = driver
        self.base_url = url

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator, time=2)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception(f'Exception with click')
            return False
        logging.info(f'Click {element_name} button')
        return True

    def filling_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f'Send {word} to element {element_name}')
        field = self.find_element(locator)
        if not field:
            logging.error(f'Element {locator} not found')
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f'Exception while operate with {locator}')
            return False
        return True

    def find_element(self, locator, time=10):
        try:
            element = WebDriverWait(self.driver, time).until(
                                    EC.presence_of_element_located(locator),
                                    message=f"Can't find element by locator {locator}")
        except:
            logging.exception('Find element exception')
            element = None
        return element

    def get_alert_text(self):
        try:
            alert = self.driver.switch_to.alert
            return alert.text
        except:
            logging.exception('Exception with alert')
            return None

    def get_element_property(self, locator, property_element):
        element = self.find_element(locator)
        if element:
            return element.value_of_css_property(property_element)
        else:
            logging.error(f'Property {property_element} not found in element with locator {locator}')
        return None

    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=2)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f'Exception while get text from {element_name}')
            return None
        logging.info(f'We find text {text} in field {element_name}')
        return text

    def go_to_site(self):
        try:
            start_browsing = self.driver.get(self.base_url)
        except:
            logging.exception('Exception while open site')
            start_browsing = None
        return start_browsing
