from common.fixture.text_type_fixture import TextTypeFixture
from common.ui.common import Common
from login.ui.elements import ADMIN_ID, ADMIN_PW
from login.ui.login import LabelEarth_login
from project.ui.text_present import is_text_present, is_text_present_2
from user.ui.add_user import addUser
import time
from user.ui.user_list import UserList


def test_user_03_0010(driver_fixture):
    LabelEarth_login(driver_fixture, ADMIN_ID, ADMIN_PW)
    add_user = addUser(driver_fixture)
    user = UserList(driver_fixture)
    random = TextTypeFixture()
    Common(driver_fixture).info.click()

    step_1_fail_message = "사용자 관리 화면으로 이동 하지 못함"
    time.sleep(1)
    Common(driver_fixture).user_managment.click()
    assert is_text_present(driver_fixture, '사용자 관리'), step_1_fail_message


    step_2_fail_message = "사용자 편집이 완료되지 않음"
    user.serach_bar.send_keys("test")
    user.mod_btn.click()
    add_user.eamil_celar_btn.click()
    random_email = random.generate_random_email()
    add_user.email.send_keys(random_email)
    #add_user.confirm_btn.click()
    assert is_text_present_2(driver_fixture, "test 님의 정보가 수정되었습니다."), step_2_fail_message
