import pytest

from login.ui.login import Login, LabelEarth
from login.ui.elements import *



def test_login_01_0060(driver_fixture):
    LabelEarth(driver_fixture)
    login = Login(driver_fixture)

    step_1_fail_message = "PW invisible 활성화 되어 있지 않음"
    login.pw_input.send_keys(ADMIN_PW)
    assert login.pw_invisible_elements == 'password', step_1_fail_message


    step_2_fail_message = "아이콘 클릭 시 패스워드가 암호화되어 보여짐"
    login.pw_invisible_btn.click()
    assert login.pw_invisible_elements == 'text', step_2_fail_message
