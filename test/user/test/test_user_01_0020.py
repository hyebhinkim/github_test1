from common.fixture.text_type_fixture import TextTypeFixture
from common.ui.common import Common
from login.ui.elements import ADMIN_ID, ADMIN_PW
from login.ui.login import LabelEarth_login
from project.ui.text_present import is_text_present
from user.ui.user_list import UserList
import time

def test_user_01_0020(driver_fixture):
    LabelEarth_login(driver_fixture, ADMIN_ID, ADMIN_PW)
    user = UserList(driver_fixture)
    text = TextTypeFixture()

    step_1_fail_message = "사용자 관리 화면으로 이동 하지 못함"
    time.sleep(1)
    Common(driver_fixture).user_managment.click()
    assert is_text_present(driver_fixture, '사용자 관리'), step_1_fail_message


    step_2_fail_message = "검색 결과 없음 화면이 보여 지지 않음"
    user.serach_bar.send_keys(text.random_korean)
    assert is_text_present(driver_fixture, "검색에 대한 결과를 찾을 수 없습니다."), step_2_fail_message
