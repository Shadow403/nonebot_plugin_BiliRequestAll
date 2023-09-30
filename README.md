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
  <img src="https://img.shields.io/badge/nonebot-2.0.0+-red.svg" alt="NoneBot">
  <img src="https://img.shields.io/badge/onebot-2.2.3+-darkgreen.svg" alt="OneBot">
  <img src="https://img.shields.io/badge/version-0.3.0-yellow.svg" alt="Version">
  </a>
</p>

### 已实现功能
- 单插件分群管理
- ~~以B站UID审核入群(粉丝)~~
- 以B站UID审核入群(粉丝团 等级`<=`20)
- 以B站UID审核入群(大航海 等级`>`20)

### 安装方法

```
pip install nonebot_plugin_BiliRequestAll
```

### 说明依赖
```
XX| [可运行依赖版本]                       [测试依赖版本]
01| nonebot2 >= 2.0.0b1                   [2.0.0]
02| nonebot-adapter-onebot >= 2.0.0b1     [2.2.3]
03| requests                              [2.31.0]
```
### 食用方法 (初始化)
- ("[]"中填写`on`/`off` "<>"中填写纯数字，注意顺序，要用"_"隔开)
```
/rqst [主开关]_[日志开关]_<主播UID>_<最低等级要求>
``` 

### 未来计划
- 审批日志
- 强审核模式

### 反馈问题
- 邮箱：anonymous_hax@foxmail.com

<details>
<summary>[日志]展开/收起</summary>

- 2022/10/03 [V0.1.0] 发布此插件
- 2023/01/18 [V0.2.0] 更新插件数据结构，新增大航海入群功能
- 2023/01/19 [V0.2.1] json加载问题 [issues https://github.com/Shadow403/nonebot_plugin_BiliRequestAll/issues/6], 修复粉丝牌审核模块
- 2023/10/01 [v0.3.0] 重写该插件