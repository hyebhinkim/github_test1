import pytest
from selenium.webdriver.common.by import By
from common.ui.elements.elements import PROJECT
from login.ui.login import Login, LabelEarth
from login.ui.elements import *

@pytest.mark.nondestructive
def test_login_01_0010(driver_fixture):
    LabelEarth(driver_fixture)
    login = Login(driver_fixture)

    step_1_fail_message = "ID가 제대로 입력 되지 않음"
    login.id_input.send_keys(ADMIN_ID)
    assert login.id_input.get_attribute("value") == ADMIN_ID, step_1_fail_message

    step_2_fail_message = "PW가 제대로 입력 되지 않음"
    login.pw_input.send_keys(ADMIN_PW)
    assert login.pw_input.get_attribute("value") == ADMIN_PW, step_2_fail_message

    step_3_fail_message = "로그인이 실패하여 프로젝트 관리 화면으로 이동하지 못함"
    login.login_btn.click()
    assert driver_fixture.find_element(By.XPATH, PROJECT), step_3_fail_message
