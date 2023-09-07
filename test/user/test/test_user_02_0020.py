from common.ui.common import Common
from login.ui.elements import ADMIN_ID, ADMIN_PW, FAKE_PW, NAME
from login.ui.login import LabelEarth_login
from project.ui.text_present import is_text_present
from user.ui.add_user import addUser
import time
from common.fixture.text_type_fixture import TextTypeFixture

def test_user_02_0020(driver_fixture):
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


    step_3_fail_message = "아이디 중복 에러 메세지가 노출되지 않음"
    add_user.email.send_keys(ADMIN_ID)
    add_user.password.send_keys(FAKE_PW)
    add_user.password_confirm.send_keys(FAKE_PW)
    add_user.user_name.send_keys(NAME)
    add_user.confirm_btn.click()
    assert is_text_present(driver_fixture, "이미 존재하는 아이디입니다. 다른 아이디를 입력해주세요."), step_3_fail_message
