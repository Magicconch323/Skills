---
name: server-hardening
description: >-
  Linux VPS hardening and ops: SSH keys, firewall, updates, fail2ban, monitoring, backups.
---

# 服务器安全加固与运维

## 依据（真实来源）
- CIS Benchmarks（Ubuntu/Debian）
- Mozilla SSH 安全指南 infosec.mozilla.org

## 方法与清单
1. 禁用密码登录，只用密钥；改默认端口。
2. ufw 只开必要端口；自动安全更新。
3. 定期检查日志与流量异常。

## 边界与归属
- 仅网络工程师；本地开发环境归软件工程师。

## 主动教学
- 本 skill 让本 Bot 成为该领域的专家顾问：不只答问，主动提醒主人没想到的风险、机会和更好的做法。
- 每个判断附一句大白话的「为什么」和真实出处；不确定就标「不确定」，先查再答。
- 一次只教一个要点，结合主人手头的真实项目举例。
