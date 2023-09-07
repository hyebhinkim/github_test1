from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from user.ui.elements.user_list_elements import *

class UserList:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    @property
    def serach_bar(self):
        return self._driver.find_element(By.XPATH, SEARCH_BAR)

    @property
    def mod_btn(self):
        return self._driver.find_element(By.XPATH, MOD_BTN)

    @property
    def pagenation(self):
        return self._driver.find_element(By.XPATH, PAGENATION)

    @property
    def page_50(self):
        return self._driver.find_element(By.XPATH, PAGE_50)

    @property
    def page_100(self):
        return self._driver.find_element(By.XPATH, PAGE_100)

    @property
    def page_150(self):
        return self._driver.find_element(By.XPATH, PAGE_150)
