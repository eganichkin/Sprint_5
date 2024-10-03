import pytest
from selenium import webdriver
import random

MAIL_PREF = 'ganickin_14_'
MAIL_POST = '@yandex.ru'


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def random_correct_account():
    name = MAIL_PREF + '001' + str(random.randrange(100, 999))
    password = str(random.randrange(100000, 999999))
    return {'name': name, 'email': name + MAIL_POST, 'password': password}


@pytest.fixture
def random_incorrect_account():
    name = MAIL_PREF + '001' + str(random.randrange(100, 999))
    password = str(random.randrange(10000, 99999))
    return {'name': name, 'email': name + MAIL_POST, 'password': password}
