from telnetlib import EC

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from login.ui.elements import ADMIN_ID, ADMIN_PW
from login.ui.login import LabelEarth_login
from project.ui.project_list import ProjectList
from project.ui.project_task import ProjectTask
from project.ui.text_present import is_text_present
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_project_05_0160(driver_fixture):
    LabelEarth_login(driver_fixture, ADMIN_ID, ADMIN_PW)
    project = ProjectList(driver_fixture)
    actions = ActionChains(driver_fixture)
    task = ProjectTask(driver_fixture)

    step_1_fail_message = "작업 화면으로 이동 하지 못함"
    time.sleep(1.5)
    actions.move_to_element(project.first_project).click().perform()
    assert is_text_present(driver_fixture, '작업'), step_1_fail_message


    step_2_fail_message = "작업 예정 필터링이 되지 않음"
    time.sleep(3)
    actions.move_to_element(task.job_status).perform()
    actions.click(task.job_status_filter).perform()
    task.upcoming_task.click()
    assert 'checkbox-checked' in task.upcoming_task.get_attribute('class'), step_2_fail_message


    step_3_fail_message = "필터가 초기화 되지 않음"
    task.filter_reset_btn.click()
    assert not is_text_present(driver_fixture, '필터 초기화'), step_3_fail_message
