from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from mypage.ui.elements.edit_info_elements import *

class editInfo:
    def __init__(self, driver: WebDriver):
        self._driver = driver


    @property
    def edit_info(self):
        return self._driver.find_element(By.XPATH, EDIT_INFO)

    @property
    def edit_password(self):
        return self._driver.find_element(By.XPATH, EDIT_PASSWORD)

    @property
    def current_password(self):
        return self._driver.find_element(By.XPATH, CURRENT_PASSWORD)

    @property
    def new_password(self):
        return self._driver.find_element(By.XPATH, NEW_PASSWORD)

    @property
    def new_password_confirm(self):
        return self._driver.find_element(By.XPATH, NEW_PASSWORD_CONFIRM)


    @property
    def cancle_btn(self):
        return self._driver.find_element(By.XPATH, CANCLE_BTN)

    @property
    def change_btn(self):
        return self._driver.find_element(By.XPATH, CHANGE_BTN)
