from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from project.ui.elements.assignment_modal_elements import *


class AssignmentModal:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    @property
    def search_bar(self):
        return self._driver.find_element(By.XPATH, SEARCH_BAR)

    @property
    def search_clear_btn(self):
        return self._driver.find_element(By.XPATH, SEARCH_CLEAR_BTN)


    @property
    def row_result(self):
        return self._driver.find_element(By.XPATH, ROW_RESEULT)
