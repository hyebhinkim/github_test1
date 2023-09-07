from selenium.webdriver import ActionChains

from common.ui.common import Common
from login.ui.elements import ADMIN_ID, ADMIN_PW
from login.ui.login import LabelEarth_login
from project.ui.project_list import ProjectList
from project.ui.project_task import ProjectTask
import time
from project.ui.text_present import is_text_present
from selenium.webdriver.common.by import By


def test_project_05_0250(driver_fixture):
    LabelEarth_login(driver_fixture, ADMIN_ID, ADMIN_PW)
    project = ProjectList(driver_fixture)
    actions = ActionChains(driver_fixture)
    task = ProjectTask(driver_fixture)

    # 후에 기능 사라지면 삭제
    Common(driver_fixture).info.click()

    step_1_fail_message = "작업자 할당 모달창이 열리지 않음"
    time.sleep(1.5)
    actions.click(project.first_project).perform()
    task.check_box.click()
    task.assign_worker_btn.click()
    assert is_text_present(driver_fixture, '작업자 할당'), step_1_fail_message


    step_2_fail_message = "현재 할당된 작업수가 오름차순으로 보여지지 않음"
    time.sleep(1)
    actions.click(task.current_task_count).perform()
    assert task.current_task_count.get_attribute("aria-sort") == "ascending", step_2_fail_message


    step_3_fail_message = "현재 할당된 작업수가 내림차순으로 보여지지 않음"
    task.current_task_count.click()
    assert task.current_task_count.get_attribute("aria-sort") == "descending", step_3_fail_message
