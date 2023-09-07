from common.ui.common import Common
from login.ui.elements import ADMIN_ID, ADMIN_PW
from login.ui.login import LabelEarth_login
from project.ui.text_present import is_text_present
from user.ui.user_list import UserList
import time

def test_user_01_0010(driver_fixture):
    LabelEarth_login(driver_fixture, ADMIN_ID, ADMIN_PW)
    user = UserList(driver_fixture)


    step_1_fail_message = "사용자 관리 화면으로 이동 하지 못함"
    time.sleep(1)
    Common(driver_fixture).user_managment.click()
    assert is_text_present(driver_fixture, '사용자 관리'), step_1_fail_message


    step_2_fail_message = "사용자 이름으로 검색 되지 않음"
    user.serach_bar.send_keys("admin")
    assert is_text_present(driver_fixture, "admin"), step_2_fail_message
