from common.ui.common import Common
from login.ui.elements import ADMIN_ID, ADMIN_PW
from login.ui.login import LabelEarth_login
from project.ui.create_project import CreateProject
from project.ui.project_list import ProjectList
from selenium.webdriver.common.by import By
from project.ui.data_picker import is_aria_checked
from utils.test_util import TestUtil
import time

def test_project_02_0200(driver_fixture):
    LabelEarth_login(driver_fixture, ADMIN_ID, ADMIN_PW)
    project = ProjectList(driver_fixture)
    create = CreateProject(driver_fixture)

    # 후에 기능 사라지면 삭제
    Common(driver_fixture).info.click()

    step_1_fail_message = "종료일 지정 토글이 off가 아님"
    TestUtil.wait_time_until_find_element(driver_fixture, By.XPATH, "//*[contains(@class, ' progress-bar')]")
    project.creat_project.click()
    create.type_rbb.click()
    time.sleep(0.5)
    create.next_btn.click()
    toggle = create.date_toggle
    assert is_aria_checked(toggle, 'false'), step_1_fail_message


    step_2_fail_message = "종료일 지정 토글이 on이 아님"
    create.date_toggle.click()
    assert is_aria_checked(toggle, 'true'), step_2_fail_message
