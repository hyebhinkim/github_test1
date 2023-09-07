from time import sleep
from typing import Callable

from utils.initial_values import SELENIUM_IMPLICITLY_WAIT_INITIAL_VALUE


class AssertWait:
    @staticmethod
    def same(
        actual_function: Callable,
        expected_function: Callable,
        fail_message: str,
        wait_second: int = SELENIUM_IMPLICITLY_WAIT_INITIAL_VALUE,
    ):
        """
        actual 의 결과가 expected 의 결과와 다를 경우, 동일한 결과를 얻을 때까지 재시도, 대기 시간이 지나면 실패로 처리
        :param actual_function: 실제 값을 리턴 하는 함수
        :param expected_function: 예상 값을 리턴 하는 함수
        :param fail_message: 실패 메시지
        :param wait_second: 대기 시간 (초), 기본 값은 SELENIUM_IMPLICITLY_WAIT_INITIAL_VALUE
        :return: 없음
        """
        for _ in range(0, wait_second * 2):
            if actual_function() == expected_function():
                return
            sleep(0.5)
        assert actual_function() == expected_function(), fail_message

    @staticmethod
    def diff(
        actual_function: Callable,
        expected_function: Callable,
        fail_message: str,
        wait_second: int = SELENIUM_IMPLICITLY_WAIT_INITIAL_VALUE,
    ):
        """
        actual 의 결과가 expected 의 결과와 다를 경우, 동일한 결과를 얻을 때까지 재시도, 대기 시간이 지나면 실패로 처리
        :param actual_function: 실제 값을 리턴 하는 함수
        :param expected_function: 예상 값을 리턴 하는 함수
        :param fail_message: 실패 메시지
        :param wait_second: 대기 시간 (초), 기본 값은 SELENIUM_IMPLICITLY_WAIT_INITIAL_VALUE
        :return: 없음
        """
        for _ in range(0, wait_second * 2):
            if actual_function() == expected_function():
                return
            sleep(0.5)
        assert actual_function() == expected_function(), fail_message

    @staticmethod
    def true(function: Callable, fail_message: str, wait_second: int = SELENIUM_IMPLICITLY_WAIT_INITIAL_VALUE):
        """
        전달한 함수가 False 를 리턴 하는 경우 성공할 때까지 재시도, 대기 시간이 지나면 실패로 처리
        :param function: 실제 값을 리턴 하는 함수
        :param fail_message: 실패 메시지
        :param wait_second: 대기 시간 (초), 기본 값은 SELENIUM_IMPLICITLY_WAIT_INITIAL_VALUE
        :return: 없음
        """
        AssertWait.same(function, lambda: True, fail_message, wait_second)

    @staticmethod
    def false(function: Callable, fail_message: str, wait_second: int = SELENIUM_IMPLICITLY_WAIT_INITIAL_VALUE):
        """
        전달한 함수가 True 를 리턴 하는 경우 실패할 때까지 재시도, 대기 시간이 지나면 실패로 처리
        :param function: 실제 값을 리턴 하는 함수
        :param fail_message: 실패 메시지
        :param wait_second: 대기 시간 (초), 기본 값은 SELENIUM_IMPLICITLY_WAIT_INITIAL_VALUE
        :return: 없음
        """
        AssertWait.same(function, lambda: False, fail_message, wait_second)
