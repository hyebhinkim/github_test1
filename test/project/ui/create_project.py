import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from conftest import driver_fixture
from project.ui.elements.create_project_elements import *
from utils.assert_wait import AssertWait


class CreateProject:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    @property
    def type_modal(self):
        return self._driver.find_element(By.XPATH, TYPE_MODAl)

    @property
    def type_rbb(self):
        return self._driver.find_element(By.XPATH, TYPE_RBB)

    @property
    def type_polygon(self):
        return self._driver.find_element(By.XPATH, TYPE_POLYGON)

    @property
    def next_btn(self):
        return self._driver.find_element(By.XPATH, NEXT_BTN)

    @property
    def skip_btn(self):
        return self._driver.find_element(By.XPATH, SKIP_BTN)

    @property
    def name(self):
        return self._driver.find_element(By.XPATH, NAME)

    @property
    def name_clear_bth(self):
        return self._driver.find_element(By.XPATH, NAME_CLEAR_BTN)

    @property
    def description(self):
        return self._driver.find_element(By.XPATH, DESCRIPTION)

    @property
    def create_btn(self):
        return self._driver.find_element(By.XPATH, CREATE_BTN)

    @property
    def scene(self):
        return self._driver.find_element(By.XPATH, SCENE)

    @property
    def scene_modal(self):
        return self._driver.find_elements(By.XPATH, SCENE_SELECT)

    @property
    def input(self):
        return self._driver.find_elements(By.XPATH, INPUT)

    @property
    def scene_select(self):
        return self._driver.find_element(By.XPATH, SCENE_SELECT)

    @property
    def add_scene_btn(self):
        return self._driver.find_element(By.XPATH, ADD_SCENE_BTN)

    @property
    def scene_next_btn(self):
        return self._driver.find_element(By.XPATH, SCENE_NEXT_BTN)

    @property
    def latlng(self):
        return self._driver.find_element(By.XPATH, LATLNG)

    @property
    def latlng_copy(self):
        return self._driver.find_element(By.XPATH, LATLNG_COPY)

    @property
    def scene_name(self):
        return self._driver.find_element(By.XPATH, SCENE_NAME)

    @property
    def scene_copy(self):
        return self._driver.find_element(By.XPATH, SCENE_COPY)

    @property
    def success_msg(self):
        return self._driver.find_element(By.XPATH, SUCCESS_MSG)

    @property
    def import_label(self):
        return self._driver.find_element(By.XPATH, IMPORT_LABEL)

    @property
    def add_label(self):
        return self._driver.find_element(By.XPATH, ADD_LABEL)

    @property
    def label_name(self):
        return self._driver.find_element(By.XPATH, LABEL_NAME)

    @property
    def label_description(self):
        return self._driver.find_element(By.XPATH, LABEL_DESCRIPTION)

    @property
    def add_label_btn(self):
        return self._driver.find_element(By.XPATH, ADD_LABEL_BTN)

    @property
    def edit_label(self):
        return self._driver.find_element(By.XPATH, EDIT_LABEL)

    @property
    def delete_label(self):
        return self._driver.find_element(By.XPATH, DELETE_LABEL)

    @property
    def create_success_msg(self):
        return self._driver.find_element(By.XPATH, CREATE_SUCCESS_MSG)

    @property
    def date_toggle(self):
        return self._driver.find_element(By.XPATH, DATA_TOGGLE)

    @property
    def selected_annotator(self):
        return self._driver.find_element(By.XPATH, SELECTED_ANNOTATOR)

    @property
    def selected_reviewer(self):
        return self._driver.find_element(By.XPATH, SELECTED_REVIEWER)

    @property
    def annotator_modal(self):
        return self._driver.find_element(By.XPATH, ANNOTAOTR_MODAL)

    @property
    def reviewer_modal(self):
        return self._driver.find_element(By.XPATH, REVIEWER_MODAL)

    @property
    def selected_modal_serach_bar(self):
        return self._driver.find_element(By.XPATH, SELECTED_MODAL_SEARCH_BAR)

    @property
    def check_box_btn(self):
        return self._driver.find_element(By.XPATH, CHECK_BOX_BTN)

    @property
    def save_btn(self):
        return self._driver.find_element(By.XPATH, SAVE_BTN)







    def create_rbb_project(self, project_name: str, label_name: str):
        self.type_rbb.click()
        self.next_btn.click()
        self.name.send_keys(project_name)
        self.selected_annotator.click()
        time.sleep(1)
        self.check_box_btn.click()
        time.sleep(1)
        self.save_btn.click()
        time.sleep(1)
        self.selected_reviewer.click()
        time.sleep(1)
        self.check_box_btn.click()
        time.sleep(1)
        self.save_btn.click()
        time.sleep(1)
        self.scene.click()
        self.scene_select.click()
        self.add_scene_btn.click()
        self.add_label.click()
        self.label_name.send_keys(label_name)
        self.add_label_btn.click()
        self.create_btn.click()
        time.sleep(5)


    def create_polygon_project(self, project_name: str, label_name: str):
        self.type_polygon.click()
        self.next_btn.click()
        time.sleep(0.5)
        self.skip_btn.click()
        self.name.send_keys(project_name)
        self.selected_annotator.click()
        time.sleep(1)
        self.check_box_btn.click()
        time.sleep(1)
        self.save_btn.click()
        time.sleep(1)
        self.selected_reviewer.click()
        time.sleep(1)
        self.check_box_btn.click()
        time.sleep(1)
        self.save_btn.click()
        time.sleep(1)
        self.scene.click()
        self.scene_select.click()
        self.add_scene_btn.click()
        self.add_label.click()
        self.label_name.send_keys(label_name)
        self.add_label_btn.click()
        self.create_btn.click()
        time.sleep(2)

    def toast_message(self, expected_message):
        def get_actual_message():
            toast_message_element = self.success_msg
            return toast_message_element.text

        AssertWait.same(get_actual_message, lambda: expected_message,
                        f"Expected toast message: {expected_message}, Actual toast message: {{}}")
