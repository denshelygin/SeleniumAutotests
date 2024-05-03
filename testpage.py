from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import time
import yaml


ids = dict()
with open('locators.yaml') as f:
    locators = yaml.safe_load(f)
for locator in locators['xpath'].keys():
    ids[locator] = (By.XPATH, locators['xpath'][locator])
for locator in locators['css'].keys():
    ids[locator] = (By.CSS_SELECTOR, locators['css'][locator])

class OperationsHelper(BasePage):
    def enter_text_into_field(self, locator, word, description=None):
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
            logging.exception(f'Exception while operation with {locator}')
            return False
        return True

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception('Exception with click')
            return False
        logging.debug(f'Clicked {element_name} button')
        return True

    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f'Exception while get test from {element_name}')
            return None
        logging.debug(f'We find text {text} in field {element_name}')
        return text




# ENTER TEXT
    def enter_login(self, word):
        self.enter_text_into_field(ids['LOCATOR_LOGIN_FIELD'], word, description='login form')

    def enter_pass(self, word):
        self.enter_text_into_field(ids['LOCATOR_PASS_FIELD'], word, description='pass form')

    def enter_title(self, word):
        self.enter_text_into_field(ids['LOCATOR_TITLE_POST'], word, description='title form')

    def enter_description(self, word):
        self.enter_text_into_field(ids['LOCATOR_DESCRIPTION_POST'], word,
                                   description='description form')

    def enter_content(self, word):
        self.enter_text_into_field(ids['LOCATOR_CONTENT_POST'], word, description='content form')

    def add_name(self, word):
        self.enter_text_into_field(ids['LOCATOR_NAME'], word, description='name form')

    def add_email(self, word):
        self.enter_text_into_field(ids['LOCATOR_EMAIL'], word, description='email form')

    def add_content(self, word):
        self.enter_text_into_field(ids['LOCATOR_CONTACT_CONTENT'], word,
                                   description='content_contact form')

#CLICK
    def click_login_button(self):
        self.click_button(ids['LOCATOR_LOGIN_BTN'], description='login')

    def click_add_post_button(self):
        self.click_button(ids['LOCATOR_ADD_POST'], description='add post')

    def click_delete_post(self):
        self.click_button(ids['LOCATOR_DELETE_POST'], description='delete post')

    def click_post(self):
        self.click_button(ids['LOCATOR_CLICK_POST'], description='click post')

    def click_contact_us_button(self):
        self.click_button(ids['LOCATOR_CONTACT_US_BTN'], description='contact us')

    def click_safe_post_button(self):
        self.click_button(ids['LOCATOR_SAFE_BTN'], description='safe')

    def click_contact_btn(self):
        self.click_button(ids['LOCATOR_CONTACT_BTN'], description='contact')


# GET TEXT
    def get_error_text(self):
        return self.get_text_from_element(ids['LOCATOR_ERROR_FIELD'], description='error text')

    def login_success(self):
        return self.get_text_from_element(ids['LOCATOR_SUCCESS'], description='login')

    def find_new_post_title(self):
        return self.get_text_from_element(ids['LOCATOR_FIND_NEW_POST'], description='new title')

    def find_post_title(self):
        return self.get_text_from_element(ids['LOCATOR_FIND_POST'], description='title')

    def get_alert_message(self):
        time.sleep(1)
        logging.info("Get alert message")
        txt = self.get_alert_txt()
        logging.info(f"Alert message is {txt}")
        return txt

