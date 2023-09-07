import pytest
from selenium.webdriver import ActionChains
from login.ui.elements import ADMIN_ID, ADMIN_PW
from login.ui.login import LabelEarth_login
from project.ui.assignment_log import AssignmentLog
from project.ui.project_list import ProjectList
from project.ui.project_task import ProjectTask
from project.ui.text_present import is_text_present
import time



@pytest.mark.skip()
def test_project_05_0190(driver_fixture):
    LabelEarth_login(driver_fixture, ADMIN_ID, ADMIN_PW)
    project = ProjectList(driver_fixture)
    actions = ActionChains(driver_fixture)
    task = ProjectTask(driver_fixture)
    log = AssignmentLog(driver_fixture)

    step_1_fail_message = "작업자 할당 내역 모달창이 열리지 않음"
    time.sleep(1)
    actions.move_to_element(project.first_project).click().perform()
    log.worker_low.click()
    assert is_text_present(driver_fixture, '작업자 할당 내역'), step_1_fail_message


    step_2_fail_message = "이름으로 검색 되지 않음"
    log.search_bar.send_keys("admin")
    assert is_text_present(driver_fixture, "admin@labelearth.com"), step_2_fail_message


    step_3_fail_message = " 일시로 검색 되지 않음"
    log.search_clear_btn.click()
    log.search_bar.send_keys("2023-06-15")
    assert is_text_present(driver_fixture, "2023-06-15"), step_3_fail_message
