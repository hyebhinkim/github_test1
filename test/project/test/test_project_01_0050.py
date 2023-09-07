from login.ui.elements import ADMIN_ID, ADMIN_PW
from login.ui.login import LabelEarth_login
from project.ui.project_list import TypeFilter


def test_project_01_0050(driver_fixture):
    LabelEarth_login(driver_fixture, ADMIN_ID, ADMIN_PW)
    filter = TypeFilter(driver_fixture)

    step_1_fail_message = "RBB 프로젝트만 보여지지 않음"
    filter.type_filter.click()
    filter.rbb.click()
    element = filter.get_type_title('RBB')
    assert element.get_attribute('title') == 'RBB', step_1_fail_message


    step_2_fail_message = "Polygon 프로젝트만 보여지지 않음"
    filter.clear_btn.click()
    filter.polyon.click()
    element = filter.get_type_title('Polygon')
    assert element.get_attribute('title') == 'Polygon', step_2_fail_message
