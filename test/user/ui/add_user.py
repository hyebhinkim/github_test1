from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from user.ui.elements.addUser_elements import *

class addUser:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    @property
    def user_add_btn(self):
        return self._driver.find_element(By.XPATH, USER_ADD_BTN)

    @property
    def user_add_modal(self):
        return self._driver.find_element(By.XPATH, USER_ADD_MODAL)

    @property
    def email(self):
        return self._driver.find_element(By.XPATH, EMAIL)

    @property
    def eamil_celar_btn(self):
        return self._driver.find_element(By.XPATH, EMAIL_CLEAR_BTN)

    @property
    def password(self):
        return self._driver.find_element(By.XPATH, PASSWORD)

    @property
    def password_confirm(self):
        return self._driver.find_element(By.XPATH, PASSWORD_CONFIRM)

    @property
    def user_name(self):
        return self._driver.find_element(By.XPATH, USER_NAME)

    @property
    def role(self):
        return self._driver.find_element(By.XPATH, ROLE)

    @property
    def manager(self):
        return self._driver.find_element(By.XPATH, MANAGER)

    @property
    def annotator(self):
        return self._driver.find_element(By.XPATH, ANNOTATOR)

    @property
    def reviewer(self):
        return self._driver.find_element(By.XPATH, REVIEWER)

    @property
    def viewer(self):
        return self._driver.find_element(By.XPATH, VIEWER)

    @property
    def confirm_btn(self):
        return self._driver.find_element(By.XPATH, CONFIRN_BTN)
