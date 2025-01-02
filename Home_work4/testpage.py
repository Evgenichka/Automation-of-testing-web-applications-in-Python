from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
name = testdata.get("username")

#локаторам даем осознанные имена заглавными буквами по стандарту PO
class TestSearchLocators:
    ids = dict()
    with open("./locators.yaml") as f:
        locators = yaml.save_load(f)
    for locator in locators["xpath"].keys():
        ids[locator] = (By.XPATH, locators["xpath"][locator])
    for locator in locators["css"].keys():
        ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])
    



class OperationsHelper(BasePage):

    def enter_login(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def click_login_button(self):
        logging.info("Click login button")
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=2)
        text = error_field.text
        logging.info(f"We find text {text} in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}")
        return text

    def get_user_text(self):
        user_field = self.find_element(TestSearchLocators.LOCATOR_HELLO, time=2)
        text = user_field.text
        logging.info(f"We find text {text} in error field {TestSearchLocators.LOCATOR_HELLO}")
        return text

    def click_create_post_button(self):
        logging.info("Click create post button")
        self.find_element(TestSearchLocators.LOCATOR_CREATE_BTN).click()

    def input_title_post(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_POST_TITLE_FIELD[1]}")
        title_field = self.find_element(TestSearchLocators.LOCATOR_POST_TITLE_FIELD)
        title_field.clear()
        title_field.send_keys(word)

    def input_description_post(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_POST_DESCRIPTION_FIELD[1]}")
        description_field = self.find_element(TestSearchLocators.LOCATOR_POST_DESCRIPTION_FIELD)
        description_field.clear()
        description_field.send_keys(word)

    def input_content_post(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_POST_CONTENT_FIELD[1]}")
        content_field = self.find_element(TestSearchLocators.LOCATOR_POST_CONTENT_FIELD)
        content_field.clear()
        content_field.send_keys(word)

    def click_save_post_button(self):
        logging.info("Click save post button")
        self.find_element(TestSearchLocators.LOCATOR_SAVE_BTN).click()

    def get_new_title_text(self):
        title_field = self.find_element(TestSearchLocators.LOCATOR_SEARCH_TITLE_FIELD, time=2)
        text = title_field.text
        logging.info(f"We find text {text} in error field {TestSearchLocators.LOCATOR_SEARCH_TITLE_FIELD[1]}")
        return text

    def click_create_contact(self):
        logging.info("Click create contact")
        self.find_element(TestSearchLocators.LOCATOR_CONTACT).click()

    def enter_your_name(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_YOUR_NAME_CONTACT[1]}")
        name_field = self.find_element(TestSearchLocators.LOCATOR_YOUR_NAME_CONTACT)
        name_field.clear()
        name_field.send_keys(word)

    def enter_your_email(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_YOUR_EMAIL_CONTACT[1]}")
        email_field = self.find_element(TestSearchLocators.LOCATOR_YOUR_EMAIL_CONTACT)
        email_field.clear()
        email_field.send_keys(word)

    def enter_your_content(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_CONTENT_CONTACT[1]}")
        content_field = self.find_element(TestSearchLocators.LOCATOR_CONTENT_CONTACT)
        content_field.clear()
        content_field.send_keys(word)

    def click_submit_contact(self):
        logging.info("Click submit contact")
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_BTN).click()

    def get_alert_text(self):
        alert_field = self.driver.switch_to.alert
        text = alert_field.text
        logging.info(f"We find text {text} in alert")
        return text
