from selenium.webdriver.common.by import By
from common.ui.elements.elements import *
from login.ui.login import Login, LabelEarth, logout
from login.ui.elements import *


def test_login_02_0010(driver_fixture):
    LabelEarth(driver_fixture)
    login = Login(driver_fixture)

    step_1_fail_message = "ID가 입력 되지 않음"
    login.id_input.send_keys(ADMIN_ID)
    assert login.id_input.get_attribute("value") == ADMIN_ID, step_1_fail_message


    step_2_fail_message = "PW가 입력 되지 않음"
    login.pw_input.send_keys(ADMIN_PW)
    assert login.pw_input.get_attribute("value") == ADMIN_PW, step_2_fail_message


    step_3_fail_message = "아이디 저장 체크 박스가 클릭 되지 않음"
    login.remember_me.click()
    assert login.remember_me.is_selected() is True, step_3_fail_message


    step_4_fail_message = "로그인이 되지 않음"
    login.login_btn.click()
    assert driver_fixture.find_element(By.XPATH, PROJECT), step_4_fail_message


    step_5_fail_message = "로그아웃 후 아이디 저장이 되어 있지 않음"
    logout(driver_fixture)
    assert login.id_input.get_attribute('value') == ADMIN_ID, step_5_fail_message
