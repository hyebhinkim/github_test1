from datetime import time

from login.ui.login import Login, LabelEarth
from common.fixture.text_type_fixture import TextTypeFixture


def test_login_01_0070(driver_fixture):
    LabelEarth(driver_fixture)
    login = Login(driver_fixture)
    text_fixture = TextTypeFixture()

    step_1_fail_message = "ID에 영어, 숫자, 특수 문자가 입력 되지 않음"
    random_string = text_fixture.generate_random_mixed_string(12)
    login.id_input.send_keys(random_string)
    assert login.id_input.get_attribute('value') == random_string, step_1_fail_message

    step_2_fail_message = "PW에 영어, 숫자, 특수 문자가 입력 되지 않음"
    random_string = text_fixture.generate_random_mixed_string(12)
    login.pw_input.send_keys(random_string)
    assert login.pw_input.get_attribute('value') == random_string, step_2_fail_message
