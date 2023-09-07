from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from project.ui.elements.project_task_elements import *



class ProjectTask:
    def __init__(self, driver: WebDriver):
        self._driver = driver


    @property
    def go_back_btn(self):
        return self._driver.find_element(By.XPATH, GO_BACK_BTN)

    @property
    def info(self):
        return self._driver.find_element(By.XPATH, INFO)

    @property
    def info_modal(self):
        return self._driver.find_element(By.XPATH, INFO_MODAL)


    @property
    def search_bar(self):
        return self._driver.find_element(By.XPATH, SEARCH_BAR)

    @property
    def mypage_search_bar(self):
        return self._driver.find_element(By.XPATH, MYPAGE_SEARCH_BAR)

    @property
    def search_clear_btn(self):
        return self._driver.find_element(By.XPATH, SEARCH_CLEAR_BTN)

    @property
    def pagenation(self):
        return  self._driver.find_element(By.XPATH, PAGINATION)

    @property
    def page_50(self):
        return self._driver.find_element(By.XPATH, PAGE_50)

    @property
    def page_100(self):
        return self._driver.find_element(By.XPATH, PAGE_100)

    @property
    def page_150(self):
        return self._driver.find_element(By.XPATH, PAGE_150)

    @property
    def worker(self):
        return self._driver.find_element(By.XPATH, WORKER)

    @property
    def job_status(self):
        return self._driver.find_element(By.XPATH, JOB_STATUS)

    @property
    def job_status_filter(self):
        return self._driver.find_element(By.XPATH, JOB_STATUS_FILTER)

    @property
    def upcoming_task(self):
        return self._driver.find_element(By.XPATH, UPCOMING_TASK)

    @property
    def in_progress(self):
        return self._driver.find_element(By.XPATH, IN_PROGRESS)

    @property
    def pending_review(self):
        return self._driver.find_element(By.XPATH, PENDING_REVIEW)

    @property
    def under_review(self):
        return self._driver.find_element(By.XPATH, UNDER_REVIEW)

    @property
    def completd(self):
        return self._driver.find_element(By.XPATH, COMPLETED)

    @property
    def filter_reset_btn(self):
        return self._driver.find_element(By.XPATH, FILTER_RESET_BTN)

    @property
    def check_box(self):
        return self._driver.find_element(By.XPATH, CHECK_BOX)

    @property
    def assign_worker_btn(self):
        return self._driver.find_element(By.XPATH, ASSIGN_WORKER_BTN)


    @property
    def current_task_count(self):
        return self._driver.find_element(By.XPATH, CURRENT_TASK_COUNT)
