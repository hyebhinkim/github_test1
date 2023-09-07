import pytest
from selenium.webdriver import ActionChains
from webdriver_manager.core import driver

from login.ui.elements import ADMIN_ID, ADMIN_PW
from login.ui.login import LabelEarth_login
from project.ui.project_list import ProjectList
from project.ui.project_task import ProjectTask
from project.ui.text_present import is_text_present
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.skip()
def test_project_05_0070(driver_fixture):
    LabelEarth_login(driver_fixture, ADMIN_ID, ADMIN_PW)
    project = ProjectList(driver_fixture)
    actions = ActionChains(driver_fixture)
    task = ProjectTask(driver_fixture)


    step_1_fail_message = "작업 화면으로 이동 하지 못함"
    time.sleep(1)
    actions.move_to_element(project.first_project).click().perform()
    assert is_text_present(driver_fixture, '작업'), step_1_fail_message


    step_2_fail_message = "작업ID로 검색되지 않음"
    task.search_bar.send_keys("352")
    assert is_text_present(driver_fixture, '352'), step_2_fail_message


    step_3_fail_message = "작업자로 검색되지 않음"
    task.search_clear_btn.click()
    task.search_bar.send_keys("hyebhin")
    assert is_text_present(driver_fixture, "hyebhin"), step_3_fail_message
