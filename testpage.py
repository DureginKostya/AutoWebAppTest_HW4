import yaml
from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import requests


class TestSearchLocator:

    ids = dict()
    with open('locators.yaml', encoding='utf-8') as file:
        locators = yaml.safe_load(file)
    for locator in locators['xpath'].keys():
        ids[locator] = (By.XPATH, locators['xpath'][locator])
    with open('descriptions.yaml', encoding='utf-8') as file:
        dsr = yaml.safe_load(file)
    with open('config.yaml', encoding='utf-8') as file:
        data_api = yaml.safe_load(file)


class OperationHelperUI(BasePage):

    def get_alert(self):
        logging.info('Get alert text')
        text = self.get_alert_text()
        logging.info(text)
        return text

    def get_error_text(self):
        return self.get_text_from_element(TestSearchLocator.ids['LOCATOR_ERROR_FIELD'],
                                          description=TestSearchLocator.dsr['LOCATOR_ERROR_FIELD'])

    def get_text_blog(self):
        return self.get_text_from_element(TestSearchLocator.ids['LOCATOR_LABEL_BLOG'],
                                          description=TestSearchLocator.dsr['LOCATOR_LABEL_BLOG'])

    def get_title_new_post(self):
        return self.get_text_from_element(TestSearchLocator.ids['LOCATOR_TITLE_NEW_POST'],
                                          description=TestSearchLocator.dsr['LOCATOR_TITLE_NEW_POST'])

    def get_title_contact_us(self):
        return self.get_text_from_element(TestSearchLocator.ids['LOCATOR_TITLE_CONTACT_US'],
                                          description=TestSearchLocator.dsr['LOCATOR_TITLE_CONTACT_US'])


class OperationHelperAPI:

    def get_list_posts(self, user_url, user_token, whose, field, order=None):
        logging.debug(f'List formation {field}')
        try:
            res_get = requests.get(url=user_url,
                                   headers={'X-Auth-Token': user_token},
                                   params={'owner': whose, 'order': order}).json()['data']
            result = [item[field] for item in res_get]
        except:
            logging.exception(f'Failed to create list {field}')
            return None
        return result

    def get_list_my_posts(self, user_token):
        return self.get_list_posts(TestSearchLocator.data_api['url_post'], user_token, 'Me',
                                   TestSearchLocator.data_api['condition_field_me'])

    def get_list_not_my_posts(self, user_token):
        return self.get_list_posts(TestSearchLocator.data_api['url_post'], user_token, 'notMe',
                                   TestSearchLocator.data_api['condition_field_not_me'], 'ASC')
