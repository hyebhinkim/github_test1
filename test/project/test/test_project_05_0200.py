import pytest
from selenium.webdriver import ActionChains
from login.ui.elements import ADMIN_ID, ADMIN_PW
from login.ui.login import LabelEarth_login
from project.ui.assignment_log import AssignmentLog
from project.ui.project_list import ProjectList
from project.ui.text_present import is_text_present
import time



@pytest.mark.skip()
def test_project_05_0200(driver_fixture):
    LabelEarth_login(driver_fixture, ADMIN_ID, ADMIN_PW)
    project = ProjectList(driver_fixture)
    actions = ActionChains(driver_fixture)
    log = AssignmentLog(driver_fixture)

    step_1_fail_message = "작업자 할당 내역 모달창이 열리지 않음"
    time.sleep(1)
    actions.move_to_element(project.first_project).click().perform()
    log.worker_low.click()
    assert is_text_present(driver_fixture, '작업자 할당 내역'), step_1_fail_message


    step_2_fail_message = "할당일이 오름차순으로 보여지지 않음"
    log.assingment_date.click()
    assert log.assingment_date.get_attribute("aria-sort") == "ascending", step_2_fail_message


    step_3_fail_message = "할당일이 내림차순으로 보여지지 않음"
    log.assingment_date.click()
    assert log.assingment_date.get_attribute("aria-sort") == "descending", step_3_fail_message
