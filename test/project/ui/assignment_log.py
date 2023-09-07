from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from project.ui.elements.assignment_log_elements import *

class AssignmentLog:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    @property
    def worker_low(self):
        return self._driver.find_element(By.XPATH, WORKER_LOW)

    @property
    def search_bar(self):
        return self._driver.find_element(By.XPATH, SEARCH_BAR)


    @property
    def search_clear_btn(self):
        return self._driver.find_element(By.XPATH, SEARCH_CLEAR_BTN)

    @property
    def assingment_date(self):
        return self._driver.find_element(By.XPATH, ASSIGNMENT_DATE)
