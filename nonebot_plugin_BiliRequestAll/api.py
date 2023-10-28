# @python  : 3.11.0
# @Time    : 2023/9/29
# @Author  : Shadow403
# @Version : 0.2.7
# @Email   : admin@shadow403.cn
# @Software: Visual Studio Code

"""
API File
"""

import requests, json
requests.packages.urllib3.disable_warnings()

class biliAPI:
    """
    `API_URL`: https://api-dev.shadow403.cn
    """

    def __init__(self):
        self.url = "https://api-dev.shadow403.cn/api/bilibili"

    def upMedalInfo(self, upUID:str):
        """
        Get Medal `ID` `Name`
        """
        try:
            getMedalInfo = json.loads(requests.get(f"{self.url}/medal/owner/{upUID}").text)
            getUpName = getMedalInfo['data']['uname']
            getUpRoomID = getMedalInfo['data']['room_id']
            getMedalName = getMedalInfo['data']['medal_name']

        except Exception as ErrorGetMedalInfo:
            return [-1, f"{str(ErrorGetMedalInfo)}"]
        if (getMedalInfo['code'] == 200):
            if (getMedalName != ""):
                return [0, [getUpName, getUpRoomID, getMedalName]]
            else:
                return [-1, "medalNameMissing"]
        else:
            return [-2, f"{getMedalInfo['message']}"]
        
    def userMedalInfo(self, UID):
        """
        Get Medal `level` `name`
        """
        try:
            getUserMedalInfo = json.loads(requests.get(f"{self.url}/user/medal/{UID}").text)
        except Exception as ErrorGetUserMedalInfo:
            return [-1, f"{str(ErrorGetUserMedalInfo)}"]
        
        if (getUserMedalInfo['code'] == 200):
            getUserMedal = getUserMedalInfo['data']['fans_medal']['medal']
            if (getUserMedal != None):
                userMedalLvL = getUserMedal['level']
                userMedalName = getUserMedal['medal_name']

                return [0, [userMedalLvL, userMedalName]]
            
            else:
                return[-1, "userMedalMissing"]
        else:
            return [-2, f"{str(getUserMedalInfo)}"]
