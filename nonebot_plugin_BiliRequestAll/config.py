import os
from pydantic import BaseModel
from nonebot import get_plugin_config

_PATH_: str = os.path.dirname(__file__)
_PLUGINVER_: str = "0.3.0"

class PluginConfig(BaseModel):
    s_dir: str = "data/nonebot_plugin_BiliRequestALL"
    s_file: str = f"{s_dir}/switcher.json"
    api_url: str = "https://api-dev.shadow403.cn/api/bilibili"
    parse_error: str = '数据解析错误\n以"_"作为分隔符\n开关-严格-主播UID-最低等级\nhttps://github.com/Shadow403/nonebot_plugin_BiliRequestAll'
    httpx_headers: dict = {"User-Agent": "nonebot_plugin_bilirequestall"} 

config: PluginConfig = get_plugin_config(PluginConfig)
