# @python  : 3.11.0
# @Time    : 2023/9/29
# @Author  : Shadow403
# @Version : 0.2.5
# @Email   : admin@shadow403.cn
# @Software: Visual Studio Code

"""
Function File
"""

import json

def switchStatus(switchText:str):
    """
    switchText:`str`
    """
    switchAliases = {"turnOn":["on","开","开启"],"turnOff":["off","关","关闭"]}

    if (switchText in switchAliases["turnOn"]):
        return "on"
    elif (switchText in switchAliases["turnOff"]):
        return "off"
    else:
        return 'error'
    
def loadSwitchFileData(filePath, groupID):
    with open(f"{filePath}", "r") as switchData:
        groupSwitchData = json.load(switchData)
        if (groupID in dict(groupSwitchData['data'])):
            return groupSwitchData['data'][groupID]
        else:
            return ["groupIdisNull"]