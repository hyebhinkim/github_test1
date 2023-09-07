import pytest
from selenium.webdriver import ActionChains
from login.ui.elements import ADMIN_ID, ADMIN_PW
from login.ui.login import LabelEarth_login
from project.ui.project_list import ProjectList
from project.ui.project_task import ProjectTask
from project.ui.text_present import is_text_present
import time



@pytest.mark.skip()
def test_project_05_0180(driver_fixture):
    LabelEarth_login(driver_fixture, ADMIN_ID, ADMIN_PW)
    project = ProjectList(driver_fixture)
    actions = ActionChains(driver_fixture)
    task = ProjectTask(driver_fixture)

    step_1_fail_message = "작업 화면으로 이동 하지 못함"
    time.sleep(1)
    actions.move_to_element(project.first_project).click().perform()
    time.sleep(1)
    assert is_text_present(driver_fixture, '작업'), step_1_fail_message


    step_2_fail_message = "작업자 할당 내역 모달창이 열리지 않음"
    task.worker_low.click()
    assert is_text_present(driver_fixture, '작업자 할당 내역'), step_2_fail_message
