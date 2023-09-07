from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from project.ui.elements.create_project_elements import *


class ProjectList:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    @property
    def search_bar(self):
        return self._driver.find_element(By.XPATH, SEARCH_BAR)

    @property
    def search_clear_btn(self):
        return self._driver.find_element(By.XPATH, SEARCH_CLEAR_BTN)

    @property
    def project_list(self):
        return self._driver.find_element(By.XPATH, PROJECT_LIST)

    @property
    def first_project(self):
        return self._driver.find_element(By.XPATH, FIRST_PROJECT)

    @property
    def creat_project(self):
        return self._driver.find_element(By.XPATH, CREATE_PROJECT)

    @property
    def progress_bar(self):
        return self._driver.find_element(By.XPATH, PROGRESS_BAR)

    @property
    def kebab_btn(self):
        return self._driver.find_element(By.XPATH, KEBAB_BTN)

    @property
    def edit(self):
        return self._driver.find_element(By.XPATH, EDIT)

    @property
    def delete(self):
        return self._driver.find_element(By.XPATH, DELETE)

    @property
    def delete_confirm(self):
        return self._driver.find_element(By.XPATH, DELETE_CONFIRM)




class Filter:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    @property
    def status_filter(self):
        return self._driver.find_element(By.XPATH, STATUS_FILTER)
    @property
    def pending(self):
        return self._driver.find_element(By.XPATH, PENDING)

    @property
    def in_progress(self):
        return self._driver.find_element(By.XPATH, IN_PROGRESS)

    @property
    def completed(self):
        return self._driver.find_element(By.XPATH, COMPLETED)



class TypeFilter:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    @property
    def type_filter(self):
        return self._driver.find_element(By.XPATH, TYPE_FILTER)

    @property
    def clear_btn(self):
        return self._driver.find_element(By.XPATH, CLEAR_BTN)

    @property
    def rbb(self):
        return self._driver.find_element(By.XPATH, RBB)

    @property
    def polyon(self):
        return self._driver.find_element(By.XPATH, POLYGON)

    def get_type_title(self, title):
        xpath = f"//*[contains(@class, 'ant-select-selection-item') and @title='{title}']"
        element = self._driver.find_element(By.XPATH, xpath)
        return element
