import time
from testpage import OperationsHelper
import logging
import yaml

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)


def test_login_negative(browser):
    logging.info("test_login_negative starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login('test')
    testpage.enter_pass('test')
    testpage.click_login_button()
    assert testpage.get_error_text() == "401", "test_step1 FAILED"


def test_login_positive(browser):
    logging.info("test_login_positive starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata['login'])
    testpage.enter_pass(testdata['password'])
    testpage.click_login_button()
    assert testpage.login_success() == f"Hello, {testdata['login']}", "test_step2 FAILED"


def test_add_post(browser):
    logging.info("test_add_post starting")
    testpage = OperationsHelper(browser)
    #testpage.go_to_site()
    #testpage.enter_login(testdata['login'])
    #testpage.enter_pass(testdata['password'])
    #testpage.click_login_button()
    testpage.click_add_post_button()
    testpage.enter_title(testdata['title'])
    testpage.enter_description(testdata['description'])
    testpage.enter_content(testdata['content'])
    testpage.click_safe_post_button()
    time.sleep(3)
    assert testpage.find_new_post_title() == f'{testdata["title"]}', "test_add_post FAILED"


def test_delete_post(browser):
    logging.info("test_delete_post starting")
    testpage = OperationsHelper(browser)
    #testpage.go_to_site()
    #testpage.enter_login(testdata['login'])
    #testpage.enter_pass(testdata['password'])
    #testpage.click_login_button()
    testpage.click_post()
    testpage.click_delete_post()
    assert testpage.find_post_title() != f'{testdata["title"]}', "test_delete_post FAILED"


def test_add_contact(browser):
    logging.info("test_add_contact starting")
    testpage = OperationsHelper(browser)
    #testpage.go_to_site()
    #testpage.enter_login(testdata['login'])
    #testpage.enter_pass(testdata['password'])
    #testpage.click_login_button()
    testpage.click_contact_btn()
    testpage.add_name(testdata['name'])
    testpage.add_email(testdata['email'])
    testpage.add_content(testdata['content_contact'])
    testpage.click_contact_us_button()
    assert testpage.get_alert_message() == "Form successfully submitted", "test contact us FAILED!"

