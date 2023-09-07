from selenium.webdriver import ActionChains
from common.ui.common import Common
from login.ui.elements import ADMIN_ID, ADMIN_PW
from login.ui.login import LabelEarth_login
from project.ui.project_list import ProjectList
from project.ui.text_present import is_text_present
import time
from project.ui.create_project import *


def test_project_03_0010(driver_fixture):
    LabelEarth_login(driver_fixture, ADMIN_ID, ADMIN_PW)
    project = ProjectList(driver_fixture)
    create = CreateProject(driver_fixture)
    Common(driver_fixture).info.click()

    step_1_fail_message = "프로젝트 수정 화면으로 이동 하지 못함"
    ActionChains(project._driver).move_to_element(project.first_project).perform()
    project.kebab_btn.click()
    time.sleep(1)
    project.edit.click()
    assert is_text_present(driver_fixture, "프로젝트 수정"), step_1_fail_message


    step_2_fail_message = "프로젝트 수정 토스트 메세지가 노출 되지 않음"
    create.name_clear_bth.click()
    create.name.send_keys("test123")
    create.create_btn.click()
    time.sleep(1)
    assert create.success_msg.is_displayed(), step_2_fail_message
