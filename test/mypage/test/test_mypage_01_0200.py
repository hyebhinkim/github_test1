from common.ui.common import Common
from login.ui.elements import  TEST_ID, TEST_PW
from login.ui.login import LabelEarth_login
from mypage.ui.edit_info import editInfo
from mypage.ui.my_task_list import myTaskList
from project.ui.project_list import ProjectList
import time
from project.ui.text_present import is_text_present


def test_mypage_01_0200(driver_fixture):
    LabelEarth_login(driver_fixture, TEST_ID, TEST_PW)
    list = myTaskList(driver_fixture)
    edit = editInfo(driver_fixture)
    project = ProjectList(driver_fixture)

    step_1_fail_message = "마이페이지 화면으로 이동 하지 못함"
    time.sleep(2)
    Common(driver_fixture).profile.click()
    time.sleep(0.5)
    Common(driver_fixture).mypage.click()
    assert list.task_tab.is_displayed(), step_1_fail_message


    step_2_fail_message = "현재 비밀번호 불일치 에러 메세지가 보여지지 않음"
    edit.edit_info.click()
    edit.edit_password.click()
    edit.current_password.send_keys("123123")
    edit.new_password.send_keys("123123123123")
    edit.new_password_confirm.send_keys("123123123123")
    edit.change_btn.click()
    time.sleep(1)
    assert is_text_present(driver_fixture, '현재 비밀번호가 일치하지 않습니다.'), step_2_fail_message
