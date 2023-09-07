from login.ui.login import Login, LabelEarth
from login.ui.elements import *
from utils.assert_wait import AssertWait


def test_login_01_0030(driver_fixture):
    LabelEarth(driver_fixture)
    login = Login(driver_fixture)

    step_1_fail_message = "ID가 제대로 입력 되지 않음"
    login.id_input.send_keys(ADMIN_ID)
    assert login.id_input.get_attribute("value") == ADMIN_ID, step_1_fail_message


    step_2_fail_message = "PW가 제대로 입력됨"
    login.pw_input.send_keys(FAKE_PW)
    assert login.pw_input.get_attribute("value") == FAKE_PW, step_2_fail_message


    step_3_fail_message = "alert 메세지가 생성되지 않음"
    login.login_btn.click()
    AssertWait.same(lambda: login.alert_value(), lambda: "아이디 또는 비밀번호가 일치하지 않습니다.", step_3_fail_message)
