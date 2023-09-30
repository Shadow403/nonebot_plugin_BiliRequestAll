# @python  : 3.11.0
# @Time    : 2023/9/29
# @Author  : Shadow403
# @Version : 0.3.0
# @Email   : anonymous_hax@foxmail.com
# @Software: Visual Studio Code

import requests, json
requests.packages.urllib3.disable_warnings()

class biliAPI:
    """
    `requests`: https://require-api.orange25.site
    """

    def __init__(self):
        self.url = "https://require-api.orange25.site"

    def upMedalInfo(self, upUID:str):
        """
        Get Medal `ID` `Name`
        """
        try:
            getMedalInfo = json.loads(requests.get(f"{self.url}/bilibili/medal/{upUID}").text)
            getUpName = getMedalInfo['data']['info']['uname']
            getUpRoomID = getMedalInfo['data']['room_id']
            getMedalName = getMedalInfo['data']['medal_name']

        except Exception as ErrorGetMedalInfo:
            return [-1, f"{str(ErrorGetMedalInfo)}"]
        if (getMedalInfo['code'] == 0):
            if (getMedalName != ""):
                return [0, [getUpName, getUpRoomID, getMedalName]]
            else:
                return [-1, "medalNameMissing"]
        else:
            return [-2, f"{getMedalInfo['message']}"]
        
    def userMedalInfo(self, UID):
        try:
            getUserMedalInfo = json.loads(requests.get(f"{self.url}/bilibili/info/{UID}/min").text)
        except Exception as ErrorGetUserMedalInfo:
            return [-1, f"{str(ErrorGetUserMedalInfo)}"]
        
        if (getUserMedalInfo['code'] == 0):
            getUserMedal = getUserMedalInfo['fans_medal']['medal']
            if (getUserMedal != None):
                userMedalLvL = getUserMedal['level']
                userMedalName = getUserMedal['medal_name']

                return [0, [userMedalLvL, userMedalName]]
            
            else:
                return[-1, "userMedalMissing"]
        else:
            return [-2, f"{str(getUserMedalInfo)}"]
