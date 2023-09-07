from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from common.ui.elements.elements import PROFILE, LOGOUT
from login.ui.elements import *
from utils.config import Config
import time

class Login:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    @property
    def id_input(self):
        return self._driver.find_element(By.XPATH, ID_INPUT)

    @property
    def id_input_value(self):
        return self.id_input.get_attribute("value")

    @property
    def id_input_clear(self):
        return self._driver.find_element(By.XPATH, ID_CLEAR_BTN)

    @property
    def pw_input(self):
        return self._driver.find_element(By.XPATH, PW_INPUT)

    @property
    def pw_input_value(self):
        return self.pw_input.get_attribute("value")

    @property
    def pw_input_clear(self):
        return self._driver.find_element(By.XPATH, PW_CLEAR_BTN)

    @property
    def pw_invisible_btn(self):
        return self._driver.find_element(By.XPATH, PW_INVISIBLE_BTN)

    @property
    def pw_invisible_elements(self):
        element = self._driver.find_element(By.XPATH, "//input[@placeholder='비밀번호']")
        element_type = element.get_attribute('type')
        return element_type

    @property
    def login_btn(self):
        return self._driver.find_element(By.XPATH, LOGIN_BTN)

    @property
    def remember_me(self):
        return self._driver.find_element(By.XPATH, REMEMBER_ME)

    @property
    def alert(self):
        return self._driver.find_element(By.XPATH, ALERT)

    def alert_value(self):
        return self.alert.text


def LabelEarth(driver):
    config = Config()
    return config.user_web_url


def LabelEarth_login(driver, id_data, pw_data):
    config = Config()
    driver.get(config.user_web_url)
    driver.find_element(By.XPATH, ID_INPUT).send_keys(id_data)
    driver.find_element(By.XPATH, PW_INPUT).send_keys(pw_data)
    driver.find_element(By.XPATH, LOGIN_BTN).click()


def logout(driver_fixture):
    driver_fixture.find_element(By.XPATH, PROFILE).click()
    time.sleep(1.5)
    driver_fixture.find_element(By.XPATH, LOGOUT).click()
    time.sleep(1)
