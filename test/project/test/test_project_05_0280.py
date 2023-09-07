from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException
from common.ui.common import Common
from login.ui.elements import ADMIN_ID, ADMIN_PW
from login.ui.login import LabelEarth_login
from project.ui.project_list import ProjectList
from project.ui.project_task import ProjectTask
from project.ui.assignment_modal import AssignmentModal
from project.ui.text_present import is_text_present
import time
from utils.test_util import TestUtil


def test_project_05_0280(driver_fixture):
    LabelEarth_login(driver_fixture, ADMIN_ID, ADMIN_PW)
    project = ProjectList(driver_fixture)
    actions = ActionChains(driver_fixture)
    task = ProjectTask(driver_fixture)
    modal = AssignmentModal(driver_fixture)

    # 후에 기능 사라지면 삭제
    Common(driver_fixture).info.click()

    step_1_fail_message = "작업자 할당 모달창이 열리지 않음"
    time.sleep(1.5)
    actions.click(project.first_project).perform()
    #time.sleep(10)
    task.check_box.click()
    task.assign_worker_btn.click()
    assert is_text_present(driver_fixture, '작업자 할당'), step_1_fail_message

    step_2_fail_message = "이름으로 검색이 되지 않음"
    modal.search_bar.send_keys("admin")
    time.sleep(1)
    row_element = modal.row_result

    found_results = []
    if "검색에 대한 결과를 찾을 수 없습니다." not in row_element.text:  # 검색 결과가 없는 경우
        found_results.append(row_element.text)

    # 검색 결과가 1개 이상인 경우 성공으로 간주
    assert len(found_results) >= 1, step_2_fail_message
