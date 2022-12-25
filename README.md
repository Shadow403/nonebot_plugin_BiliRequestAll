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

## 说明依赖
```
01| nonebot2 >= 2.0.0b1
02| nonebot-adapter-onebot >= 2.0.0b1
03| requests >= 2.5
04| os, json, time
```
## 命令
### 基础命令
- #### /req initialize  # 初始化群审核插件
- #### /req   on/off  # 群审核主开关
- #### /req fans   on/off  # 群审核粉丝开关
- #### /req barand   on/off  # 群审核粉丝团开关
- ####  /req crewmate   on/off  # 群审核大航海船员开关（暂未实现）
### 配置参数命令
- #### /upuid   <纯数字>  # 配置主播UID
- #### /liveid   <纯数字>  # 配置直播间号
- #### /barandname   <粉丝牌名>  # 配置粉丝牌名 

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
