from project.ui.create_project import CreateProject
from selenium.webdriver.common.by import By
import time

def search_and_validate_results(driver_fixture, search_keyword):
    create = CreateProject(driver_fixture)
    table_row_xpath = ".//tr"
    cell_xpath = "//*[contains(@class, 'ant-table-row ant-table-row-level-0')]//div"


    # 검색어 입력
    search_input = create.input[0]
    search_input.send_keys(search_keyword)
    time.sleep(2)

    # 페이지 순회
    current_page = 1

    while True:
        # 테이블 행 순회
        rows = driver_fixture.find_elements(By.XPATH, table_row_xpath)

        for row in rows:
            cells = row.find_elements(By.XPATH, cell_xpath)
            if not any(search_keyword in cell.text for cell in cells):
                return False

        # 다음 페이지로 이동
        try:
            create.scene_next_btn.click()
            if create.scene_next_btn.is_enabled():
                create.scene_next_btn.click()


                time.sleep(2)
            else:
                return True
        except:
            break

        current_page += 1

    return True
