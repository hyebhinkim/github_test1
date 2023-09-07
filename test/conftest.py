import pytest
import platform
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from utils.config import Config
from utils.initial_values import SELENIUM_IMPLICITLY_WAIT_INITIAL_VALUE
from utils.server_config import ServerConfig
from utils.test_util import TestUtil

def setup_driver():
    chrome_driver_path = ChromeDriverManager(version="103.0.5060.53").install()

    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    # 필요한 다른 옵션들 추가

    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)
    #driver = webdriver.Chrome(desired_capabilities=capabilities)
    return driver


@pytest.fixture
def chrome_options(chrome_options):
    cwd = TestUtil.get_cwd()

    chrome_options.add_argument("--incognito")  # chrome 시크릿 모드 실행
    current_platform = platform.system()
    if current_platform == "Linux":
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")

    if Config().headless:
        chrome_options.add_argument("--lang=ko_KR")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920,1080")

    path_seperator = "/"
    if current_platform == "Windows":
        path_seperator = "\\"
    chrome_options.add_experimental_option(
        "prefs",
        {
            "download.default_directory": f"{cwd}{path_seperator}downloads",
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True,
        },
    )
    return chrome_options

@pytest.fixture
def driver_fixture(selenium, chrome_options):
    config = Config()
    server_config = ServerConfig(config.server_name)
    selenium.get(server_config.web_url)
    selenium.maximize_window()
    selenium.implicitly_wait(SELENIUM_IMPLICITLY_WAIT_INITIAL_VALUE)
    return selenium
