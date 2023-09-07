from selenium.webdriver import ActionChains
from utils.test_util import TestUtil
from common.ui.common import Common
from login.ui.elements import ADMIN_ID, ADMIN_PW
from login.ui.login import LabelEarth_login
from project.ui.create_project import CreateProject
from project.ui.project_list import ProjectList
from selenium.webdriver.common.by import By
import time


def test_project_02_0140(driver_fixture):
    LabelEarth_login(driver_fixture, ADMIN_ID, ADMIN_PW)
    project = ProjectList(driver_fixture)
    create = CreateProject(driver_fixture)

    # 후에 기능 사라지면 삭제
    Common(driver_fixture).info.click()

    step_1_fail_message = "영상 불러오기 모달창이 생성 되지 않음"
    TestUtil.wait_time_until_find_element(driver_fixture, By.XPATH, "//*[contains(@class, ' progress-bar')]")
    project.creat_project.click()
    create.type_rbb.click()
    time.sleep(0.5)
    create.next_btn.click()
    create.scene.click()
    assert len(create.scene_modal) > 0, step_1_fail_message


    step_2_fail_message = "복사 성공 토스트 메세지가 생성되지 않음"
    ActionChains(driver_fixture).move_to_element(create.latlng).perform()
    create.latlng_copy.click()
    create.toast_message("경도/위도를 복사했습니다."), step_2_fail_message
