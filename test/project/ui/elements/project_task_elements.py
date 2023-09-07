# 작업
GO_BACK_BTN = "//*[contains(@class, 'arrow-left')]"
INFO = "//*[contains(@class, 'info-circl')]"
INFO_MODAL = '//*[contains(@class, \'_modalWrapper_ppggx_20 w-80vw max-w-616px\')]'
SEARCH_BAR = "//*[contains(@placeholder, '작업 ID, 영상 이름, 작업자 검색')]"
MYPAGE_SEARCH_BAR = "//input[contains(@placeholder, '프로젝트 이름 검색')]"
SEARCH_CLEAR_BTN = "//*[contains(@class, 'close-circle')]"
SCENE_DATA = "//*[contains(@class, 'ant-table-thead')]//th[3]"
WORKER = "//*[contains(@class, 'ant-table-thead')]//th[4]"
JOB_STATUS = "//*[contains(@class, 'ant-table-thead')]//th[7]"
JOB_STATUS_FILTER = "//*[contains(@class, 'ant-table-thead')]//th[6]/div/span[2]"


# 작업 상태 필터
UPCOMING_TASK = "//*[contains(@class, 'flex flex-col px-18px py-14px')]//div[1]//span"
IN_PROGRESS = "//*[contains(@class, 'flex flex-col px-18px py-14px')]//div[2]//span"
PENDING_REVIEW = "//*[contains(@class, 'flex flex-col px-18px py-14px')]//div[3]//span"
UNDER_REVIEW = "//*[contains(@class, 'flex flex-col px-18px py-14px')]//div[4]//span"
COMPLETED = "//*[contains(@class, 'flex flex-col px-18px py-14px')]//div[5]//span"
FILTER_RESET_BTN = "//*[contains(@class, 'ant-btn css-yp8pcc ant-btn-default _Button_1l0ty_1 default uno-hcllwd')]"



# 작업 - 페이징
PAGINATION = "//li[contains(@class, 'pagination-options')]//*[contains(@class, 'pagination-options-size-changer')]"
PAGE_50 = "//*[contains(@class, 'ant-select-item-option-content') and text()='50 / page']"
PAGE_100 = "//*[contains(@class, 'ant-select-item-option-content') and text()='100 / page']"
PAGE_150 = "//*[contains(@class, 'ant-select-item-option-content') and text()='150 / page']"

#작업자 할당 모달
CHECK_BOX = "//*[contains(@class, 'ant-checkbox-input')]"
ASSIGN_WORKER_BTN = "//*[contains(text(), '작업자 할당')]/parent::button"
CURRENT_TASK_COUNT = "//*[contains(@class, 'mt-24px font-400 text-14px')]//th[2]"
