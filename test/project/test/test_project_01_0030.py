import pytest
from selenium.webdriver.common.by import By
from login.ui.elements import ADMIN_ID, ADMIN_PW
from login.ui.login import LabelEarth_login
from project.ui.elements.create_project_elements import *
from project.ui.project_list import ProjectList

@pytest.mark.skip(reason="고정된 프로젝트가 없음")
def test_project_01_0030(driver_fixture):
    LabelEarth_login(driver_fixture, ADMIN_ID, ADMIN_PW)
    project = ProjectList(driver_fixture)

    step_1_fail_message = "프로젝트가 검색되지 않음"
    search_keyword = "ever"
    project.search_bar.send_keys(search_keyword)

    project_names = get_project_names(project)
    assert any(search_keyword in name for name in project_names), step_1_fail_message



def get_project_names(project):
    project_names = []
    project_elements = project._driver.find_elements(By.XPATH, PROJECT_LIST)
    for element in project_elements:
        project_names.append(element.text)
    return project_names
