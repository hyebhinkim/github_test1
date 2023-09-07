from common.ui.common import Common
from login.ui.elements import ADMIN_ID, ADMIN_PW
from login.ui.login import LabelEarth_login
from mypage.ui.my_task_list import myTaskList
from project.ui.project_task import ProjectTask
import time
from project.ui.text_present import is_text_present


def test_mypage_01_0100(driver_fixture):
    LabelEarth_login(driver_fixture, ADMIN_ID, ADMIN_PW)
    list = myTaskList(driver_fixture)
    task = ProjectTask(driver_fixture)

    step_1_fail_message = "마이페이지 화면으로 이동 하지 못함"
    time.sleep(2)
    Common(driver_fixture).profile.click()
    time.sleep(0.5)
    Common(driver_fixture).mypage.click()
    assert list.task_tab.is_displayed(), step_1_fail_message

    step_2_fail_message = "프로젝트 이름으로 검색되지 않음"
    task.mypage_search_bar.send_keys("자동")
    assert not is_text_present(driver_fixture, '검색에 대한 결과를 찾을 수 없습니다.'), step_2_fail_message
