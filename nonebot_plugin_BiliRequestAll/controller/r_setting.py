import json
from .api import BiliAPI
from ..config import config
from nonebot import on_command
from nonebot.adapters import Message
from nonebot.params import CommandArg
from ..utils import func_switch_status
from nonebot.permission import SUPERUSER
from nonebot.adapters.onebot.v11 import GroupMessageEvent
from nonebot.adapters.onebot.v11.permission import GROUP_OWNER, GROUP_ADMIN

API = BiliAPI()

_GInit = on_command(
        "/rqst",
        aliases = {"/审批"},
        block = False,
        priority = 1,
        permission = GROUP_OWNER | GROUP_ADMIN | SUPERUSER
    )

@_GInit.handle()
async def _(Event: GroupMessageEvent, Initial: Message = CommandArg()):
    _gid = str(Event.group_id)
    _init = Initial.extract_plain_text().split("_")
    if (len(_init) != 4):
        await _GInit.finish()

    _gms = func_switch_status(_init[0])
    _gss = func_switch_status(_init[1])
    if ("error" in [_gms, _gss]):
        await _GInit.finish(config.parse_error)

    _uid = _init[2]
    _rDict = await API._up_medal_info(_uid)
    _scode = _rDict["code"]
    if _scode != 0:
        await _GInit.finish(f"远程服务器请求失败\n返回码: {_scode} \n返回信息:{_rDict['message']}")

    _up_medalname = _rDict["data"]["medal_name"]
    if _up_medalname == None:
        await _GInit.finish("主播UID解析错误\n可能该UID不存在, 或未开通直播")

    _up_name = _rDict["data"]["uname"]
    _up_roomid = _rDict["data"]["roomid"]
    _lowestlvl = _init[3]

    _initdata = [_gms, _gss, int(_uid), int(_lowestlvl), _up_medalname, _up_name, _up_roomid]

    with open(config.s_file, "r", encoding="UTF-8") as f:
        _GSD = json.load(f)
        _GSD["data"][_gid] = _initdata
    with open(config.s_file, "w", encoding="UTF-8") as f:
        json.dump(_GSD, f, indent=4, ensure_ascii=False)

    await _GInit.finish(f"审批设置成功:\n状态: {_gms}\n严格: {_gss}\nUID: {_uid}\n主播: {_up_name}\n房间号: {_up_roomid}\n粉丝牌: {_up_medalname}\n最低等级要求: {_lowestlvl}")
