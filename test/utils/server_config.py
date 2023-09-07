import configparser

from utils.test_util import TestUtil


class ServerConfig:
    """
    프로젝트 디렉토리에 있는 server_config.ini 파일을 읽어 설정 값을 가져옵니다.
    server_name을 설정하여 접근하고자 하는 서버의 설정 값을 얻습니다.
    """

    def __init__(self, server_name):
        self._config = configparser.ConfigParser()
        self._config.read(TestUtil.get_cwd() + "/server_config.ini")
        self._server_name = server_name

    @property
    def server_name(self):
        return self._config["TEST-LABELEARTH"]["DOMAIN"]

    @property
    def user_web_url(self):
        return self._config["TEST-LABELEARTH"]["user_web_url"]

    @property
    def host(self) -> str:
        return self._config["DEFAULT"]["HOST"]

    @property
    def domain(self):
        return self._config["TEST-LABELEARTH"]["DOMAIN"]

    @property
    def web_url(self):
        return "https://" + self.domain
