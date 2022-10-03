<p align="center">
  <a href="https://v2.nonebot.dev/"><img src="https://raw.githubusercontent.com/Shadow403/nonebot_plugin_BiliRequestAll/image/nonebot_plugin_BilirequestAll_logo.png" width="300" height="300" alt="nonebot"></a>
</p>

<div align="center"> 

# nonebot_plugin_BiliRequestAll

<div>

<div align=left> <div>

## 已实现功能
- 单插件分群管理
- 以B站UID审核入群（粉丝）
- 以B站UID审核入群（粉丝团）

## 安装方法

- 使用pip
```
pip install nonebot_plugin_BiliRequestAll
```

- 放入src\plugin目录下
- 重新加载插件

## 说明依赖
```
10| import os, json, time, requests
11| from xml.etree.ElementTree import Comment
12| from nonebot.adapters import Message
13| from nonebot.params import CommandArg
14| from nonebot.permission import SUPERUSER
15| from nonebot import on_request,on_command, logger
16| from nonebot.adapters.onebot.v11 import Bot, GroupRequestEvent, GroupMessageEvent
17| from nonebot.adapters.onebot.v11.permission import GROUP_OWNER, GROUP_ADMIN
```
## 命令
### 基础命令
- #### <font color="red"> /req initialize </font> # 初始化群审核插件
- #### <font color="red"> /req </font> <font color="green"> on/off </font> # 群审核主开关
- #### <font color="red"> /req fans </font> <font color="green"> on/off </font> # 群审核粉丝开关
- #### <font color="red"> /req barand </font> <font color="green"> on/off </font> # 群审核粉丝团开关
- #### <font color="grey"> /req crewmate </font> <font color="grey"> on/off </font> <font color="grey"># 群审核大航海船员开关（暂未实现）</font>
### 配置参数命令
- #### <font color="red"> /upuid </font> <font color="green"> <纯数字> </font> # 配置主播UID
- #### <font color="red"> /liveid </font> <font color="green"> <纯数字> </font> # 配置直播间号
- #### <font color="red"> /barandname </font> <font color="green"> <粉丝牌名> </font> # 配置粉丝牌名 

## 注意事项
```
加载插件并初始完成后，会在机器人目录下创建'switcher_group'文件夹,进入文件夹
找到文件'@cookie.json'打开

  {"cookie": "<Put Your Cookie In Here>"}  #将cookie完整粘贴进这里
              ^^^^^^^^^^^^^^^^^^^^^^^^^
              
保存，关闭文件
```
<p align="center">
  <a href="https://raw.githubusercontent.com/Shadow403/nonebot_plugin_BiliRequestAll/image/nonebot_plugin_BiliRequestAll_cookie.png"><img src="https://raw.githubusercontent.com/Shadow403/nonebot_plugin_BiliRequestAll/image/nonebot_plugin_BiliRequestAll_cookie.png" width="1000" height="600" alt="nonebot"></a>
</p>

## 未来计划
- ### Tips：如果在不咕的情况下 
  - 审核大航海船员
  - UID一次性化
  - 群黑白名单

### 反馈问题
- #### 邮箱：anonymous_hax@foxmail.com