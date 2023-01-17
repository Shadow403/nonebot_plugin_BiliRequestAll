# python  : 3.10.5
# Time    : 2023/1/19
# Author  : Shadow403
# Email   : anonymous_hax@foxmail.com
# Software: Visual Studio Code

import os, json, requests, logging, datetime

from nonebot.adapters import Message
from nonebot.params import CommandArg
from nonebot.permission import SUPERUSER
from nonebot import on_request, on_command
from nonebot.adapters.onebot.v11 import Bot, GroupRequestEvent, GroupMessageEvent
from nonebot.adapters.onebot.v11.permission import GROUP_OWNER, GROUP_ADMIN

file_dir = 'group_switcher'
log_dir = 'log'
cookies_json = 'cookies.json'
cookies_init = {"cookies": "<Put Your Cookie In Here>"}

if not os.path.exists('group_switcher'):
    os.makedirs('group_switcher')

cookies_config = os.path.join(file_dir, cookies_json)
if not os.path.exists(cookies_config):
    with open(cookies_config, 'w') as initial:
        json.dump(cookies_init, initial)

cookies_fullPath = os.path.join(file_dir, cookies_json)
cookies_json = json.load(open(cookies_fullPath))
cookies_ = cookies_json['cookies']

headers_ = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux) Gecko/20100101 Firefox/64.0",
            "cookies":cookies_
           }

def init(groupid, uid):

    groupid_str = str(groupid)
    uid_str = str(uid)

    makedir = os.path.join(file_dir, groupid_str)
    if not os.path.exists(makedir):
        os.makedirs(makedir)

    config_fullPath = os.path.join(file_dir, groupid_str, 'config.json')
    captain_fullPath = os.path.join(file_dir, groupid_str, 'captain.json')

    info_url = ("https://api.bilibili.com/x/space/acc/info?mid=" + uid_str)
    
    info = requests.get(info_url, headers = headers_)
    info_json = json.loads(info.text)
    info_code = str(info_json['code'])
    if (info_code == '0'):
        info_name = str(info_json['data']['name'])

        if (info_json['data']['live_room'] != None):

            info_roomid = str(info_json['data']['live_room']['roomid'])

            captain_url_info = ("https://api.live.bilibili.com/xlive/app-room/v2/guardTab/topList?roomid=" + info_roomid + "&page=1&ruid=" + uid_str + "&page_size=30")
            
            captain_info = requests.get(captain_url_info, headers = headers_)
            captain_json = json.loads(captain_info.text)
            captain_code = str(captain_json['code'])

            if (captain_code == '0'):
                captain_page = captain_json['data']['info']['page']
                captain_num = captain_json['data']['info']['num']

                if os.path.exists(config_fullPath):
                    with open(config_fullPath, 'r', encoding = 'utf-8') as load_config:
                        updata_config = json.load(load_config)
                        updata_config_json = {"live":{"roomid":info_roomid,"captain_num":captain_num}}
                        updata_config.update(updata_config_json)
                
                    with open(config_fullPath, 'w', newline = '\n', encoding = 'utf-8') as config_updata:
                        json.dump(updata_config, config_updata, indent = 4, ensure_ascii = False)

                if not os.path.exists(config_fullPath):
                    init_live_json = {"uid":uid,"name":info_name,"live":{"roomid":info_roomid,"captain_num":captain_num},"switcher":[{"main":1,"fans":0,"barand":0,"captain":0,"log":0}]}
                    init_live_data = json.dumps(init_live_json, indent = 4, ensure_ascii = False)
                    
                    with open(config_fullPath, 'w', newline = '\n', encoding = 'utf-8') as init_live:
                        init_live.write(init_live_data)

                if not os.path.exists(captain_fullPath):
                    init_captain_json = {"captain_page":captain_page,"captain_num":captain_num}
                    init_captain_data = json.dumps(init_captain_json, indent = 4, ensure_ascii = False)

                    with open(captain_fullPath, 'w', newline = '\n', encoding = 'utf-8') as init_captain:
                        init_captain.write(init_captain_data)
                
                    captain_top3 = captain_json['data']['top3']
                    for captain_list_t3 in captain_top3:
                        top3_uid = captain_list_t3['uid']
                        top3_name = captain_list_t3['username']
                        top3_level = captain_list_t3['medal_info']['medal_level']

                        with open(captain_fullPath, 'r', encoding = 'utf-8') as load_config:
                            content_t3 = json.load(load_config)
                            updata_config_json = {top3_uid:{"name":top3_name,"level":top3_level}}
                            content_t3.update(updata_config_json)
                    
                        with open(captain_fullPath, 'w', newline = '\n', encoding = 'utf-8') as config_updata:
                            json.dump(content_t3, config_updata, indent = 4, ensure_ascii = False)

                    page = 1
                    for i in range(captain_page):
                        captain_url_normal = ("https://api.live.bilibili.com/xlive/app-room/v2/guardTab/topList?roomid={}&page=" + str(page) + "&ruid=" + uid_str + "&page_size=30").format(info_roomid)
                        captain_normal_info = requests.get(captain_url_normal, headers = headers_)
                        captain_normal_json = json.loads(captain_normal_info.text)
                        captain_normal_code = str(captain_normal_json['code'])

                        if (captain_normal_code == '0'):
                            captain_normal = captain_normal_json['data']['list']
                            for captain_list in captain_normal:
                                normal_uid = captain_list['uid']
                                normal_name = captain_list['username']
                                normal_level = captain_list['medal_info']['medal_level']

                                with open(captain_fullPath, 'r', encoding = 'utf-8') as load_config:
                                    content_nor = json.load(load_config)
                                    updata_config_json = {normal_uid:{"name":normal_name,"level":normal_level}}
                                    content_nor.update(updata_config_json)
                            
                                with open(captain_fullPath, 'w', newline = '\n', encoding = 'utf-8') as config_updata:
                                    json.dump(content_nor, config_updata, indent = 4, ensure_ascii = False)
                        page = page + 1
                        
                else:
                    print('File[captain.json] --> Exists/Updata')
            else:
                print('Error[Captain] --> ' + captain_code)

        else:
            init_Nlive_json = {"uid":uid,"name":info_name,"live":None,"switcher":[{"main":1,"fans":0,"log":0}]}
            init_Nlive_data = json.dumps(init_Nlive_json, indent = 4, ensure_ascii = False)
            with open(config_fullPath, 'w', newline = '\n', encoding = 'utf-8') as init_Nlive:
                init_Nlive.write(init_Nlive_data)

    else:
        print('Error[userinfo] --> ' + info_code)

def request(groupid, uid, getID):
    groupid_str = str(groupid)
    uid_str = str(uid)
    bot:Bot

    time_data = datetime.datetime.now()
    log_data = time_data.strftime("%Y-%m-%d")

    config_fullPath = os.path.join(file_dir, groupid_str, 'config.json')
    captain_fullPath = os.path.join(file_dir, groupid_str, 'captain.json')
    log_fullPath_mkdir = os.path.join(file_dir, groupid_str, log_dir)
    log_fullPath = os.path.join(file_dir, groupid_str, log_dir, log_data + '.log')

    config_json = json.load(open(config_fullPath))
    load_config_json = json.load(open(captain_fullPath, encoding = 'utf-8'))

    load_uid = config_json['uid']
    load_live = config_json['live']
    load_switch_log = config_json['switcher'][0]['log']
    load_switch_main = config_json['switcher'][0]['main']
    load_switch_fans = config_json['switcher'][0]['fans']


    if (load_live != None):
        load_live_roomid = config_json['live']['roomid']
        load_live_captain_num = config_json['live']['captain_num']
        load_switch_barand = config_json['switcher'][0]['barand']
        load_switcher_captain = config_json['switcher'][0]['captain']

    if (load_switch_log == 1):
        if not os.path.exists(log_fullPath_mkdir):
            os.makedirs(log_fullPath_mkdir)

    if (load_switch_main == 1):
        
        if (load_switcher_captain == 1):
            captain_url = ("https://api.live.bilibili.com/xlive/app-room/v2/guardTab/topList?roomid={}&page=1&ruid=" + str(load_uid) + "&page_size=30").format(str(load_live_roomid))
            captain_info = requests.get(captain_url, headers = headers_)
            captain_json = json.loads(captain_info.text)
            captain_code = str(captain_json['code'])
            if (captain_code == '0'):
                captain_num = captain_json['data']['info']['num']

                if (captain_num == load_live_captain_num):
                    if uid_str in load_config_json:
                        print('pass')
                        logging.basicConfig(filename = log_fullPath, level = logging.INFO, 
                        format='%(asctime)s %(levelname)s %(message)s')
                        logging.info('QQ --> ' + str(getID) + '  UID --> ' + uid_str + ' [CAPTAIN PASS]')
                        return 1

                    else:
                        print('blocked')
                        logging.basicConfig(filename = log_fullPath, level = logging.INFO, 
                        format='%(asctime)s %(levelname)s %(message)s')
                        logging.info('QQ --> ' + str(getID) + '  UID --> ' + uid_str + ' [CAPTAIN BLOCKED]')

                elif (captain_num != load_live_captain_num):
                    os.remove(captain_fullPath)
                    init(groupid, uid)

        if (load_switch_barand == 1):
            barand_url = ("https://api.live.bilibili.com/xlive/web-ucenter/user/MedalWall?target_id=".format(uid_str))
            barand_info = requests.get(barand_url, headers = headers_)
            barand_json = json.loads(barand_info.text)
            barand_code = str(barand_json['code'])

            if (barand_code == '0'):
                barand_arr = barand_json['data']['list']

                for barand_list in barand_arr:
                    barand_uid = barand_list['mid']

                    if (str(barand_uid) in str(load_uid)):
                        print('pass')
                        logging.basicConfig(filename = log_fullPath, level = logging.INFO, 
                        format='%(asctime)s %(levelname)s %(message)s')
                        logging.info('QQ --> ' + str(getID) + '  UID --> ' + uid_str + ' [BARAND PASS]')
                        return 1

            elif (barand_code == '22115'):
                print('Error[barrand_requests] --> No Perm')
                logging.basicConfig(filename = log_fullPath, level = logging.INFO, 
                format='%(asctime)s %(levelname)s %(message)s')
                logging.info('QQ --> ' + str(getID) + '  UID --> ' + uid_str + ' [BARAND BLOCKED_PREM]')
            
            else:
                print('Error[barrand_requests] --> ' + barand_code)
                logging.basicConfig(filename = log_fullPath, level = logging.INFO, 
                format='%(asctime)s %(levelname)s %(message)s')
                logging.error('QQ --> ' + str(getID) + '  UID --> ' + uid_str + ' [BARAND ERROR' + barand_code + ']')

        if (load_switch_fans == 1): 
            sub_url = ("https://api.bilibili.com/x/relation/followings?vmid={}&pn=1&ps=50&order=desc&order_type=attention".format(uid_str))
            sub_info = requests.get(sub_url, headers = headers_)
            sub_json = json.loads(sub_info.text)
            sub_code = str(sub_json['code'])

            if (sub_code == '0'):
                sub_arr = sub_json['data']['list']

                for sub_list in sub_arr:
                    sub_uid = sub_list['mid']

                    if (str(sub_uid) in str(load_uid)):
                        print('pass')
                        logging.basicConfig(filename = log_fullPath, level = logging.INFO, 
                        format='%(asctime)s %(levelname)s %(message)s')
                        logging.error('QQ --> ' + str(getID) + '  UID --> ' + uid_str + ' [FANS PASS]')
                        return 1

            elif (sub_code == '22115'):
                print('Error[sub_requests] --> No Perm')
                logging.basicConfig(filename = log_fullPath, level = logging.INFO, 
                format='%(asctime)s %(levelname)s %(message)s')
                logging.info('QQ --> ' + str(getID) + '  UID --> ' + uid_str + ' [FANS BLOCKED_PREM]')

            else:
                print('Error[sub_requests] --> ' + sub_code)
                logging.basicConfig(filename = log_fullPath, level = logging.INFO, 
                format='%(asctime)s %(levelname)s %(message)s')
                logging.error('QQ --> ' + str(getID) + '  UID --> ' + uid_str + ' [FANS ERROR' + sub_code + ']')

def main_Switch(group_id, main, fans, barand, captain, log):
    
    groupid_str = str(group_id)
    config_fullPath = os.path.join(file_dir, groupid_str, 'config.json')
    
    with open(config_fullPath, 'r', encoding = 'utf-8') as load_switch:
        content_switch = json.load(load_switch)
        for switch in content_switch['switcher']:
            switch['main'] = main
            switch['fans'] = fans
            switch['barand'] = barand
            switch['captain'] = captain
            switch['log'] = log

    with open(config_fullPath, 'w', newline = '\n', encoding = 'utf-8') as switch_updata:
        json.dump(content_switch, switch_updata, indent = 4, ensure_ascii = False)

initial = on_command('/init', priority = 1, block = False, permission = GROUP_OWNER | GROUP_ADMIN | SUPERUSER)
switch = on_command('/switch', priority = 2, block = False, permission = GROUP_OWNER | GROUP_ADMIN | SUPERUSER)

@initial.handle()
async def initial_(event: GroupMessageEvent, initial: Message = CommandArg()):
    groupid = str(event.group_id)
    initial_ = initial.extract_plain_text()
    config_fullPath = os.path.join(file_dir, groupid , 'config.json')
    captain_fullPath = os.path.join(file_dir, groupid , 'captain.json')
    if os.path.exists(config_fullPath):
        os.remove(config_fullPath)
    if os.path.exists(captain_fullPath):
        os.remove(captain_fullPath)
    init(groupid, initial_)

@switch.handle()
async def initial_(event: GroupMessageEvent, switch: Message = CommandArg()):
    groupid = str(event.group_id)
    switch_ = switch.extract_plain_text()
    switch_list = switch_.split("，")

    if switch_list[0] in ["开", "开启"]:
        main = 1
    elif switch_list[0] in ["关", "关闭"]:
        main = 0

    if switch_list[1] in ["开", "开启"]:
        fans = 1
    elif switch_list[1] in ["关", "关闭"]:
        fans = 0

    if switch_list[2] in ["开", "开启"]:
        barand = 1
    elif switch_list[2] in ["关", "关闭"]:
        barand = 0

    if switch_list[3] in ["开", "开启"]:
        captain = 1
    elif switch_list[3] in ["关", "关闭"]:
        captain = 0

    if switch_list[4] in ["开", "开启"]:
        log = 1
    elif switch_list[4] in ["关", "关闭"]:
        log = 0
    main_Switch(groupid, main, fans, barand, captain, log)

group_req = on_request(priority=1, block=False)

@group_req.handle()
async def request_fans_(bot: Bot, event: GroupRequestEvent):
    groupid = str(event.group_id)
    getID = str(event.user_id)
    uid_json = json.loads(event.json())
    flag = uid_json['flag']
    uid_str = uid_json['comment']
    sub_type = uid_json['sub_type']
    uid = ''.join(filter(str.isdigit,uid_str))
    status = request(groupid, uid, getID)

    if status == 1:
        await bot.set_group_add_request(
            flag = flag,
            sub_type = sub_type,
            approve = True,
            reason=' ',
        )