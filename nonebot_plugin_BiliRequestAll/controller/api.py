import json
import httpx
from nonebot import logger
from ..config import config

HTTPClient = httpx.AsyncClient(
        timeout=10,
        verify=False,
        headers=config.httpx_headers
    )

class BiliAPI:
    """
    [`https://api-dev.shadow403.cn/docs/BiliAPI/`](https://api-dev.shadow403.cn/docs/BiliAPI/)
    """

    def __init__(self):
        self.url = config.api_url

    async def _up_medal_info(self, UID):
        try:
            rUrl = f"{self.url}/medal/owner/{UID}"
            logger.info(f"开始获取数据 {rUrl}")
            rDict = json.loads((await HTTPClient.get(rUrl)).text)
            logger.success(f"获取数据成功 UID: {UID}")
            return rDict
        except Exception as e:
            return {"code": 401, "message": e}

    async def _user_medal_info(self, UID):
        try:
            rUrl = f"{self.url}/user/medal/{UID}"
            logger.info(f"开始获取数据 {rUrl}")
            rDict = json.loads((await HTTPClient.get(rUrl)).text)
            logger.success(f"获取数据成功 UID: {UID}")
            return rDict
        except Exception as e:
            return {"code": 401, "message": e}
