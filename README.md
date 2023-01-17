<p align="center">
  <a href="https://v2.nonebot.dev/"><img src="https://raw.githubusercontent.com/Shadow403/nonebot_plugin_BiliRequestAll/image/nonebot_plugin_BilirequestAll_logo.png" width="300" height="300" alt="nonebot"></a>
</p>

<div align="center"> 

# nonebot_plugin_BiliRequestAll

<div>

<div align=left> <div>


<p align="center">
  <img src=https://img.shields.io/github/stars/Shadow403/nonebot_plugin_BiliRequestAll.svg alt="Start">
  <img src="https://img.shields.io/badge/python-3.10+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/nonebot-2.0.0b1+-red.svg" alt="NoneBot">
  <img src="https://img.shields.io/badge/onebot-2.0.0b1+-darkgreen.svg" alt="OneBot">
  </a>
</p>

## 已实现功能
- 单插件分群管理
- 以B站UID审核入群（粉丝）
- 以B站UID审核入群（粉丝团）
- 以B站UID审核入群（大航海）

## 安装方法

```
pip install nonebot_plugin_BiliRequestAll
```

## 说明依赖
```
XX| [可运行依赖版本]                       [测试依赖版本]
01| nonebot2 >= 2.0.0b1                   [2.0.0rc2]
02| nonebot-adapter-onebot >= 2.0.0b1     [2.2.0]
03| requests >= 2.2                       [2.28.2]
04| os, json, time                        [XX]
```
## 命令
- ### /init [uid]  # 初始化群审核插件
- ### /switch [主开关]，[粉丝]，[粉丝团]，[大航海]，[日志] 
- ### ("[ ]"中填写开/关，注意顺序，要用"，"隔开)

## 注意事项
```
加载插件并初始完成后，会在机器人目录下创建'group_switcher'文件夹,进入文件夹
找到文件'cookies.json'打开

  {"cookies": "<Put Your Cookie In Here>"}  #将cookie完整粘贴进这里
              ^^^^^^^^^^^^^^^^^^^^^^^^^
              
保存，关闭文件
```
<p align="center">
  <a href="https://raw.githubusercontent.com/Shadow403/nonebot_plugin_BiliRequestAll/image/nonebot_plugin_BiliRequestAll_cookie.png"><img src="https://raw.githubusercontent.com/Shadow403/nonebot_plugin_BiliRequestAll/image/nonebot_plugin_BiliRequestAll_cookie.png" width="1000" height="600" alt="nonebot"></a>
</p>

## 未来计划
- ### 强审核模式

## 反馈问题
- ### 邮箱：anonymous_hax@foxmail.com

<details>
<summary>[日志]展开/收起</summary>

- 2022/10/03 发布此插件
- 2023/01/18 更新插件数据结构，新增大航海入群功能
