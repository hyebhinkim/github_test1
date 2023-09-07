from common.ui.common import Common
from login.ui.elements import ADMIN_ID, ADMIN_PW
from login.ui.login import LabelEarth_login
from project.ui.create_project import CreateProject
from project.ui.project_list import ProjectList
from selenium.webdriver.common.by import By
from project.ui.satellite_crawling import search_and_validate_results
from utils.test_util import TestUtil
import time

def test_project_02_0130(driver_fixture):
    LabelEarth_login(driver_fixture, ADMIN_ID, ADMIN_PW)
    project = ProjectList(driver_fixture)
    create = CreateProject(driver_fixture)

    # 후에 기능 사라지면 삭제
    Common(driver_fixture).info.click()

    step_1_fail_message = "영상 불러오기 모달창이 생성 되지 않음"
    TestUtil.wait_time_until_find_element(driver_fixture, By.XPATH, "//*[contains(@class, ' progress-bar')]")
    project.creat_project.click()
    time.sleep(0.5)
    create.type_rbb.click()
    create.next_btn.click()
    create.scene.click()
    assert len(create.scene_modal) > 0, step_1_fail_message


    step_2_fail_message = "검색 위성 외의 다른 위성이 검색됨"
    driver = driver_fixture
    result = search_and_validate_results(driver, "wayback")
    assert result, step_2_fail_message
