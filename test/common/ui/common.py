
from selenium.webdriver.remote.webdriver import WebDriver
from common.ui.elements.elements import *
from selenium.webdriver.common.by import By

class Common:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    @property
    def info(self):
        return self._driver.find_element(By.XPATH, INFO)

    @property
    def user_managment(self):
        return self._driver.find_element(By.XPATH, USER_MANAGMENT)


    @property
    def profile(self):
        return self._driver.find_element(By.XPATH, PROFILE)

    @property
    def logout(self):
        return self._driver.find_element(By.XPATH, LOGOUT)

    @property
    def mypage(self):
        return self._driver.find_element(By.XPATH, MY_PAGE)
