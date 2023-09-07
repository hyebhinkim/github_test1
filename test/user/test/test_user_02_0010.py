from common.ui.common import Common
from login.ui.elements import ADMIN_ID, ADMIN_PW, FAKE_PW, NAME
from login.ui.login import LabelEarth_login
from project.ui.text_present import is_text_present
from user.ui.add_user import addUser
import time
from common.fixture.text_type_fixture import TextTypeFixture

def test_user_02_0010(driver_fixture):
    LabelEarth_login(driver_fixture, ADMIN_ID, ADMIN_PW)
    add_user = addUser(driver_fixture)
    random = TextTypeFixture()
    Common(driver_fixture).info.click()

    step_1_fail_message = "사용자 관리 화면으로 이동 하지 못함"
    time.sleep(1)
    Common(driver_fixture).user_managment.click()
    assert is_text_present(driver_fixture, '사용자 관리'), step_1_fail_message


    step_2_fail_message = "사용자 추가 모달창이 생성 되지 않음"
    add_user.user_add_btn.click()
    assert add_user.user_add_modal.is_displayed(), step_2_fail_message


    step_3_fail_message = "아이디가 입력 되지 않음"
    random_email = random.generate_random_email()
    add_user.email.send_keys(random_email)
    time.sleep(5)
    assert add_user.email.get_attribute("value") == random_email, step_3_fail_message


    step_4_fail_message = "비밀번호가 입력 되지 않음"
    add_user.password.send_keys(FAKE_PW)
    assert add_user.password.get_attribute("value") == FAKE_PW, step_4_fail_message


    step_5_fail_message = "비밀번호 확인이 입력 되지 않음"
    add_user.password_confirm.send_keys(FAKE_PW)
    assert add_user.password_confirm.get_attribute("value") == FAKE_PW, step_5_fail_message


    step_6_fail_message = "사용자 이름이 입력 되지 않음"
    add_user.user_name.send_keys(NAME)
    assert add_user.user_name.get_attribute("value") == NAME, step_6_fail_message
