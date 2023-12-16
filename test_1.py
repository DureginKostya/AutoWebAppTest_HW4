from testpage import OperationHelperUI, TestSearchLocator, OperationHelperAPI
import yaml
import logging
import time

with open("testdata.yaml", encoding='utf-8') as file:
    testdata = yaml.safe_load(file)


class TestUI:

    def test_step1(self, browser):
        logging.info('Test 1 - Star')
        test_page = OperationHelperUI(browser, testdata['address'])
        test_page.go_to_site()
        test_page.filling_field(TestSearchLocator.ids['LOCATOR_LOGIN_FIELD'], testdata['failed_login'],
                                TestSearchLocator.dsr['LOCATOR_LOGIN_FIELD'])
        test_page.filling_field(TestSearchLocator.ids['LOCATOR_PASS_FIELD'], testdata['failed_passwd'],
                                TestSearchLocator.dsr['LOCATOR_PASS_FIELD'])
        test_page.click_button(TestSearchLocator.ids['LOCATOR_LOGIN_BTN'],
                               TestSearchLocator.dsr['LOCATOR_LOGIN_BTN'])
        assert test_page.get_error_text() == '401'
        logging.info('Test 1 - Finish')

    def test_step2(self, browser):
        logging.info('Test 2 - Star')
        test_page = OperationHelperUI(browser, testdata['address'])
        test_page.go_to_site()
        test_page.filling_field(TestSearchLocator.ids['LOCATOR_LOGIN_FIELD'], testdata['login'],
                                TestSearchLocator.dsr['LOCATOR_LOGIN_FIELD'])
        test_page.filling_field(TestSearchLocator.ids['LOCATOR_PASS_FIELD'], testdata['passwd'],
                                TestSearchLocator.dsr['LOCATOR_PASS_FIELD'])
        test_page.click_button(TestSearchLocator.ids['LOCATOR_LOGIN_BTN'], TestSearchLocator.dsr['LOCATOR_LOGIN_BTN'])
        assert test_page.get_text_blog() == 'Blog'
        logging.info('Test 2 - Finish')

    def test_step3(self, browser):
        logging.info('Test 3 - Star')
        test_page = OperationHelperUI(browser, testdata['address'])
        test_page.go_to_site()
        test_page.filling_field(TestSearchLocator.ids['LOCATOR_LOGIN_FIELD'], testdata['login'],
                                TestSearchLocator.dsr['LOCATOR_LOGIN_FIELD'])
        test_page.filling_field(TestSearchLocator.ids['LOCATOR_PASS_FIELD'], testdata['passwd'],
                                TestSearchLocator.dsr['LOCATOR_PASS_FIELD'])
        test_page.click_button(TestSearchLocator.ids['LOCATOR_LOGIN_BTN'], TestSearchLocator.dsr['LOCATOR_LOGIN_BTN'])
        test_page.click_button(TestSearchLocator.ids['LOCATOR_CREATE_NEW_BLOG_BTN'],
                               TestSearchLocator.dsr['LOCATOR_CREATE_NEW_BLOG_BTN'])
        test_page.filling_field(TestSearchLocator.ids['LOCATOR_NEW_TITLE'], testdata['title_new_post'],
                                TestSearchLocator.dsr['LOCATOR_NEW_TITLE'])
        test_page.filling_field(TestSearchLocator.ids['LOCATOR_NEW_DESCRIPTION'], testdata['description_new_post'],
                                TestSearchLocator.dsr['LOCATOR_NEW_DESCRIPTION'])
        test_page.filling_field(TestSearchLocator.ids['LOCATOR_NEW_CONTENT'], testdata['content_new_post'],
                                TestSearchLocator.dsr['LOCATOR_NEW_CONTENT'])
        test_page.filling_field(TestSearchLocator.ids['LOCATOR_DATE_CREATE_POST'], testdata['date_created'],
                                TestSearchLocator.ids['LOCATOR_DATE_CREATE_POST'])
        test_page.click_button(TestSearchLocator.ids['LOCATOR_SAVE_BTN'], TestSearchLocator.dsr['LOCATOR_SAVE_BTN'])
        time.sleep(2)
        assert test_page.get_title_new_post() == testdata['title_new_post']
        logging.info('Test 3 - Finish')

    def test_step4(self, browser):
        logging.info('Test 4 - Star')
        test_page = OperationHelperUI(browser, testdata['address'])
        test_page.go_to_site()
        test_page.filling_field(TestSearchLocator.ids['LOCATOR_LOGIN_FIELD'], testdata['login'],
                                TestSearchLocator.dsr['LOCATOR_LOGIN_FIELD'])
        test_page.filling_field(TestSearchLocator.ids['LOCATOR_PASS_FIELD'], testdata['passwd'],
                                TestSearchLocator.dsr['LOCATOR_PASS_FIELD'])
        test_page.click_button(TestSearchLocator.ids['LOCATOR_LOGIN_BTN'], TestSearchLocator.dsr['LOCATOR_LOGIN_BTN'])
        test_page.click_button(TestSearchLocator.ids['LOCATOR_CONTACT_BTN'],
                               TestSearchLocator.dsr['LOCATOR_CONTACT_BTN'])
        time.sleep(2)
        assert test_page.get_title_contact_us() == 'Contact us!'
        logging.info('Test 4 - Finish')

    def test_step5(self, browser):
        logging.info('Test 5 - Star')
        test_page = OperationHelperUI(browser, testdata['address'])
        test_page.go_to_site()
        test_page.filling_field(TestSearchLocator.ids['LOCATOR_LOGIN_FIELD'], testdata['login'],
                                TestSearchLocator.dsr['LOCATOR_LOGIN_FIELD'])
        test_page.filling_field(TestSearchLocator.ids['LOCATOR_PASS_FIELD'], testdata['passwd'],
                                TestSearchLocator.dsr['LOCATOR_PASS_FIELD'])
        test_page.click_button(TestSearchLocator.ids['LOCATOR_LOGIN_BTN'], TestSearchLocator.dsr['LOCATOR_LOGIN_BTN'])
        test_page.click_button(TestSearchLocator.ids['LOCATOR_CONTACT_BTN'],
                               TestSearchLocator.dsr['LOCATOR_CONTACT_BTN'])
        test_page.filling_field(TestSearchLocator.ids['LOCATOR_NAME_CONTACT_FIELD'], testdata['your_name_new'],
                                TestSearchLocator.dsr['LOCATOR_NAME_CONTACT_FIELD'])
        test_page.filling_field(TestSearchLocator.ids['LOCATOR_EMAIL_CONTACT_FIELD'], testdata['email_new'],
                                TestSearchLocator.dsr['LOCATOR_EMAIL_CONTACT_FIELD'])
        test_page.filling_field(TestSearchLocator.ids['LOCATOR_CONTENT_CONTACT_FIELD'], testdata['content_new_contact'],
                                TestSearchLocator.dsr['LOCATOR_CONTENT_CONTACT_FIELD'])
        test_page.click_button(TestSearchLocator.ids['LOCATOR_CONTACT_US_BTN'],
                               TestSearchLocator.dsr['LOCATOR_CONTACT_US_BTN'])
        time.sleep(2)
        assert test_page.get_alert() == testdata['message_alert']
        logging.info('Test 5 - Finish')


class TestAPI:

    def test_step6(self, get_token):
        logging.info('Test 6 - Star')
        assert TestSearchLocator.data_api['title_not_my_post'] in OperationHelperAPI().get_list_not_my_posts(get_token)
        logging.info('Test 6 - Finish')

    def test_step7(self, get_token, create_my_post):
        logging.info('Test 7 - Star')
        assert TestSearchLocator.data_api['description_my_post'] in OperationHelperAPI().get_list_my_posts(get_token)
        logging.info('Test 7 - Finish')
