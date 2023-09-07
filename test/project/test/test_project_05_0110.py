from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from login.ui.elements import ADMIN_ID, ADMIN_PW
from login.ui.login import LabelEarth_login
from project.ui.project_list import ProjectList
from project.ui.project_task import ProjectTask
from project.ui.text_present import is_text_present

import time

from utils.test_util import TestUtil


def test_project_05_0110(driver_fixture):
    LabelEarth_login(driver_fixture, ADMIN_ID, ADMIN_PW)
    project = ProjectList(driver_fixture)
    actions = ActionChains(driver_fixture)
    task = ProjectTask(driver_fixture)

    step_1_fail_message = "작업 화면으로 이동 하지 못함"
    time.sleep(1.5)
    actions.move_to_element(project.first_project).click().perform()
    assert is_text_present(driver_fixture, '작업'), step_1_fail_message

    step_2_fail_message = "판독 탭 항목이 오름차순으로 보여지지 않음"
    time.sleep(5)
    TestUtil.wait_time_until_find_element(driver_fixture, By.XPATH, "//*[contains(@class, 'ant-table-thead')]//th[4]")
    task.worker.click()
    task.worker.click()
    time.sleep(1)
    assert task.worker.get_attribute("aria-sort") == "ascending", step_2_fail_message

    step_3_fail_message = "판독 탭 항이 내림차순으로 보여지지 않음"
    time.sleep(1)
    task.worker.click()
    time.sleep(1)
    assert task.worker.get_attribute("aria-sort") == "descending", step_3_fail_message
