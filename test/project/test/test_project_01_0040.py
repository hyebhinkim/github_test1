
from selenium.webdriver.common.by import By
from login.ui.elements import ADMIN_ID, ADMIN_PW
from login.ui.login import LabelEarth_login
from project.ui.project_list import Filter



def test_project_01_0040(driver_fixture):
    LabelEarth_login(driver_fixture, ADMIN_ID, ADMIN_PW)
    filter = Filter(driver_fixture)

    step_1_fail_message = "진행 전인 프로젝트가 필터링 되지 않음"
    filter.status_filter.click()
    filter.pending.click()
    assert_status(driver_fixture, "진행 전"), step_1_fail_message


    step_2_fail_message = "진행 중인 프로젝트가 필터링 되지 않음"
    filter.status_filter.click()
    filter.in_progress.click()
    assert_status(driver_fixture, "진행 중"), step_2_fail_message


    step_3_fail_message = "완료인 프로젝트가 필터링 되지 않음"
    filter.status_filter.click()
    filter.completed.click()
    assert_status(driver_fixture, "완료"), step_3_fail_message






def assert_status(driver, status):
    xpath = f"//*[contains(@class, 'ant-select-selection-item') and @title='{status}']"
    element = driver.find_element(By.XPATH, xpath)
    assert element is not None, f"{status} 상태를 찾을 수 없습니다."
