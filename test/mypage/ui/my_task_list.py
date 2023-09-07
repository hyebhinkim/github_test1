from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from mypage.ui.elements.my_task_list_elements import *
class myTaskList:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    @property
    def search_bar(self):
        return self._driver.find_element(By.XPATH, SEARCH_BAR)

    @property
    def search_clear_btn(self):
        return self._driver.find_element(By.XPATH, SEARCH_CLEAR_BTN)

    @property
    def task_tab(self):
        return self._driver.find_element(By.XPATH, TASK_TAB)



class myPggeStatusFilter:
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



class myPageTypeFilter:
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
