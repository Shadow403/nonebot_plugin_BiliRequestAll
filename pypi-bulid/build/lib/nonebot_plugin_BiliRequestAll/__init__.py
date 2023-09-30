# @python  : 3.11.0
# @Time    : 2023/9/29
# @Author  : Shadow403
# @Version : 0.3.0
# @Email   : anonymous_hax@foxmail.com
# @Software: Visual Studio Code

import os, json
from .func import *
from .api import biliAPI
from nonebot.adapters import Message
from nonebot.params import CommandArg
from nonebot.permission import SUPERUSER
from nonebot import on_request, on_command
from nonebot.adapters.onebot.v11 import Bot, GroupRequestEvent, GroupMessageEvent
from nonebot.adapters.onebot.v11.permission import GROUP_OWNER, GROUP_ADMIN

biliAPI = biliAPI()

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
groupSwitch = on_command("/rqst switch", aliases = {"/审批 开关"}, block = False, priority = 2, permission = GROUP_OWNER | GROUP_ADMIN | SUPERUSER)

@groupInit.handle()
async def groupInit_handle(event: GroupMessageEvent, Initial: Message = CommandArg()):
    groupID = str(event.group_id)

    initialText = Initial.extract_plain_text()
    initialSwitch = initialText.split("_")
    if (len(initialSwitch) != 4):
        await groupInit.finish('数据解析错误\n以"_"作为分隔符\n开关-日志-主播UID-最低等级')

    else:
        groupMainSwitch = switchStatus(initialSwitch[0])
        groupLogSwitch = switchStatus(initialSwitch[1])
        switchStatusList = []
        switchStatusList += [groupMainSwitch, groupLogSwitch]
        if ("error" in switchStatusList):
            await groupInit.finish('数据解析错误\n以"_"作为分隔符\n开关-日志-主播UID-最低等级')

        else:
            upUID = initialSwitch[2]
            fewerMedalLvL = initialSwitch[3]
            upBaseUID = biliAPI.upMedalInfo(upUID)
            print(upBaseUID)
            MedalStatus = upBaseUID[0]

            if (MedalStatus != 0):
                groupLogSwitch = "off"
                await groupInit.finish('主播UID解析错误')

            else:
                upName = upBaseUID[1][0]
                upRoomID = upBaseUID[1][1]
                MedalName = upBaseUID[1][2]
            
                initialData = [groupMainSwitch, groupLogSwitch, upRoomID, int(fewerMedalLvL), MedalName, int(upUID), upName]

                with open(f"{saveDIr}/{saveJson}", "r") as switchData:
                    groupSwitchData = json.load(switchData)
                groupSwitchData['data'][groupID] = initialData
                with open(f"{saveDIr}/{saveJson}", 'w') as switchFile:
                    json.dump(groupSwitchData, switchFile, indent = 4)
                await groupInit.finish(f"审批设置成功:\n状态: {groupMainSwitch}\n日志: {groupLogSwitch}\nUID: {upUID}\n主播: {upName}\n房间号: {upRoomID}\n粉丝牌: {MedalName}\n最低等级要求: {fewerMedalLvL}")


groupReq = on_request(priority = 1, block = False)

@groupReq.handle()
async def groupReq_handle(bot: Bot, event: GroupRequestEvent):
    groupID = str(event.group_id)
    userID = str(event.user_id)
    applyJson = json.loads(event.json())
    applyFlag = applyJson['flag']
    applyUID = applyJson['comment']
    applySubType = applyJson['sub_type']
    approveUID = ''.join(filter(str.isdigit,applyUID))
    switchStatusList = func.loadSwitchFileData(f"{saveDIr}/{saveJson}", groupID)
    if (switchStatusList[0] not in ["groupIdisNull", "off"]):
        getUserMedalInfo = biliAPI.userMedalInfo(approveUID)
        if (getUserMedalInfo[0] == 0):
            userMedalLvL = int(getUserMedalInfo[1][0])
            userMedalName = getUserMedalInfo[1][1]

            if (switchStatusList[4] == userMedalName):
                if (userMedalLvL >= switchStatusList[3]):
                    approveStatus = "pass"
                else:
                    approveStatus = "lvlLow"
            else:
                approveStatus = "medalMissing"

            if (approveStatus == "pass"):
                await bot.set_group_add_request(
                    flag = applyFlag,
                    sub_type = applySubType,
                    approve = True,
                    reason = " ",
                )
            elif (approveStatus == "lvlLow"):
                await bot.set_group_add_request(
                    flag = applyFlag,
                    sub_type = applySubType,
                    approve = False,
                    reason = "粉丝牌等级过低",
                )

        else:
            await bot.set_group_add_request(
                    flag = applyFlag,
                    sub_type = applySubType,
                    approve = False,
                    reason = "请打开粉丝牌展示, 并佩戴匹配该群的粉丝牌!",
                )
    else:
        pass