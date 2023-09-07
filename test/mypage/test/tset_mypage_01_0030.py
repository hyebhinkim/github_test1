from selenium.webdriver.common.by import By
from common.ui.common import Common
from login.ui.elements import ADMIN_ID, ADMIN_PW
from login.ui.login import LabelEarth_login
from mypage.ui.my_task_list import myTaskList
from project.ui.elements.create_project_elements import PROJECT_LIST
from project.ui.project_list import ProjectList
import time

def test_mypage_01_0030(driver_fixture):
    LabelEarth_login(driver_fixture, ADMIN_ID, ADMIN_PW)
    list = myTaskList(driver_fixture)
    project = ProjectList(driver_fixture)

    step_1_fail_message = "마이페이지 화면으로 이동 하지 못함"
    time.sleep(2)
    Common(driver_fixture).profile.click()
    time.sleep(0.5)
    Common(driver_fixture).mypage.click()
    assert list.task_tab.is_displayed(), step_1_fail_message


    step_2_fail_message = "프로젝트가 검색되지 않음"
    search_keyword = "프로젝트"
    project.search_bar.send_keys(search_keyword)

    project_names = get_project_names(project)
    assert any(search_keyword in name for name in project_names), step_2_fail_message


def get_project_names(project):
    project_names = []
    project_elements = project._driver.find_elements(By.XPATH, PROJECT_LIST)
    for element in project_elements:
        project_names.append(element.text)
    return project_names
