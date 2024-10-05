<div align="center">

<a href="https://v2.nonebot.dev/store">
  <img src="https://raw.githubusercontent.com/A-kirami/nonebot-plugin-template/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo">
</a>

<p>
  <img src="https://raw.githubusercontent.com/lgc-NB2Dev/readme/main/template/plugin.svg" alt="NoneBotPluginText">
</p>

# nonebot-plugin-BiliRequestAll

_✨ 基于 [NoneBot2](https://github.com/nonebot/nonebot2) & [WebAPI](https://api-dev.shadow403.cn/) 的一个 NoneBot B站自动审批插件 ✨_

<img src="https://img.shields.io/badge/python-3.10+-blue.svg" alt="python">
<a href="./LICENSE">
  <img src="https://img.shields.io/github/license/shadow403/nonebot_plugin_BiliRequestAll.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot_plugin_BiliRequestAll">
  <img src="https://img.shields.io/pypi/v/nonebot_plugin_BiliRequestAll.svg" alt="pypi">
</a>

</div>

## 😎 功能
- 分群管理
- 以B站UID审核入群(粉丝团 等级`<=`20)
- 以B站UID审核入群(大航海 等级`>`20)

## 💿 安装

```
nb plugin install nonebot_plugin_BiliRequestAll
```
```
pip install nonebot_plugin_BiliRequestAll
```

## 🍴 使用

- 设置: `/rqst [主开关]_[强审核]_<主播UID>_<最低等级要求>`
- 查看: `/rqst info`

> [!IMPORTANT]
> ("[]"中填写`on`/`off` "<>"中填写纯数字，注意顺序，要用"_"隔开)
>
> 强审核: 不满足要入群要求会自动拒绝, 如设为 off 会忽略该加群请求 (等待人工审核)

<br>

<details>
<summary> 日志 </summary>

- `V0.1.0` 发布此插件
- `V0.2.0` 更新插件数据结构，新增大航海入群功能
- `V0.2.1` json加载问题 [#6](https://github.com/Shadow403/n_BiliRequestAll/issues/), 修复粉丝牌审核模块
- `v0.2.5` 重写该插件
- `v0.2.6` 更新查看审批信息功能
- `v0.2.7` 更新API模块
- `v0.2.8` 修复不满足入群条件时返回信息不全报错
- `v0.3.0` 重写该插件
- `v0.3.1` 修改插件名
