import os, json
from .controller import *
from .config import PluginConfig, config
from nonebot.plugin import PluginMetadata

__plugin_meta__ = PluginMetadata(
    name="BiliRequestAll",
    description="通过B站UID审核入群",
    usage="https://github.com/Shadow403/nonebot_plugin_BiliRequestAll#食用方法-初始化",
    type="application",
    homepage="https://github.com/Shadow403/nonebot_plugin_BiliRequestAll",
    supported_adapters={"~onebot.v11"},
    config=PluginConfig,
    extra={},
)

if not os.path.exists(config.s_dir):
    os.makedirs(config.s_dir)
    with open(config.s_file, "w") as initData:
        json.dump({"mainSwitch": "on","data": {}}, initData, indent = 4, ensure_ascii = False)
