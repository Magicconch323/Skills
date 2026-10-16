---
name: networking-fundamentals
description: >-
  Networking fundamentals: OSI/TCP-IP layers, DNS, TLS, routing, MTU. Use to explain and diagnose VPN issues in plain language.
---

# 网络基础：分层、TCP/IP、DNS、路由

## 依据（真实来源）
- Kurose & Ross《Computer Networking: A Top-Down Approach》
- W. Richard Stevens《TCP/IP Illustrated》

## 方法与清单
1. 故障按层排查：物理 → IP → 传输 → 应用。
2. 工具：ping / tracert / nslookup / curl -v。
3. 先给主人一句话原理，再给命令。

## 边界与归属
- VPN 与网络归本 Bot。

## 主动教学
- 本 skill 让本 Bot 成为该领域的专家顾问：不只答问，主动提醒主人没想到的风险、机会和更好的做法。
- 每个判断附一句大白话的「为什么」和真实出处；不确定就标「不确定」，先查再答。
- 一次只教一个要点，结合主人手头的真实项目举例。

## 网络排障流程（2026-10-16 新增）

原则：先查再答；由物理层向上逐层排查，下一层没确认正常前不跳到上一层；每步把命令和输出原样留作证据；一次只改一个变量，改完立即复测；改任何配置前先备份（备份放 `E:\coding\Project\VPN\` 内，文件名带日期，不出 E:\coding）。

| 步骤 | 查什么 | Windows 命令（PowerShell） | 正常证据 |
|---|---|---|---|
| 1 链路/网卡 | 网卡是否 Up、有无断线 | `Get-NetAdapter`；`netsh wlan show interfaces` | Status=Up，信号/速率正常 |
| 2 IP/网关 | 拿到 IP、网关可达 | `ipconfig /all`；`ping <网关IP>` | 非 169.254.x.x，网关 ping 通 |
| 3 DNS | 域名能否解析、是否被污染 | `Resolve-DnsName example.com`；`nslookup example.com 223.5.5.5`；`ipconfig /flushdns` | 返回合理 IP，不同 DNS 结果一致 |
| 4 路由 | 走哪条路、在哪一跳断 | `tracert -d 8.8.8.8`；`route print`；`Test-NetConnection 8.8.8.8 -TraceRoute` | 能看到断点跳数或全程通 |
| 5 端口/防火墙 | 目标端口通不通、本机是否拦截 | `Test-NetConnection <主机> -Port 443`；`Get-NetFirewallProfile`；`netstat -ano \| findstr <端口>` | TcpTestSucceeded=True，端口被正确进程监听 |
| 6 代理客户端 | 客户端是否运行、系统代理/TUN 是否生效、节点可用 | 查看 v2rayN/Clash 日志；`netsh winhttp show proxy`；`Get-ItemProperty 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings'` | 日志无报错，代理端口在监听，节点延迟正常 |
| 7 应用 | 具体软件/浏览器自身设置 | `curl.exe -v https://example.com`；`curl.exe -x http://127.0.0.1:<端口> -v https://www.google.com` | 返回 200/正常页面 |

回报格式：每一步写「命令 → 关键输出 → 结论」，最后指出故障所在层、改了哪一个变量、备份位置、复测结果。
