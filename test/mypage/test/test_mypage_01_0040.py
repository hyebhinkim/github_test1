from common.ui.common import Common
from login.ui.elements import ADMIN_ID, ADMIN_PW
from login.ui.login import LabelEarth_login
from mypage.ui.my_task_list import myTaskList
import time

def test_mypage_01_0040(driver_fixture):
    LabelEarth_login(driver_fixture, ADMIN_ID, ADMIN_PW)
    list = myTaskList(driver_fixture)


    step_1_fail_message = "마이페이지 화면으로 이동 하지 못함"
    time.sleep(2)
    Common(driver_fixture).profile.click()
    time.sleep(0.5)
    Common(driver_fixture).mypage.click()
    assert list.task_tab.is_displayed(), step_1_fail_message
