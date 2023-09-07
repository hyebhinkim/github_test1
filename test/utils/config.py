import configparser
from utils.test_util import TestUtil

class Config:
    """
    프로젝트 디렉토리에 있는 server_config.ini 파일을 읽어 설정 값을 가져옵니다.
    """

    def __init__(self):
        self._config = configparser.ConfigParser()
        self._config.read(TestUtil.get_cwd() + "/server_config.ini")

    @property
    def server_name(self):
        return self._config.get("TEST-LABELEARTH", "DOMAIN")

    @property
    def user_web_url(self):
        return self._config.get("TEST-LABELEARTH", "user_web_url")

    @property
    def headless(self) -> bool:
        try:
            return self._config.getboolean("DEFAULT", "headless")
        except (configparser.NoSectionError, configparser.NoOptionError):
            return False
