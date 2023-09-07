# 프로젝트 관리 목록
SEARCH_BAR = "//input[@placeholder='프로젝트 이름 검색']"
SEARCH_CLEAR_BTN = "//span[contains(@class, 'ant-input-suffix')]"
PROJECT_LIST = "//*[contains(@class, 'ProjectList_51zz4_1')]"
FIRST_PROJECT = "//*[contains(@class, 'ProjectList_51zz4_1')]//li[1]"
CREATE_PROJECT = "//*[contains(@class, ' _Button_1cgl1')]"
PROGRESS_BAR = "//*[contains(@class, ' progress-bar')]"

# 각 프로젝트 편집 및 삭제
KEBAB_BTN = "//*[contains(@class, 'kebab')]"
EDIT ="//*[contains(@class, 'ant-dropdown-menu-item ant-dropdown-menu-item-only-child')]//*[contains(text(), '편집')]"
DELETE = "//*[contains(@class, 'ant-dropdown-menu-item ant-dropdown-menu-item-only-child')]//*[contains(text(), '삭제')]"
DELETE_CONFIRM = "//*[contains(@class, '_modalWrapper_ppggx_20 uno-z4lehi')]//button[2]"

# 프로젝트 상태 필터
STATUS_FILTER = "//*[contains(@class, 'ant-select-selector')]"
PENDING = "//div[contains(@class, 'ant-select-item-option-content') and text()='진행 전']"
IN_PROGRESS = "//div[contains(@class, 'ant-select-item-option-content') and text()='진행 중']"
COMPLETED = "//div[contains(@class, 'ant-select-item-option-content') and text()='완료']"


# 기능 유형 필터
TYPE_FILTER = "//*[contains(@class, 'ant-select-selector') and descendant::text() = '기능 유형 전체']"
CLEAR_BTN = "//*[contains(@class, 'ant-select-selection-item-remove')]"
RBB = "//div[@title='RBB']"
POLYGON = "//div[@title='Polygon']"


# 프로젝트 생성
TYPE_MODAl = "//*[contains(text(), '기능 유형 선택')]"
TYPE_RBB = "//img[contains(@alt, 'rotated_bounding_box')]" # 기능 유형 선택 모달
TYPE_POLYGON = "//img[contains(@alt, 'polygonal')]" # 기능 유형 선택 모달
NEXT_BTN = "//*[contains(@class, 'flex items-center justify-end mt-32px')]//button[2]" #rbb 다음 버튼
SKIP_BTN = "//*[contains(text(), '건너뛰기')]/ancestor::button" # polygon 라벨 클래스 건너뛰기

NAME = "//*[contains(@placeholder, '프로젝트 이름을 입력해주세요.')]"
NAME_CLEAR_BTN = "//*[contains(@class, 'ant-input-clear-icon')]"
DESCRIPTION = "//*[contains(@placeholder, '설명을 입력해주세요')]"
CREATE_BTN = "//*[contains(text(), '프로젝트 생성')]/ancestor::button"
CREATE_SUCCESS_MSG = "//*[contains(@class, 'ant-message-notice-content')]"

# 프로젝트 생성 > 프로젝트 참여자 선택
SELECTED_MANAGER = "//*[contains(text(), '프로젝트에 참여할 Manager를 선택해주세요.')]"
SELECTED_ANNOTATOR = "//*[contains(text(), '프로젝트에 참여할 Annotator를 선택해주세요.')]"
SELECTED_REVIEWER = "//*[contains(text(), '프로젝트에 참여할 Reviewer를 선택해주세요.')]"
MANAGER_MODAL = "//*[contains(@class, '_modalWrapper_')]//*[contains(text(), 'Manager 선택')]"
ANNOTAOTR_MODAL = "//*[contains(@class, '_modalWrapper_')]//*[contains(text(), 'Annotator 선택')]"
REVIEWER_MODAL = "//*[contains(@class, '_modalWrapper_')]//*[contains(text(), 'Reviewer 선택')]"
SELECTED_MODAL_SEARCH_BAR = "//input[contains(@placeholder, '이름 검색')]"
CHECK_BOX_BTN = "//*[contains(@class, 'modalWrapper')]//*[@aria-label='Select all']"
SAVE_BTN = "//*[contains(@class, '_modalWrapper_')]//button"

# 프로젝트 생성 > 영상 선택
SCENE = "//span[text()='영상 불러오기']/ancestor::button"
SCENE_MODAL = "//*[contains(@class, 'uno-cxydzz') and contains(text(), '영상 불러오기')]"
INPUT = "//*[contains(@placeholder, '위성, 영상 이름, 국가 및 지역 검색')]"
SCENE_SELECT = "//tr[@data-row-key='2']//*[contains(concat(' ', normalize-space(@class), ' '), ' ant-checkbox-wrapper css-yp8pcc ')]"
ADD_SCENE_BTN = "//*[contains(@class, 'flex items-center flex-auto')]//button"
SCENE_NEXT_BTN = "//li[@title='Next Page']//button"
LATLNG  = "//tr[contains(@class, 'ant-table-row ant-table-row-level')]/td[6]"
LATLNG_COPY = "//tr[contains(@class, 'ant-table-row ant-table-row-level')]/td[6]//*[contains(@class, 'i-outline:copy text-16px text-$icon-secondary')]"
SCENE_NAME = "//tr[contains(@class, 'ant-table-row ant-table-row-level')]/td[3]"
SCENE_COPY = "//tr[contains(@class, 'ant-table-row ant-table-row-level')]/td[3]//*[contains(@class, 'i-outline:copy text-16px text-$icon-secondary')]"
SUCCESS_MSG = "//*[contains(@class, 'ant-message-custom-content ant-message-success')]"


#작업 기간
DATA_TOGGLE = "//*[contains(@class, 'endDate')]//button[@type='button']"



# 프로젝트 생성 > 라벨 클래스
IMPORT_LABEL = "//*[contains(@class, '_btns_eb5nz_18')]//button[1]"
ADD_LABEL = "//*[@data-test='labelClassAddBtn']"
LABEL_NAME= "//input[@placeholder='새 클래스 이름']" # 클래스 추가 모달창
LABEL_DESCRIPTION = "//*[@placeholder='클래스 설명']"
ADD_LABEL_BTN = "//*[contains(@class, 'flex items-center justify-end mt-32px')]//button[2]" # 클래스 추가 모달
EDIT_LABEL = "//*[contains(@class, 'pencil')]"
DELETE_LABEL= "//*[contains(@class, 'bin')]"
