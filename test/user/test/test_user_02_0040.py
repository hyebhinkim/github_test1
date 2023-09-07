from common.ui.common import Common
from login.ui.elements import ADMIN_ID, ADMIN_PW
from login.ui.login import LabelEarth_login
from project.ui.text_present import is_text_present
from user.ui.add_user import addUser
import time


def test_user_02_0040(driver_fixture):
    LabelEarth_login(driver_fixture, ADMIN_ID, ADMIN_PW)
    add_user = addUser(driver_fixture)
    Common(driver_fixture).info.click()

    step_1_fail_message = "사용자 관리 화면으로 이동 하지 못함"
    time.sleep(1)
    Common(driver_fixture).user_managment.click()
    assert is_text_present(driver_fixture, '사용자 관리'), step_1_fail_message


    step_2_fail_message = "사용자 추가 모달창이 생성 되지 않음"
    add_user.user_add_btn.click()
    assert add_user.user_add_modal.is_displayed(), step_2_fail_message


    step_3_fail_message = "역할이 다중 선택 되지 않음"
    add_user.role.click()
    add_user.manager.click()
    add_user.annotator.click()
    add_user.reviewer.click()
    add_user.viewer.click()
