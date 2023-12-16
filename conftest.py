import logging
import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from email_report import sendemail
import requests

with open('testdata.yaml', encoding='utf-8') as file:
    testdata = yaml.safe_load(file)

with open('config.yaml', encoding='utf-8') as file:
    data = yaml.safe_load(file)


@pytest.fixture()
def browser():
    if testdata['browser'] == "firefox":
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    elif testdata['browser'] == "chrome":
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def create_my_post(get_token):
    logging.info(f'Creating a post {data["title_my_post"]}')
    try:
        user_post = requests.post(url=data['url_post'],
                                  headers={'X-Auth-Token': get_token},
                                  params={'owner': 'Me',
                                          'title': data['title_my_post'],
                                          'description': data['description_my_post'],
                                          'content': data['content_my_post']})
    except:
        logging.exception(f'Post {data["title_my_post"]} not created')
        user_post = None
    return user_post


@pytest.fixture(autouse=True, scope='class')
def get_token():
    logging.info(f'Receiving a token for username {data["login"]}')
    try:
        user_token = requests.post(url=data['url_login'],
                                   data={'username': data['login'], 'password': data['passwd']}).json()['token']
    except:
        logging.exception('Wrong login or password')
        user_token = None
    return user_token


@pytest.fixture(autouse=True, scope='class')
def send_report_email():
    yield
    sendemail()
