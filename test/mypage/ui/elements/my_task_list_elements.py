# 마이페이지 > 프로젝트 관리 목록
SEARCH_BAR = "//input[@placeholder='프로젝트 이름 검색']"
SEARCH_CLEAR_BTN = "//span[contains(@class, 'ant-input-suffix')]"
TASK_TAB = "//*[text()='내 작업 목록']"


# 마이페이지 > 작업 상태 필터
STATUS_FILTER = "//*[contains(@class, 'ant-select-selector')]"
PENDING = "//div[contains(@class, 'ant-select-item-option-content') and text()='진행 전']"
IN_PROGRESS = "//div[contains(@class, 'ant-select-item-option-content') and text()='진행 중']"
COMPLETED = "//div[contains(@class, 'ant-select-item-option-content') and text()='완료']"


# 마이페이지 > 기능 유형 필터
TYPE_FILTER = "//*[contains(@class, 'ant-select-selector') and descendant::text() = '기능 유형 전체']"
CLEAR_BTN = "//*[contains(@class, 'ant-select-selection-item-remove')]"
RBB = "//div[@title='RBB']"
POLYGON = "//div[@title='Polygon']"
