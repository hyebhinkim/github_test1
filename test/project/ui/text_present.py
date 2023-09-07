from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def is_text_present(driver, text):
    try:
        element = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, "//*[contains(text(), '{}')]".format(text)), text))
        return True
    except:
        return False


def is_text_present_2(driver, text):
    try:
        return text in driver.page_source
    except:
        return False
