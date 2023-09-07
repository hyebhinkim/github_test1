from login.ui.login import Login, LabelEarth
from login.ui.elements import *



def test_login_01_0050(driver_fixture):
    LabelEarth(driver_fixture)
    login = Login(driver_fixture)

    step_1_fail_message = "패스워드에 입력 데이터가 존재하지 않는데 로그인 버튼이 비활성화 되어있지 않음"
    login.id_input.send_keys(ADMIN_ID)
    assert not login.login_btn.is_enabled(), step_1_fail_message

    step_2_fail_message = "아이디에 입력 데이터가 존재하지 않는데 로그인 버튼이 비활성화 되어있지 않음"
    login.id_input_clear.click()
    login.pw_input.send_keys(ADMIN_PW)
    assert not login.login_btn.is_enabled(), step_2_fail_message

    step_3_fail_message = "입력 데이터가 모두 존재하지 않는데 로그인 버튼이 비활성화 되어있지 않음"
    login.pw_input_clear.click()
    assert not login.login_btn.is_enabled(), step_3_fail_message
