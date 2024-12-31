import httpx
from nonebot import logger
from ..config import config, _PLUGINVER_

Client = httpx.Client(
        timeout=config.httpx_timeout, verify=False, headers=config.httpx_headers
    )

AsyncClient = httpx.AsyncClient(
        timeout=config.httpx_timeout, verify=False, headers=config.httpx_headers
    )

class BiliAPI:
    """
    [`https://api-dev.shadow403.com.cn`](https://api-dev.shadow403.com.cn)
    """

    def __init__(self):
        rootDict = Client.get(config.api_url).json()
        self.root = rootDict["root"]
        self.paths = rootDict["paths"]
        self.parms = rootDict["parms"]
        self.version = rootDict["version"]

        if self.version != _PLUGINVER_:
            logger.error(f"\n===BiliRequestAll===\n插件版本与API版本不匹配\n插件版本: {_PLUGINVER_}\nAPI版本: {self.version}")
        else:
            logger.success(f"\n===BiliRequestAll===\n当前版本 {_PLUGINVER_}")

    async def _up_medal_info(self, UID):
        path = "medal_owner"
        try:
            rUrl = f"{self.root}/{self.paths[_PLUGINVER_][path]}/{UID}"
            logger.info(f"开始获取数据 {rUrl}")
            rDict = (await AsyncClient.get(rUrl)).json()
            logger.success(f"获取数据成功 UID: {UID}")
            return rDict
        except Exception as e:
            return {"code": 401, "message": e}

    async def _user_medal_info(self, UID):
        path = "medal_info"
        try:
            rUrl = f"{self.root}/{self.paths[_PLUGINVER_][path]}/{UID}{self.parms[_PLUGINVER_][path]}"
            logger.info(f"开始获取数据 {rUrl}")
            rDict = (await AsyncClient.get(rUrl)).json()
            logger.success(f"获取数据成功 UID: {UID}")
            return rDict
        except Exception as e:
            return {"code": 401, "message": e}

API = BiliAPI()
