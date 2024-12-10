from mpsiemlib.common import ModuleInterface, MPSIEMAuth, MPComponents, LoggingHandler, Settings
from mpsiemlib.common import exec_request

class EDR(ModuleInterface, LoggingHandler):
    """
    Модуль каких-то полезных действий по работе с EDR
    """
    __api_edr_agents_discovery = "/api/edr/v1/agents/{}/discovery"

    def __init__(self, auth: MPSIEMAuth, settings: Settings):
        ModuleInterface.__init__(self, auth, settings)
        LoggingHandler.__init__(self)
        self.__core_session = auth.connect(MPComponents.CORE)
        self.__core_hostname = auth.creds.core_hostname
        self.log.debug('status=succes, action=prepare, msg="EDR Module init"')
        
    def get_edr_agent_by_hash(self, hash: str) -> dict:
        """Получить информацию об агенте EDR

        Args:
            hash (str): идентификатор агента EDR (хеш)

        Returns:
            dict: словарь с данными об агенте
        """        
        api_url = self.__api_edr_agents_discovery.format(hash)
        url = "https://{}{}".format(self.__core_hostname, api_url)
        rq = exec_request(self.__core_session, url)
        response = rq.json()
        return response.get("data")
