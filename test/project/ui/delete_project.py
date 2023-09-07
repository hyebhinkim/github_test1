from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

def delete_project(project):
    wait = WebDriverWait(project._driver, 10)
    element = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//*[contains(@class, '_ProjectList_51zz4_1')]//li[1]")))
    ActionChains(project._driver).move_to_element(element).perform()
    project.kebab_btn.click()
    time.sleep(1)
    project.delete.click()
    time.sleep(2)
    project.delete_confirm.click()
    time.sleep(1)

# time.sleep 해결 필요
