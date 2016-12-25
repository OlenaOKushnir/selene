from selenium import webdriver

from selene import config
from selene.conditions import css_class
from selene.selene_driver import SeleneDriver
from tests.atomic.helpers.givenpage import GivenPage

__author__ = 'yashaka'

driver = SeleneDriver(webdriver.Firefox())
GIVEN_PAGE = GivenPage(driver)
WHEN = GIVEN_PAGE
original_timeout = config.timeout


def teardown_module(m):
    driver.quit()


def test_waits_nothing():
    GIVEN_PAGE.opened_empty()
    elements = driver.all('li').filtered_by(css_class('will-appear'))

    WHEN.load_body('''
                   <ul>Hello to:
                       <li>Anonymous</li>
                       <li class='will-appear'>Bob</li>
                       <li class='will-appear' style='display:none'>Kate</li>
                   </ul>''')
    assert len(elements) == 2

    WHEN.load_body_with_timeout('''
                                <ul>Hello to:
                                    <li>Anonymous</li>
                                    <li class='will-appear'>Bob</li>
                                    <li class='will-appear' style='display:none'>Kate</li>
                                    <li class='will-appear'>Joe</li>
                                </ul>''',
                                500)
    assert len(elements) == 2
