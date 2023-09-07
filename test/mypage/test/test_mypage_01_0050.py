from common.ui.common import Common
from login.ui.elements import ADMIN_ID, ADMIN_PW
from login.ui.login import LabelEarth_login
from mypage.ui.my_task_list import myTaskList
from project.ui.project_list import TypeFilter
import time

def test_mypage_01_0050(driver_fixture):
    LabelEarth_login(driver_fixture, ADMIN_ID, ADMIN_PW)
    list = myTaskList(driver_fixture)
    filter = TypeFilter(driver_fixture)

    step_1_fail_message = "마이페이지 화면으로 이동 하지 못함"
    time.sleep(2)
    Common(driver_fixture).profile.click()
    time.sleep(0.5)
    Common(driver_fixture).mypage.click()
    assert list.task_tab.is_displayed(), step_1_fail_message


    step_2_fail_message = "RBB 프로젝트만 보여지지 않음"
    filter.type_filter.click()
    filter.rbb.click()
    element = filter.get_type_title('RBB')
    assert element.get_attribute('title') == 'RBB', step_2_fail_message


    step_3_fail_message = "Polygon 프로젝트만 보여지지 않음"
    filter.clear_btn.click()
    filter.polyon.click()
    element = filter.get_type_title('Polygon')
    assert element.get_attribute('title') == 'Polygon', step_3_fail_message
