# @python  : 3.11.0
# @Time    : 2023/9/29
# @Author  : Shadow403
# @Version : 0.2.7
# @Email   : anonymous_hax@foxmail.com
# @Software: Visual Studio Code

import os, json
from .func import *
from .api import biliAPI
from nonebot.adapters import Message
from nonebot.params import CommandArg
from nonebot.permission import SUPERUSER
from nonebot.plugin import PluginMetadata
from nonebot import on_request, on_command, logger
from nonebot.adapters.onebot.v11 import Bot, GroupRequestEvent, GroupMessageEvent
from nonebot.adapters.onebot.v11.permission import GROUP_OWNER, GROUP_ADMIN

biliAPI = biliAPI()

__plugin_meta__ = PluginMetadata(
    name="BiliRequestAll",
    description="通过B站UID审核入群",
    usage="https://github.com/Shadow403/nonebot_plugin_BiliRequestAll#食用方法-初始化",
    type="application",
    homepage="https://github.com/Shadow403/nonebot_plugin_BiliRequestAll",
    supported_adapters={"~onebot.v11"},
    extra={},
)

logDir = "log"
saveDIr = "groupSwitcher"
saveJson = "switcher.json"
if not os.path.exists(saveDIr):
    os.makedirs(saveDIr)
if not os.path.exists(f"{saveDIr}/{logDir}"):
    os.makedirs(f"{saveDIr}/{logDir}")
if not os.path.exists(f"{saveDIr}/{saveJson}"):
    data = {"mainSwitch": "on","data": {}}
    with open(f"{saveDIr}/{saveJson}", "w") as initData:
        json.dump(data, initData, indent = 4, ensure_ascii = False)

groupInit = on_command("/rqst", aliases = {"/审批"}, block = False, priority = 1, permission = GROUP_OWNER | GROUP_ADMIN | SUPERUSER)
groupSwitchData = on_command("/rqst info", aliases = {"/审批 信息"}, block = False, priority = 1, permission = GROUP_OWNER | GROUP_ADMIN | SUPERUSER)

@groupInit.handle()
async def groupInit_handle(event: GroupMessageEvent, Initial: Message = CommandArg()):
    groupID = str(event.group_id)

    initialText = Initial.extract_plain_text()
    initialSwitch = initialText.split("_")
    if (len(initialSwitch) != 4):
        await groupInit.finish('数据解析错误\n以"_"作为分隔符\n开关-严格-主播UID-最低等级\nhttps://github.com/Shadow403/nonebot_plugin_BiliRequestAll')

    else:
        groupMainSwitch = func.switchStatus(initialSwitch[0])
        groupStrictSwitch = func.switchStatus(initialSwitch[1])
        switchStatusList = [groupMainSwitch, groupStrictSwitch]
        if ("error" in switchStatusList):
            await groupInit.finish('数据解析错误\n以"_"作为分隔符\n开关-严格-主播UID-最低等级\nhttps://github.com/Shadow403/nonebot_plugin_BiliRequestAll')

        else:
            upUID = initialSwitch[2]
            fewerMedalLvL = initialSwitch[3]
            upBaseUID = biliAPI.upMedalInfo(upUID)
            MedalStatus = upBaseUID[0]

            if (MedalStatus != 0):
                groupStrictSwitch = "off"
                await groupInit.finish('主播UID解析错误\n可能该UID不存在, 或未开通直播')

            else:
                upName = upBaseUID[1][0]
                upRoomID = upBaseUID[1][1]
                MedalName = upBaseUID[1][2]
            
                initialData = [groupMainSwitch, groupStrictSwitch, upRoomID, int(fewerMedalLvL), MedalName, int(upUID), upName]

                with open(f"{saveDIr}/{saveJson}", "r") as switchData:
                    groupSwitchData = json.load(switchData)
                groupSwitchData['data'][groupID] = initialData
                with open(f"{saveDIr}/{saveJson}", 'w') as switchFile:
                    json.dump(groupSwitchData, switchFile, indent = 4)
                await groupInit.finish(f"审批设置成功:\n状态: {groupMainSwitch}\n严格: {groupStrictSwitch}\nUID: {upUID}\n主播: {upName}\n房间号: {upRoomID}\n粉丝牌: {MedalName}\n最低等级要求: {fewerMedalLvL}")


@groupSwitchData.handle()
async def groupSwitchData_handle(event: GroupMessageEvent, Initial: Message = CommandArg()):
    groupID = str(event.group_id)
    with open(f"{saveDIr}/{saveJson}", "r") as switchData:
        groupSwitchData = json.load(switchData)

    if (groupID not in groupSwitchData['data']):
        await groupInit.finish(f"该群 ({groupID}) 无审批信息")
    else:
        groupSwitchList = groupSwitchData['data'][groupID]
        groupMainSwitch = groupSwitchList[0]
        groupStrictSwitch = groupSwitchList[1]
        upRoomID = groupSwitchList[2]
        fewerMedalLvL = groupSwitchList[3]
        MedalName = groupSwitchList[4]
        upUID = groupSwitchList[5]
        upName = groupSwitchList[6]

    await groupInit.finish(f"审批设置信息:\n状态: {groupMainSwitch}\n严格: {groupStrictSwitch}\nUID: {upUID}\n主播: {upName}\n房间号: {upRoomID}\n粉丝牌: {MedalName}\n最低等级要求: {fewerMedalLvL}")


groupReq = on_request(priority = 1, block = False)

@groupReq.handle()
async def groupReq_handle(bot: Bot, event: GroupRequestEvent):
    groupID = str(event.group_id)
    applyJson = json.loads(event.json())
    applyFlag = applyJson['flag']
    applyUID = applyJson['comment']
    applySubType = applyJson['sub_type']
    approveUID = ''.join(filter(str.isdigit, applyUID))
    switchStatusList = func.loadSwitchFileData(f"{saveDIr}/{saveJson}", groupID)
    groupMainSwitch = switchStatusList[0]
    groupStrictMode = switchStatusList[1]

    if (groupMainSwitch not in ["groupIdisNull", "off"]):
        getUserMedalInfo = biliAPI.userMedalInfo(approveUID)
        if (getUserMedalInfo[0] == 0):
            userMedalLvL = int(getUserMedalInfo[1][0])
            userMedalName = getUserMedalInfo[1][1]

            if (switchStatusList[4] == userMedalName):

                if (userMedalLvL >= switchStatusList[3]):
                    await bot.set_group_add_request(
                        flag = applyFlag,
                        sub_type = applySubType,
                        approve = True,
                        reason = "",
                    )

                else:
                    if (groupStrictMode == "on"):
                        await bot.set_group_add_request(
                            flag = applyFlag,
                            sub_type = applySubType,
                            approve = False,
                            reason = "粉丝牌等级过低",
                        )
            else:
                if (groupStrictMode == "on"):
                    await bot.set_group_add_request(
                            flag = applyFlag,
                            sub_type = applySubType,
                            approve = False,
                            reason = "请打开粉丝牌展示, 并佩戴匹配该群的粉丝牌!",
                        )

    else:
        pass

