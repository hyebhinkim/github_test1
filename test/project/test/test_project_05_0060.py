from selenium.webdriver import ActionChains
from login.ui.elements import ADMIN_ID, ADMIN_PW
from login.ui.login import LabelEarth_login
from project.ui.project_list import ProjectList
from project.ui.project_task import ProjectTask
from project.ui.text_present import is_text_present
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_project_05_0060(driver_fixture):
    LabelEarth_login(driver_fixture, ADMIN_ID, ADMIN_PW)
    project = ProjectList(driver_fixture)
    actions = ActionChains(driver_fixture)
    task = ProjectTask(driver_fixture)


    step_1_fail_message = "작업 화면으로 이동 하지 못함"
    time.sleep(1)
    actions.move_to_element(project.first_project).click().perform()
    assert is_text_present(driver_fixture, '작업'), step_1_fail_message


    step_2_fail_message = "pagenation이 100/page로 바뀌지 않음"
    task.pagenation.click()
    WebDriverWait(driver_fixture, 5).until(
        EC.element_to_be_clickable(task.page_100)
    ).click()
    assert pagination_selected(driver_fixture, 100), step_2_fail_message


    step_3_fail_message = "pagenation이 150/page로 바뀌지 않음"
    task.pagenation.click()
    WebDriverWait(driver_fixture, 5).until(
        EC.element_to_be_clickable(task.page_150)
    ).click()
    assert pagination_selected(driver_fixture, 150), step_3_fail_message


def pagination_selected(driver, page_number):
    expected_title = f"{page_number} / page"
    expected_aria_selected = "true"

    element = driver.find_element(By.XPATH, f"//*[contains(@class, 'ant-select-item') and @title='{expected_title}'][@aria-selected='{expected_aria_selected}']")
    return element.get_attribute("aria-selected") == expected_aria_selected
