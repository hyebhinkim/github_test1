from common.ui.common import Common
from login.ui.elements import ADMIN_ID, ADMIN_PW
from login.ui.login import LabelEarth_login
from project.ui.create_project import CreateProject
from project.ui.project_list import ProjectList
from selenium.webdriver.common.by import By
from project.ui.text_present import is_text_present
from project.ui.alert_message import *
from utils.test_util import TestUtil
import time

def test_project_02_0260(driver_fixture):
    LabelEarth_login(driver_fixture, ADMIN_ID, ADMIN_PW)
    project = ProjectList(driver_fixture)
    create = CreateProject(driver_fixture)
    # 후에 기능 사라지면 삭제
    Common(driver_fixture).info.click()


    step_1_fail_message = "클래스 추가 모달창이 생성되지 않음"
    TestUtil.wait_time_until_find_element(driver_fixture, By.XPATH, "//*[contains(@class, ' progress-bar')]")
    project.creat_project.click()
    create.type_rbb.click()
    time.sleep(0.5)
    create.next_btn.click()
    create.add_label.click()
    assert is_text_present(driver_fixture, '클래스 추가'),step_1_fail_message


    step_2_fail_message = "라벨 클래스가 추가 되지 않음"
    create.label_name.send_keys("label-1")
    create.add_label_btn.click()
    assert is_text_present(driver_fixture, 'label-1'), step_2_fail_message


    step_3_fail_message = "라벨 클래스 아름이 중복 alert 메세지가 노출되지 않음"
    create.add_label.click()
    create.label_name.send_keys("label-1")
    create.add_label_btn.click()
    assert is_text_present(driver_fixture, NAMING_COLLISION), step_3_fail_message
