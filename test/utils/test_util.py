import os
from time import sleep
from typing import Callable
from selenium.webdriver.remote.webelement import WebElement
from utils.assert_wait import AssertWait
from utils.initial_values import SELENIUM_IMPLICITLY_WAIT_INITIAL_VALUE
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
class TestUtil:
    @staticmethod
    def get_cwd() -> str:
        cwd = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
        return cwd

    @staticmethod
    def find_element_without_waiting(item_element: WebElement, by: By, value: str, driver: WebDriver) -> WebElement:
        """대기 없이 element를 찾아 리턴합니다."""
        try:
            driver.implicitly_wait(0)
            return item_element.find_element(by, value)
        finally:
            driver.implicitly_wait(SELENIUM_IMPLICITLY_WAIT_INITIAL_VALUE)

    @staticmethod
    def check_element_exist_without_waiting(driver: WebDriver, by: By, value: str) -> bool:
        """대기 없이 element의 존재 여부를 리턴합니다."""
        try:
            driver.implicitly_wait(0)
            return TestUtil.exist_element(driver, by, value)
        finally:
            driver.implicitly_wait(SELENIUM_IMPLICITLY_WAIT_INITIAL_VALUE)

    @staticmethod
    def not_exist_element(driver: WebDriver, by: By, value: str) -> bool:
        """element가 없는 경우 True 를 리턴합니다. element가 있다면 기본 대기 시간 동안 기다리며 없어지는지 확인합니다."""
        try:
            driver.implicitly_wait(0)
            return AssertWait().wait(lambda: not TestUtil.exist_element(driver, by, value))
        finally:
            driver.implicitly_wait(SELENIUM_IMPLICITLY_WAIT_INITIAL_VALUE)

    @staticmethod
    def exist_element(driver: WebDriver, by: By, value: str) -> bool:
        """element 의 존재 여부를 리턴합니다."""
        if len(driver.find_elements(by, value)) > 0:
            return True
        else:
            return False


    @staticmethod
    def wait(function: Callable, wait_second: int = SELENIUM_IMPLICITLY_WAIT_INITIAL_VALUE) -> bool:
        """
        function이 성공할 때까지 재시도, 기본 대기 시간이 지나면 실패
        :param function: 수행하고자 하는 함수
        :param wait_second: 대기 시간 (초), 기본 값은 SELENIUM_IMPLICITLY_WAIT_INITIAL_VALUE
        :return: function이 성공하면 True, 기본 대기 시간이 지나면 False 반환
        """
        for _ in range(0, wait_second * 2):
            if function():
                return True
            sleep(0.5)
        return False

    @staticmethod
    def wait_time_until_find_element(driver, by, value):
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((by, value)))


    @staticmethod
    def wait_clickable(driver: WebDriver, by: By, value: str) -> None:
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((by, value)))

    @staticmethod
    def wait_time_and_click(driver: WebDriver, by: By, value: str, timeout=15):
        try:
            element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value)))
            element.click()
        except TimeoutException:
            raise TimeoutException(f"Element with {by}={value} was not found and clickable within {timeout} seconds.")
