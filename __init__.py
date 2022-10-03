# python 3.10.5
# Time    : 2022/10/03
# Author  : Shadow403
# Email   : anonymous_hax@foxmail.com
# File    : BiliRequestAll.py
# Software: Visual Studio Code

version = '0.1.0'

import os, json, time, requests
from nonebot.adapters import Message
from nonebot.params import CommandArg
from nonebot.permission import SUPERUSER
from nonebot import on_request, on_command, logger
from nonebot.adapters.onebot.v11 import Bot, GroupRequestEvent, GroupMessageEvent
from nonebot.adapters.onebot.v11.permission import GROUP_OWNER, GROUP_ADMIN

filesave_dir = 'switcher_group' # 文件夹名称
cookie = '@cookie.json' # cookie文件名

request_main = on_command('/req', priority = 1, block = False, permission = GROUP_OWNER | GROUP_ADMIN | SUPERUSER)              # 主开关
request_initial = on_command('/req initialize', priority = 1, block = False, permission = GROUP_OWNER | GROUP_ADMIN | SUPERUSER)   # 初始化
request_fans = on_command('/req fans', priority = 1, block = False, permission = GROUP_OWNER | GROUP_ADMIN | SUPERUSER)         # 粉丝开关
request_barand = on_command('/req barand', priority = 1, block = False, permission = GROUP_OWNER | GROUP_ADMIN | SUPERUSER)     # 粉丝牌开关
request_crewmate = on_command('/req crewmate', priority = 1, block = False, permission = GROUP_OWNER | GROUP_ADMIN | SUPERUSER) # 船员开关
request_state = on_command('/req state', priority = 1, block = False, permission = GROUP_OWNER | GROUP_ADMIN | SUPERUSER)       # 状态查询

upuid_request = on_command('/upuid', priority = 1, block = False, permission = GROUP_OWNER | GROUP_ADMIN | SUPERUSER)           # 主播UID
liveid_request = on_command('/liveid', priority = 1, block = False, permission = GROUP_OWNER | GROUP_ADMIN | SUPERUSER)         # 直播间ID
barandname_request = on_command('/barandname', priority = 1, block = False, permission = GROUP_OWNER | GROUP_ADMIN | SUPERUSER) # 粉丝牌名
# show_cookie = on_command('/show cookie', priority = 1, block = False, permission = SUPERUSER)                                 # 显示cookie

# 创建配置文件
@request_initial.handle()
async def request_initial_(event: GroupMessageEvent):
    group_id = str(event.group_id)
    filename = group_id + '.json' # 创建文件名
    if not os.path.exists('switcher_group'): # 判断文件是否存在
        os.makedirs('switcher_group') # 创建 switcher_group 文件夹
    filesave_full_path = os.path.join(filesave_dir, filename) # 完整保存路径
    cookie_full_path = os.path.join(filesave_dir, cookie)     # cookie 保存路径
    switcher_start = {'group_id': group_id, 'request': "off", 'fans': "off", 'barand': "off", 'crewmate': "off", 'up_uid': "", 'up_live_id': "", 'barand_name' : ""} # 初始化
    cookies_start = {'cookie': "<Put Your Cookie In Here>"} # 创建cookies存放文件
    with open(filesave_full_path, 'w') as initial: # 初始化开关状态
        json.dump(switcher_start, initial) # 写入初始化内容
        logger.info('已创建' + filename + '文件' )
    if not os.path.exists(cookie_full_path): # 判断文件是否存在
        with open(cookie_full_path, 'w') as cookie_initial: # 初始化cookie
            json.dump(cookies_start, cookie_initial) # 写入初始化cookie内容
            logger.info('已创建' + cookie + '文件')
    await request_initial.send('初始化成功')

# 主开关
@request_main.handle()
async def request_main_(event: GroupMessageEvent, request_main_: Message = CommandArg()):
    group_id = str(event.group_id)
    filename = group_id + '.json' # 文件名
    filesave_full_path = os.path.join(filesave_dir, filename) # 完整路径
    with open (filesave_full_path, 'rb') as load_request_initial: # 记录主开关状态
        updata = json.load(load_request_initial)
        request_switch = request_main_.extract_plain_text() # 提取主开关信息
        updata['request'] = request_switch # 更新主开关状态
        dict = updata
    load_request_initial.close # 关闭文件
    with open(filesave_full_path, 'w') as write_switch_request: #写入主开关状态
        json.dump(dict,write_switch_request) # 写入更新主开关状态后的字符
    write_switch_request.close # 关闭文件
    
    switcher_group = (dict['group_id']) # 群ID
    switcher_request = (dict['request']) # 主开关
    if group_id in switcher_group:
        if 'on' in switcher_request:
            await request_main.send(f'主开关：开') # 发送开启成功主开关通知
        else:
            await request_main.send(f'主开关：关') # 发送关闭成功主开关通知
    else:
        await request_main.send('未初始化')

# 粉丝开关
@request_fans.handle()
async def request_fans_(event: GroupMessageEvent, request_fans_: Message = CommandArg()):
    group_id = str(event.group_id)
    filename = group_id + '.json' # 文件名
    filesave_full_path = os.path.join(filesave_dir, filename) # 完整路径
    with open (filesave_full_path, 'rb') as load_request_fans: # 记录粉丝开关状态
        updata = json.load(load_request_fans)
        request_switch = request_fans_.extract_plain_text() # 提取粉丝开关信息
        updata['fans'] = request_switch # 更新粉丝开关状态
        dict = updata
    load_request_fans.close # 关闭文件
    with open(filesave_full_path, 'w') as write_switch_request: #写入粉丝开关状态
        json.dump(dict,write_switch_request) # 写入更新主开关状态后的字符
    write_switch_request.close # 关闭文件
    
    switcher_group = (dict['group_id'])
    switcher_request = (dict['request']) # 主开关
    switcher_fans = (dict['fans']) # 粉丝开关
    if group_id in switcher_group:
        if 'on' in switcher_request:
            if 'on' in switcher_fans:
                await request_fans.send(f'粉丝开关：开') # 发送开启成功粉丝开关通知
            else:
                await request_fans.send(f'粉丝开关：关') # 发送关闭成功粉丝开关通知
        else:
            await request_fans.send('提示：主开关未打开')
    else:
        await request_fans.send('未初始化')

#粉丝团开关
@request_barand.handle()
async def request_barand_(event: GroupMessageEvent, request_barand_: Message = CommandArg()):
    group_id = str(event.group_id)
    filename = group_id + '.json' # 文件名
    filesave_full_path = os.path.join(filesave_dir, filename)  # 完整路径
    with open (filesave_full_path, 'rb') as load_request_fans: # 记录粉丝牌开关状态
        updata = json.load(load_request_fans)
        request_switch = request_barand_.extract_plain_text()  # 提取粉丝牌开关信息
        updata['barand'] = request_switch # 更新粉丝牌开关状态
        dict = updata
    load_request_fans.close # 关闭文件
    with open(filesave_full_path, 'w') as write_switch_request: #写入粉丝牌开关状态
        json.dump(dict,write_switch_request) # 写入更新粉丝牌开关状态后的字符
    write_switch_request.close # 关闭文件
    
    switcher_group = (dict['group_id'])
    switcher_request = (dict['request']) # 主开关
    switcher_barand = (dict['barand']) # 粉丝牌开关
    if group_id in switcher_group:
        if 'on' in switcher_request:
            if 'on' in switcher_barand:
                await request_barand.send(f'粉丝团：开') # 发送开启成功粉丝牌开关通知
            else:
                await request_barand.send(f'粉丝团：关') # 发送关闭成功粉丝牌开关通知
        else:
            await request_barand.send('提示：主开关未打开')
    else:
        await request_barand.send('未初始化')

#大航海船员开关
@request_crewmate.handle()
async def request_crewmate_(event: GroupMessageEvent, request_crewmate_: Message = CommandArg()):
    group_id = str(event.group_id)
    filename = group_id + '.json' # 文件名
    filesave_full_path = os.path.join(filesave_dir, filename) # 完整路径
    with open (filesave_full_path, 'rb') as load_request_fans:  # 记录大航海船员开关状态
        updata = json.load(load_request_fans)
        request_switch = request_crewmate_.extract_plain_text() # 提取大航海船员开关信息
        updata['crewmate'] = request_switch # 更新大航海船员开关状态
        dict = updata
    load_request_fans.close # 关闭文件
    with open(filesave_full_path, 'w') as write_switch_request: #写入大航海船员开关状态
        json.dump(dict,write_switch_request) # 写入更新大航海船员开关状态后的字符
    write_switch_request.close # 关闭文件
    
    switcher_group = (dict['group_id'])
    switcher_request = (dict['request']) # 主开关
    switcher_crewmate = (dict['crewmate']) # 大航海船员开关
    if group_id in switcher_group:
        if 'on' in switcher_request:
            if 'on' in switcher_crewmate:
                await request_crewmate.send(f'船员：开') # 发送开启成功大航海船员开关通知
            else:
                await request_crewmate.send(f'船员：关') # 发送关闭成功大航海船员开关通知
        else:
            await request_crewmate.send('提示：主开关未打开')
    else:
        await request_crewmate.send('未初始化')

# 状态信息
@request_state.handle()
async def request_state_(event: GroupMessageEvent):
    group_id = str(event.group_id)
    filename = group_id + '.json' # 文件名
    filesave_full_path = os.path.join(filesave_dir, filename) # 完整路径
    load_file = open(filesave_full_path) # 打开文件
    dict = json.load(load_file)          # 加载文件信息
    # 读取指定开关内容
    switcher_groupid = (dict['group_id'])      # 群ID
    switcher_request = (dict['request'])       # 主开关
    switcher_fans = (dict['fans'])             # 粉丝开关
    switcher_barand = (dict['barand'])         # 粉丝牌开关
    switcher_crewmate = (dict['crewmate'])     # 船员开关
    upuid_request = (dict['up_uid'])           # 主播UID
    liveid_request = (dict['up_live_id'])      # 直播间ID
    barandname_request = (dict['barand_name']) # 粉丝牌名
    if int(switcher_groupid) == event.group_id:
        await request_state.send('本群审核开关\n主开关：' + switcher_request + '\n粉丝开关：' + switcher_fans + '\n粉丝团开关：' + switcher_barand + '\n大航海船员开关：' + switcher_crewmate + '\n\n主播UID：' + upuid_request + '\n主播直播间ID：' + liveid_request + '\n牌子名称：' + barandname_request)
    else:
        await request_state.send('未初始化')

# 主播uid
@upuid_request.handle()
async def upuid_request_(event: GroupMessageEvent, upuid_request_: Message = CommandArg()):
    group_id = str(event.group_id)
    filename = group_id + '.json' # 文件名
    filesave_full_path = os.path.join(filesave_dir, filename) # 完整路径
    with open (filesave_full_path, 'rb') as load_uid_request: # 记录UID
        updata = json.load(load_uid_request)
        upuid = upuid_request_.extract_plain_text() # 提取UID信息
        updata['up_uid'] = upuid                    # 更新UID内容
        dict = updata
    load_uid_request.close                          # 关闭文件
    with open(filesave_full_path, 'w') as upuid:    #写入UID信息
        json.dump(dict,upuid)                       # 写入更新UID后的字符
    upuid.close                                     # 关闭文件
    
    switcher_groupid = (dict['group_id'])
    switcher_request = (dict['request']) # 主开关
    if int(switcher_groupid) == event.group_id:
        if 'on' in switcher_request:
            await upuid_request.send('主播UID更新为：' + upuid_request_) # 发送UID更新成功
        else:
            await upuid_request.send('提示：提示：主开关未打开')
    else:
        await upuid_request.send('未初始化')

# 直播间id
@liveid_request.handle()
async def live_request_(event: GroupMessageEvent, liveid_request_: Message = CommandArg()):
    group_id = str(event.group_id)
    filename = group_id + '.json' # 文件名
    filesave_full_path = os.path.join(filesave_dir, filename)  # 完整路径
    with open (filesave_full_path, 'rb') as load_live_request: # 记录直播间ID
        updata = json.load(load_live_request)
        liveid = liveid_request_.extract_plain_text()          # 提取直播间ID
        updata['up_live_id'] = liveid                          # 更新直播间ID
        dict = updata
    load_live_request.close                                    # 关闭文件
    with open(filesave_full_path, 'w') as liveid:              #写入直播间ID
        json.dump(dict,liveid)                                 # 写入更新直播间ID后的字符
    liveid.close                                               # 关闭文件
    
    switcher_groupid = (dict['group_id'])
    switcher_request = (dict['request']) # 主开关
    if int(switcher_groupid) == event.group_id:
        if 'on' in switcher_request:
            await liveid_request.send('直播间ID更新为：' + liveid_request_) # 发送直播间ID更新成功
        else:
            await liveid_request.send('提示：主开关未打开')
    else:
        await liveid_request.send('未初始化')

# 粉丝牌名
@barandname_request.handle()
async def barandname_request_(event: GroupMessageEvent, barandname_request_: Message = CommandArg()):
    group_id = str(event.group_id)
    filename = group_id + '.json' # 文件名
    filesave_full_path = os.path.join(filesave_dir, filename)  # 完整路径
    with open (filesave_full_path, 'rb') as load_live_request: # 记录粉丝牌名
        updata = json.load(load_live_request)
        brandaname = barandname_request_.extract_plain_text()  # 提取粉丝牌信息
        updata['barand_name'] = brandaname                     # 更新粉丝牌信息
        dict = updata
    load_live_request.close                                    # 关闭文件
    with open(filesave_full_path, 'w') as brandaname:          #写入粉丝牌信息
        json.dump(dict,brandaname)                             # 写入更新粉丝牌后的字符
    brandaname.close                                           # 关闭文件
    
    switcher_groupid = (dict['group_id'])
    switcher_request = (dict['request']) # 主开关
    if int(switcher_groupid) == event.group_id:
        if 'on' in switcher_request:
            await barandname_request.send('粉丝牌名更新为：' + barandname_request_) # 发送粉丝牌名更新成功
        else:
            await barandname_request.send('提示：主开关未打开')
    else:
        await barandname_request.send('未初始化')

'''
# 显示cookie
@show_cookie.handle()
async def show_cookie_(bot: Bot, event: GroupMessageEvent):

    cookie_full_path = os.path.join(filesave_dir, cookie) # cookie完整路径
    file_cooke = open(cookie_full_path)                   # 打开文件
    load_cookie = json.load(file_cooke)                   # 加载cookie信息
    cookie_ = (load_cookie['cookie'])

    await show_cookie.send('请勿发送cookie给任何人！！！\n\n' + cookie_ + '\n\n请勿发送cookie给任何人！！！')
'''

# 入群审核
group_req = on_request(priority=1, block=False)

@group_req.handle()
async def request_fans_(bot: Bot, event: GroupRequestEvent):
    #加载配置文件
    group_id = str(event.group_id)                            # 群id
    filename = group_id + '.json'                             # 文件名
    filesave_full_path = os.path.join(filesave_dir, filename) # 完整路径
    load_file = open(filesave_full_path)                      # 打开文件
    dict = json.load(load_file)                               # 加载配置文件
    cookie_full_path = os.path.join(filesave_dir, cookie)     # cookie完整路径
    file_cooke = open(cookie_full_path)                       # 打开文件
    load_cookie = json.load(file_cooke)                       # 加载cookie信息
    #提取信息
    switcher_groupid = (dict['group_id'])           # 群ID
    switcher_request = (dict['request'])            # 主开关
    switcher_fans = (dict['fans'])                  # 粉丝开关
    switcher_barand = (dict['barand'])              # 粉丝牌开关
    switcher_crewmate = (dict['crewmate'])          # 船员开关
    upuid_request = (dict['up_uid'])                # 主播uid
    liveid_request = (dict['up_live_id'])           # 直播间id
    barandname_request = (dict['barand_name'])      # 粉丝牌名
    cookie_ = (load_cookie['cookie'])               # cookie展示
    # 开关判断
    if int(switcher_groupid) == event.group_id:
        # 粉丝入群
        if 'on' == switcher_request:   # 判断主开关是否开启
            raw = json.loads(event.json())
            gid = str(event.group_id)
            uid = str(event.user_id)
            flag = raw['flag']
            logger.info('flag:', str(flag))
            sub_type = raw['sub_type']
            comment = raw['comment']
            biliuid = ''.join(filter(str.isdigit,comment))
            if 'on' == switcher_fans:  # 判断粉丝开关是否开启
                url_fans = ('https://api.bilibili.com/x/relation/followings?vmid=' + biliuid + '&pn=1&ps=50&order=desc&order_type=attention') # <- API
                response_fans = requests.get(url_fans)
                response_fans_text = response_fans.text
                logger.info(response_fans_text)
                time.sleep(6)
                # 同意入群
                if upuid_request in response_fans_text:
                        logger.info(f"同意{uid}加入群 {gid},验证消息为 “{comment}”")
                        await bot.set_group_add_request(
                            flag=flag,
                            sub_type=sub_type,
                            approve=True,
                            reason=' ',
                        )
            else:
                logger.error('fans off = group{group_id}')
            # 粉丝团成员入群
            if 'on' == switcher_barand:
                cookies = {"cookie": cookie_}
                url_barand = ('https://api.live.bilibili.com/xlive/web-ucenter/user/MedalWall?target_id=' + biliuid) # <- API
                response_barand = requests.get(url_barand, cookies = cookies)
                response_barand_text = response_barand.text
                logger.info(response_barand_text)
                time.sleep(6)
                # 同意入群
                if barandname_request in response_barand_text:
                        logger.info(f"同意{uid}加入群 {gid},验证消息为 “{comment}”")
                        await bot.set_group_add_request(
                            flag=flag,
                            sub_type=sub_type,
                            approve=True,
                            reason=' ',
                        )
                #未配置cookie提示
                if  '账号未登录' in response_barand_text:
                    logger.error('BiliRequest: 未配置cookies')
            else:
                logger.error('barand off = group{group_id}')
            # 以下功能暂未实现(大航海船员入群)
            '''
            if 'on' == switcher_crewmate:
                cookies = {"cookie": cookie_}
                url_main = ('https://api.live.bilibili.com/xlive/app-room/v2/guardTab/topList?roomid=' + liveid_request + '&page=' + i + '&ruid=' + (upuid_request + '&page_size=30') # <- API
                response = requests.get(url_main, cookies = cookies)
                response_text = response.text
                time.sleep(6)

                # 同意入群
                if biliuid in response_text:
                        logger.info(f"同意{uid}加入群 {gid},验证消息为 “{comment}”")
                        await bot.set_group_add_request(
                            flag=flag,
                            sub_type=sub_type,
                            approve=True,
                            reason=' ',
                        )
                #未配置cookie提示
                if  '账号未登录' in response:
                    logger.error('BiliRequest: 未配置cookies')
            else:
                logger.info('crewmate off')
            '''
