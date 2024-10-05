import json
from ..config import config
from nonebot import on_command
from nonebot.permission import SUPERUSER
from nonebot.adapters.onebot.v11 import GroupMessageEvent
from nonebot.adapters.onebot.v11.permission import GROUP_OWNER, GROUP_ADMIN

_GData = on_command(
        "/rqst info",
        aliases = {"/审批 信息"},
        block = False,
        priority = 1,
        permission = GROUP_OWNER | GROUP_ADMIN | SUPERUSER
    )

@_GData.handle()
async def _(Event: GroupMessageEvent):
    _gid = str(Event.group_id)
    with open(config.s_file, "r", encoding="UTF-8") as f:
        _gsd = json.load(f)

    if _gid not in _gsd["data"]:
        await _GData.finish(f"该群 ({_gid}) 无审批信息")
    _pgsd = _gsd['data'][_gid]
    await _GData.finish(f"审批设置信息:\n状态: {_pgsd[0]}\n严格: {_pgsd[1]}\nUID: {_pgsd[2]}\n主播: {_pgsd[3]}\n房间号: {_pgsd[4]}\n粉丝牌: {_pgsd[5]}\n最低等级要求: {_pgsd[6]}")
