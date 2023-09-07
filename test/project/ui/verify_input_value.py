from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def verify_input_value(driver, placeholder, expected_value):
    input_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='{}']".format(placeholder))))
    actual_value = input_element.get_attribute('value')
    return actual_value == expected_value
