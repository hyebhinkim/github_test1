from selenium.webdriver.common.by import By
from common.fixture.text_type_fixture import TextTypeFixture
from common.ui.common import Common
from login.ui.elements import ADMIN_ID, ADMIN_PW
from login.ui.login import LabelEarth_login
from project.ui.create_project import CreateProject
from project.ui.project_list import ProjectList
from utils.assert_wait import AssertWait
from utils.test_util import TestUtil
import time

def test_project_02_0060(driver_fixture):
    LabelEarth_login(driver_fixture, ADMIN_ID, ADMIN_PW)
    project = ProjectList(driver_fixture)
    create = CreateProject(driver_fixture)
    text_fixture = TextTypeFixture()
    # 후에 기능 사라지면 삭제
    Common(driver_fixture).info.click()

    step_1_fail_message = "기능 유형 선택 모달창이 생성 되지 않음"
    TestUtil.wait_time_until_find_element(driver_fixture, By.XPATH, "//*[contains(@class, ' progress-bar')]")
    project.creat_project.click()
    time.sleep(0.5)
    assert create.type_modal.is_displayed(), step_1_fail_message


    step_2_fail_message = "RBB 프로젝트가 생성 되지 않음"
    create.create_rbb_project(text_fixture.random_english, "라벨 이름입니다")
    AssertWait.true(create.create_success_msg.is_displayed, step_2_fail_message)
