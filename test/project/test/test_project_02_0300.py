from common.ui.common import Common
from login.ui.elements import ADMIN_ID, ADMIN_PW
from login.ui.login import LabelEarth_login
from project.ui.create_project import CreateProject
from project.ui.project_list import ProjectList
from selenium.webdriver.common.by import By
from project.ui.text_present import is_text_present
from project.ui.alert_message import *


def test_project_02_0260(driver_fixture):
    LabelEarth_login(driver_fixture, ADMIN_ID, ADMIN_PW)
    project = ProjectList(driver_fixture)
    create = CreateProject(driver_fixture)
    # 후에 기능 사라지면 삭제
    Common(driver_fixture).info.click()


    step_1_fail_message = "라벨 클래스 아름 공백 alert 메세지가 노출되지 않음"
    project.creat_project.click()
    create.type_rbb.click()
    create.next_btn.click()
    create.add_label.click()
    create.label_description.click()
    assert is_text_present(driver_fixture, NAME_EMPTY), step_1_fail_message
