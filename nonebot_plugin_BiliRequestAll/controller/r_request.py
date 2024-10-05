import json
from .api import BiliAPI
from ..config import config
from nonebot import on_request, logger
from ..utils import func_load_switchdata
from nonebot.adapters.onebot.v11 import Bot, GroupRequestEvent

API = BiliAPI()

_GReq = on_request(priority = 1, block = False)

@_GReq.handle()
async def groupReq_handle(Bot: Bot, Event: GroupRequestEvent):
    _gid = str(Event.group_id)
    _aplJson = json.loads(Event.model_dump_json())
    _aplFlag = _aplJson["flag"]
    _splST = _aplJson["sub_type"]
    _aplUID = "".join(filter(str.isdigit, _aplJson["comment"]))
    _swl = func_load_switchdata(config.s_file, _gid)

    if (_swl[0] in [None, "off"]):
        await _GReq.finish()
    _user_medal_info = await API._user_medal_info(_aplUID)
    if (_user_medal_info["code"] != 0):
        await _GReq.finish()
    _user_medal_lvl = _user_medal_info["data"]["fans_medal"]["medal"]["level"]
    _user_medal_name = _user_medal_info["data"]["fans_medal"]["medal"]["medal_name"]

    if _user_medal_name !=_swl[4]:
        if _swl[1] != "on":
            await _GReq.finish()
        await Bot.set_group_add_request(
                flag = _aplFlag,
                sub_type = _splST,
                approve = False,
                reason = "请打开粉丝牌展示, 并佩戴匹配该群的粉丝牌!",
            )

    if _user_medal_lvl >= _swl[3]:
        await Bot.set_group_add_request(
            flag = _aplFlag,
            sub_type = _splST,
            approve = True,
            reason = "",
        )

    if (_swl[1] == "on"):
        await Bot.set_group_add_request(
            flag = _aplFlag,
            sub_type = _splST,
            approve = False,
            reason = "粉丝牌等级过低",
        )
    