<div align="center">

<img src="assets/osint_arsenal_logo.png" width="1200" alt="OSINT Arsenal"/>

<br/>

# 🔍 AWESOME OSINT ARSENAL（OSINT 军火库）

### 终极开源情报 + 安全工具箱

<br/>

[![Tools](https://img.shields.io/badge/Tools-753%2B-FF4444?style=for-the-badge&logo=target&logoColor=white)](https://github.com/rawfilejson/awesome-osint-arsenal)
[![Categories](https://img.shields.io/badge/Categories-50-0066CC?style=for-the-badge&logo=buffer&logoColor=white)](https://github.com/rawfilejson/awesome-osint-arsenal)
[![Version](https://img.shields.io/badge/Version-2.1-00CC66?style=for-the-badge&logoColor=white)](https://github.com/rawfilejson/awesome-osint-arsenal)
[![Updated](https://img.shields.io/badge/Updated-2026--05--10-FF8800?style=for-the-badge&logoColor=white)](https://github.com/rawfilejson/awesome-osint-arsenal)
[![Stars](https://img.shields.io/github/stars/rawfilejson/awesome-osint-arsenal?style=for-the-badge&color=gold&logo=github)](https://github.com/rawfilejson/awesome-osint-arsenal/stargazers)

<br/>

> **753+ tools · 50 categories · Multi-distro installers · Georgian OSINT · Termux support**
>
> *互联网上最全的 OSINT 与安全工具箱——每个工具都带安装说明或经过验证的链接。*

<a href="https://www.buymeacoffee.com/rawfilejson" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me a Coffee" style="height: 60px !important;width: 217px !important;" ></a>

<br/>

### ⚡ 一条命令装齐全部

```bash
git clone https://github.com/rawfilejson/awesome-osint-arsenal && cd awesome-osint-arsenal && sudo bash install.sh
```

### 🎯 或者按需挑选

```bash
sudo bash osint.sh        # 🔍 OSINT only (Sherlock, Maigret, Amass, …)
```

```bash
sudo bash redteam.sh      # ⚔️  Red team (Sliver, BloodHound, Mimikatz, Nuclei, …)
```

```bash
sudo bash blueteam.sh     # 🛡️  Blue team (Wazuh, Sigma, Suricata, Velociraptor, …)
```

```bash
sudo bash forensics.sh    # 🔬 DFIR + RE (Volatility, Ghidra, radare2, …)
```

```bash
sudo bash hardware.sh     # 🔌 Hardware + SDR (binwalk, hackrf, openocd, …)
```

```bash
sudo bash labs.sh         # 🎓 Vulnerable apps for practice (DVWA, Juice Shop, …)
```

```bash
bash termux.sh            # 📱 Android (Termux subset, no sudo needed)
```

> Works on **Kali, Debian, Ubuntu, Parrot, Mint, Pop!_OS** (best — `apt`)
> 部分支持 **Arch / Manjaro / Fedora / RHEL**（自动识别，回退到 git/pip/go 安装）
> **Android** 上可用 Termux 子集

<br/>

</div>

---

> [!IMPORTANT]
> ## 🙏 Fork 之前说两句
>
> 本仓库有 **50 个分类、753 个工具**。链接、安装命令、每周的新工具都要跟进，对一个人来说是*很大的量*。
>
> **没人搭手的话，这份清单迟早会过时。** 这是实话。
>
> **30 秒就能帮上忙的方式：**
> - ⭐ **给仓库点 Star**（星越多，越多人看到并参与贡献）
> - 🐛 **发现死链？** 提个 issue，一分钟的事
> - 🧩 **想添加工具？** 先过一眼 [CONTRIBUTING.md](CONTRIBUTING.md)，免得 PR 被关
> - ☕ [**请作者喝杯咖啡**](https://www.buymeacoffee.com/rawfilejson) 让周末维护能持续下去
> - 📢 **转发分享**——推特、Discord，安全圈出没的地方都行
>
> 发现问题：**别光抱怨——提 issue 或 PR，这份清单才能一直有用。**

---

> [!WARNING]
> **免责声明：** 本仓库仅用于**教育与授权的安全研究**。
> 测试非本人所有的系统前，务必取得书面授权。
> 作者对本文所列工具或技术的任何滥用**不承担责任**。
> 完整版见页底[法律免责声明](#%EF%B8%8F-legal-disclaimer)。


---

## 📋 目录

<details>
<summary><b>🔭 侦察与发现</b>——点开展开</summary>

1. [用户名与社交媒体 OSINT](#1-username--social-media-osint)
2. [邮箱 OSINT 工具](#2-email-osint-tools)
3. [电话号码 OSINT](#3-phone-number-osint)
4. [Domain & IP OSINT](#4-domain--ip-osint)
5. [地理定位与地图 OSINT](#5-geolocation--maps-osint)
6. [图像与视频 OSINT](#6-image--video-osint)
7. [人脸识别与人物搜索](#7-facial-recognition--people-search)
8. [社交媒体监控](#8-social-media-monitoring)

</details>

<details>
<summary><b>💥 数据泄露</b>——点开展开</summary>

9. [数据泄露与拖库搜索引擎](#9-data-breach--leak-search-engines)
10. [WikiLeaks、DDoSecrets 与爆料平台](#10-wikileaks-ddosecrets--whistleblower-platforms)
11. [密码破解与凭据工具](#11-password-cracking--credential-tools)

</details>

<details>
<summary><b>🕶️ 暗网与隐私</b>——点开展开</summary>

12. [暗网搜索引擎与工具](#12-dark-web-search-engines--tools)
13. [匿名化与隐私工具](#13-anonymous--privacy-tools)

</details>

<details>
<summary><b>⚔️ 攻击安全</b>（仅限授权测试）——点开展开</summary>

14. [Web 应用 OSINT 与扫描](#14-web-application-osint--scanning)
15. [社会工程与钓鱼](#15-social-engineering--phishing)
16. [漏洞扫描与利用](#16-vulnerability-scanning--exploitation)
17. [网络与无线工具](#17-network--wireless-tools)
18. [移动黑客与手机利用](#18-mobile-hacking--phone-exploitation)

</details>

<details>
<summary><b>🧠 情报与分析</b>——点开展开</summary>

19. [AI 驱动的 OSINT 与免费 AI 工具](#19-ai-powered-osint--free-ai-tools)
20. [金融与企业情报](#20-financial--corporate-intelligence)
21. [车辆、房产与公共记录](#21-vehicle-property--public-records)
22. [元数据与数字取证](#22-metadata--digital-forensics)

</details>

<details>
<summary><b>👁️ 监控与 Dork</b>——点开展开</summary>

23. [网络摄像头与 IP Camera OSINT](#23-ip-camera--webcam-osint)
24. [Google Dork 圣经](#24-google-dorking-bible)
25. [凭据与数据 Dork](#25-credential--data-dorking)
26. [IP 追踪与地理定位链接](#26-ip-tracking--geolocation-links)

</details>

<details>
<summary><b>🌐 社区与平台</b>——点开展开</summary>

27. [Telegram OSINT 机器人与频道](#27-telegram-osint-bots--channels)
28. [俄罗斯 OSINT 与人物查询服务](#28-russian-osint--person-lookup-services)
29. [社交媒体搜索平台](#29-social-media-searcher-platforms)

</details>

<details>
<summary><b>🧰 工具箱与框架</b>——点开展开</summary>

30. [Termux 黑客工具箱（完整版）](#30-termux-hacking-toolkit-complete)
31. [Kali Linux OSINT 工具包](#31-kali-linux-osint-toolkit)
32. [一体化黑客框架](#32-all-in-one-hacking-frameworks)
33. [字典生成与暴力破解](#33-wordlist-generation--brute-force)

</details>

<details>
<summary><b>🖥️ 硬件与操作系统</b>——点开展开</summary>

34. [硬件黑客工具](#34-hardware-hacking-tools)
35. [OSINT 操作系统](#35-osint-operating-systems)

</details>

<details>
<summary><b>👨‍💻 开发者与学习</b>——点开展开</summary>

36. [OSINT API 与开发者工具](#36-osint-apis--developer-tools)
37. [OSINT 浏览器扩展](#37-browser-extensions-for-osint)
38. [OSINT 学习资源](#38-osint-learning-resources)
39. [Awesome OSINT GitHub 仓库](#39-awesome-osint-github-repos)

</details>

<details>
<summary><b>⚡ 速查表</b>——点开展开</summary>

40. [一键安装脚本](#40-one-click-install-scripts)
41. [必备工具 Top 50（速查）](#41-top-50-must-have-tools-quick-reference)

</details>


<details>
<summary><b>⚔️ 红队与蓝队</b>——点开展开</summary>

42. [红队与攻击安全](#42--red-team--offensive-security)
43. [蓝队与防御安全](#43--blue-team--defensive-security)
44. [威胁情报平台](#44--threat-intel-platforms)

</details>

<details>
<summary><b>🔬 取证、硬件与训练</b>——点开展开</summary>

45. [数字取证与逆向工程](#45--digital-forensics--reverse-engineering)
46. [训练、靶场与 CTF](#46--training-labs--ctf)
47. [漏洞赏金平台](#47--bug-bounty-platforms)

</details>

<details>
<summary><b>📚 知识与精选补充</b>——点开展开</summary>

48. [学习资源](#48--learning-resources)
49. [补充工具（精选新增）](#49--extra-tools-curated-additions)

</details>

<details>
<summary><b>🇬🇪 国家专属 OSINT</b>——点开展开</summary>

50. [格鲁吉亚 OSINT 军火库（500+ 资源）](#50--georgian-osint-arsenal-500-resources)

</details>

---

## ⚙️ 安装指南

### 快速安装——Kali / Debian / Ubuntu / Parrot

```bash
git clone https://github.com/rawfilejson/awesome-osint-arsenal
```

```bash
cd awesome-osint-arsenal
```

```bash
sudo bash install.sh
```

### 选择单一技术栈

| 脚本 | 安装内容 | 适用场景 |
|---|---|---|
| `osint.sh` | OSINT 工具（Sherlock、Maigret、Amass、theHarvester 等） | 只做侦察/调查时选它 |
| `redteam.sh` | Sliver、BloodHound、Impacket、NetExec、Mimikatz、Nuclei 等 | 授权渗透测试 / 红队 |
| `blueteam.sh` | Wazuh、Sigma、Suricata、Velociraptor、Atomic Red Team、MITRE CALDERA | SOC / 检测工程 |
| `forensics.sh` | Volatility 3、Ghidra、radare2、Plaso、CyberChef 等 | DFIR / 恶意软件分析 |
| `hardware.sh` | binwalk、hackrf、openocd、GNU Radio、gqrx 等 | 射频 / IoT / 固件研究 |
| `labs.sh` | DVWA、Juice Shop、WebGoat（Docker） | 本地练习靶场 |
| `termux.sh` | Android 兼容子集 | 手机端侦察 |

### 其他 Linux 发行版

安装器会自动识别你的包管理器：

| Distro | Manager | Status |
|---|---|---|
| Kali / Debian / Ubuntu / Parrot / Mint / Pop!_OS | `apt` | ✅ 最佳——首选平台 |
| Arch / Manjaro / EndeavourOS | `pacman` | 🟡 部分支持（仅 apt 的工具自动跳过） |
| Fedora / RHEL / Rocky / Alma | `dnf` | 🟡 部分支持（仅 apt 的工具自动跳过） |
| Termux (Android) | `pkg` | ✅ 仅子集——用 `bash termux.sh` |
| macOS / Windows | — | ❌ 请用 Kali 虚机或 WSL2 |

### 各安装器都做了什么

- 自动识别发行版并选用正确的包管理器
- 已装过的自动跳过（幂等，可放心重跑）
- Color output: 🟢 installed · 🟡 skipped · 🔴 failed
- Logs failures to `~/osint-install-errors.log`
- 结束时打印安装摘要
- git 克隆的工具装到 `/opt/osint-arsenal/`（Termux 下为 `$HOME/osint-arsenal/`）

### 安装后——把工具加入 PATH

```bash
echo 'export PATH="$PATH:/opt/osint-arsenal"' >> ~/.bashrc
```

```bash
source ~/.bashrc
```

经 `apt`/`pip`/`go install` 安装的工具已在 `$PATH` 中。


---
## 📊 数据速览

<div align="center">

| 🛠️ Total Tools | 💻 命令行工具 | 📁 GitHub Repos | 🌐 Online Platforms | 🤖 AI Tools |
|:-:|:-:|:-:|:-:|:-:|
| **753+** | **167+** | **117+** | **461+** | **25+** |

| 🕶️ Dark Web | 🇬🇪 格鲁吉亚 OSINT | 💥 Breach Engines | ⚔️ Red Team | 🛡️ Blue Team |
|:-:|:-:|:-:|:-:|:-:|
| **15+** | **500+** | **39+** | **35+** | **24+** |

| 🔬 Forensics | 🔌 硬件 | 🎓 Training | 🎯 Bug Bounty | 📂 Total Categories |
|:-:|:-:|:-:|:-:|:-:|
| **16+** | **16+** | **21+** | **12+** | **50** |

<a href="https://www.buymeacoffee.com/rawfilejson" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me a Coffee" style="height: 60px !important;width: 217px !important;" ></a>

</div>


---
## 1. 用户名与社交媒体 OSINT

> 🎯 在数百个平台查找账号、档案与数字足迹。
>
> **实用建议：** 先用 Sherlock 快扫一遍，再用 Maigret 做深挖——它覆盖 3000+ 网站。

| 工具 | 说明 | 安装 / 链接 |
|------|-------------|----------------|
| **Sherlock** | 在 400+ 社交网络查用户名 | `pip install sherlock-project` |
| **Maigret** | Sherlock 高级分支——3000+ 网站 | `pip install maigret` |
| **Namechk** | 用户名与域名可用性检查 | [namechk.com](https://namechk.com/) |
| **WhatsMyName** | 网页版用户名枚举 | [whatsmyname.app](https://whatsmyname.app/) |
| **Snoop** | 用户名搜索（侧重俄语平台） | `pip install snoop` |
| **UserRecon** | Bash 编写的用户名查找器 | `git clone https://github.com/wishihab/userrecon.git` |
| **Blackbird** | 快速用户名搜索工具 | `pip install blackbird-osint` |
| **Social Analyzer** | 基于 API 的社交媒体画像工具 | `pip install social-analyzer` |
| **NExfil** | 按用户名找档案 | `pip install nexfil` |
| **Socid-extractor** | 从网页提取信息 | `pip install socid-extractor` |
| **Gitrecon** | GitHub OSINT 侦察 | `pip install gitrecon` |
| **OSRFramework** | 用户名研究框架 | `pip install osrframework` |
| **Holehe** | 查邮箱是否注册过 120+ 网站 | `pip install holehe` |
| **socialscan** | 查邮箱/用户名是否已注册 | `pip install socialscan` |
| **Investigo** | 用户名检查器（Go 编写） | `go install github.com/tdh8316/investigo@latest` |
| **OSINT Framework** | OSINT 工具可视化地图 | [osintframework.com](https://osintframework.com/) |
| **CheckUserNames** | 跨多平台查用户名 | [checkusernames.com](https://checkusernames.com/) |
| **KnowEm** | 500+ 网站用户名搜索 | [knowem.com](https://knowem.com/) |
| **Instant Username Search** | 实时用户名检查器 | [instantusername.com](https://instantusername.com/) |
| **Usersearch.org** | 免费社交网络搜索 | [usersearch.org](https://usersearch.org/) |
| **Lullar** | 按邮箱、用户名或姓名在 175+ 网站免费找人 | [com.lullar.com](https://com.lullar.com/) |

<details>
<summary><b>💻 Sherlock——安装与用法</b></summary>

```bash
# Kali Linux / Ubuntu
pip install sherlock-project
sherlock "username"

# 从 GitHub 源码装（永远最新）
git clone https://github.com/sherlock-project/sherlock.git
cd sherlock
pip install -r requirements.txt
python3 sherlock "username"

# 一次搜多个用户名
sherlock user1 user2 user3
```
</details>

<details>
<summary><b>💻 Maigret——安装与用法</b></summary>

```bash
pip install maigret
maigret "username"

# 从源码安装
git clone https://github.com/soxoj/maigret.git
cd maigret
pip install -r requirements.txt
python3 -m maigret "username"

# 生成 HTML 报告
maigret "username" --html
```
</details>

---

## 2. 邮箱 OSINT 工具

> 📧 Verify emails, find linked accounts, check breach exposure, and analyze headers.
>
> **实用建议：** Holehe 免费且快。配好 API key 后，h8mail 做泄露关联最强。

| 工具 | 说明 | 安装 / 链接 |
|------|-------------|----------------|
| **h8mail** | 邮箱 OSINT 与泄露追踪 | `pip install h8mail` |
| **Holehe** | 在 120+ 网站查邮箱 | `pip install holehe` |
| **theHarvester** | 邮箱与域名收集器 | `pip install theHarvester` |
| **EmailAnalyzer** | 分析可疑的 .eml 邮件文件 | `git clone https://github.com/keraattin/EmailAnalyzer` |
| **Prowl** | 邮箱与域名侦察 | `git clone https://github.com/nettitude/Prowl` |
| **EmailHeader-Analyzer** | 命令行邮件头解析 + OSINT | `git clone https://github.com/Giritharram/EmailHeader-Analyzer-CLI-Python` |
| **MailHeaderDetective** | 邮件头取证 | `git clone https://github.com/akajhon/MailHeaderDetective` |
| **WhatMail** | 邮件头分析命令行工具 | `git clone https://github.com/z0m31en7/WhatMail` |
| **mailto_analyzer** | 邮箱暴露分析 | `pip install mailto-analyzer` |
| **Infoga** | 邮箱 OSINT 信息收集 | `git clone https://github.com/m4ll0k/Infoga` |
| **Hunter.io** | 查找职业邮箱 | [hunter.io](https://hunter.io/) |
| **Phonebook.cz** | 邮箱、域名与 URL 搜索 | [phonebook.cz](https://phonebook.cz/) |
| **EmailRep** | 邮箱信誉查询 | [emailrep.io](https://emailrep.io/) |
| **Epieos** | 获取邮箱关联信息 | [epieos.com](https://epieos.com/) |
| **GetNotify** | 邮件打开追踪 + 地理定位 | [getnotify.com](https://getnotify.com/) |
| **Snov.io** | 邮箱查找与验证 | [snov.io](https://snov.io/) |
| **MXToolbox** | 邮件头分析与 DNS 检查 | [mxtoolbox.com](https://mxtoolbox.com/) |
| **SimpleLogin** | OSINT 用的邮箱别名服务 | [simplelogin.io](https://simplelogin.io/) |
| **Email-Checker** | 邮箱验证工具 | [email-checker.net](https://email-checker.net/) |
| **Voila Norbert** | 查找任何人的邮箱 | [voilanorbert.com](https://voilanorbert.com/) |

<details>
<summary><b>💻 h8mail——安装与用法</b></summary>

```bash
pip install h8mail

# 基本扫描
h8mail -t "target@email.com"

# 带 API key（解锁更多泄露源）
# 用 HIBP、BreachDirectory 等的 API key 创建 config.ini
h8mail -t "target@email.com" -k config.ini

# Scan a list of emails
h8mail -t emails.txt
```
</details>

---

## 3. 电话号码 OSINT

> 📱 从手机号识别运营商、归属地、注册情况与关联账号。
>
> **实用建议：** PhoneInfoga 是命令行工具的金标准。GetContact 能看别人把你的号码备注成什么。

| 工具 | 说明 | 安装 / 链接 |
|------|-------------|----------------|
| **PhoneInfoga** | 高级电话号码扫描器 | `pip install phoneinfoga` |
| **Ignorant** | 查手机号在各网站的注册情况 | `pip install ignorant` |
| **GetContact** | 看别人把你的号码备注成什么 | [getcontact.com](https://getcontact.com/) |
| **NumVerify** | 手机号有效性验证 API | [numverify.com](https://numverify.com/) |
| **Truecaller** | 来电识别与骚扰号码查询 | [truecaller.com](https://truecaller.com/) |
| **Sync.me** | 电话号码查询 | [sync.me](https://sync.me/) |
| **CallerIDTest** | 反向电话查询 | [calleridtest.com](https://calleridtest.com/) |
| **SpyDialer** | 免费反向电话查询 | [spydialer.com](https://spydialer.com/) |
| **National Cellular Directory** | 机主信息查询 | [nationalcellulardirectory.com](https://www.nationalcellulardirectory.com/) |
| **TelPoisk** | 俄罗斯电话簿 | [telpoisk.com](https://telpoisk.com/) |
| **NumLookup** | 免费反向电话查询 | [numlookup.com](https://www.numlookup.com/) |
| **Hlr-Lookups** | HLR 手机号查询 | [hlr-lookups.com](https://www.hlr-lookups.com/) |
| **PhoneSploit** | 基于 ADB 的手机利用 | `git clone https://github.com/aerosol-can/PhoneSploit` |

<details>
<summary><b>💻 PhoneInfoga——安装与用法</b></summary>

```bash
# 二进制安装（Kali Linux）
curl -sSL https://raw.githubusercontent.com/sundowndev/phoneinfoga/master/support/scripts/install | bash

# 在 localhost:8080 打开 Web 界面
phoneinfoga serve -p 8080

# 命令行扫描
phoneinfoga scan -n "+1234567890"

# pip 安装（备选）
pip install phoneinfoga
```
</details>

---

## 4. Domain & IP OSINT

> 🌐 枚举子域名、查 DNS 记录、发现 IP 段、测绘攻击面。
>
> **实用建议：** amass + subfinder 一起跑可获最大子域名覆盖，再管道给 httpx 检查哪些主机存活。

| 工具 | 说明 | 安装 / 链接 |
|------|-------------|----------------|
| **Amass** | 深度 DNS 枚举 | `go install github.com/owasp-amass/amass/v4/...@master` |
| **Subfinder** | 快速被动子域名发现 | `go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest` |
| **dnsrecon** | DNS 枚举 | `pip install dnsrecon` |
| **Sublist3r** | 子域名枚举 | `pip install sublist3r` |
| **crt.sh** | 证书透明度查询 | [crt.sh](https://crt.sh/) |
| **Shodan** | 联网设备搜索 | [shodan.io](https://shodan.io/) |
| **Censys** | 全网扫描结果搜索 | [censys.io](https://censys.io/) |
| **Criminal IP** | AI 驱动的网络威胁情报 | [criminalip.io](https://www.criminalip.io/) |
| **VirusTotal** | 域名/IP/文件分析 | [virustotal.com](https://virustotal.com/) |
| **SecurityTrails** | DNS 与域名情报 | [securitytrails.com](https://securitytrails.com/) |
| **IPGeoLocation** | IP 地址地理定位 | `git clone https://github.com/maldevel/IPGeoLocation` |
| **Nmap** | 网络扫描与拓扑绘制 | `apt install nmap` |
| **Masscan** | 最快的互联网端口扫描器 | `apt install masscan` |
| **WHOIS.com** | WHOIS 域名查询 | [whois.com](https://www.whois.com/) |
| **ViewDNS** | 多个 DNS 工具 | [viewdns.info](https://viewdns.info/) |
| **DNSDumpster** | DNS 侦察与测绘 | [dnsdumpster.com](https://dnsdumpster.com/) |
| **Robtex** | DNS 查询可视化 | [robtex.com](https://robtex.com/) |
| **ARIN WHOIS** | IP 注册信息数据库 | [whois.arin.net](https://whois.arin.net/) |
| **BGP Toolkit** | BGP/ASN/IP 情报 | [bgp.he.net](https://bgp.he.net/) |
| **urlscan.io** | URL/域名分析与截图 | [urlscan.io](https://urlscan.io/) |
| **AbuseIPDB** | IP 地址信誉数据库 | [abuseipdb.com](https://www.abuseipdb.com/) |
| **Web-Check** | 一站式网站分析 | [web-check.xyz](https://web-check.xyz/) |
| **IPinfo** | IP 地址数据与地理定位 | [ipinfo.io](https://ipinfo.io/) |
| **DB-IP** | IP 地理定位数据库 | [db-ip.com](https://db-ip.com/) |

<details>
<summary><b>💻 Amass + Subfinder + HTTPx——最有效的侦察组合</b></summary>

```bash
# 第 1 步：被动枚举子域名（快）
subfinder -d example.com -o subs.txt

# 第 2 步：主动深度枚举（慢但更全）
amass enum -d example.com -o amass_subs.txt

# 第 3 步：合并去重
cat subs.txt amass_subs.txt | sort -u > all_subs.txt

# 第 4 步：检查哪些子域名存活
cat all_subs.txt | httpx -status-code -title -o live_subs.txt

# 第 5 步：给所有存活主机截图
cat live_subs.txt | eyewitness --web -d screenshots/
```
</details>

---

## 5. 地理定位与地图 OSINT

> 🗺️ 图像定位、卫星数据分析、照片地点核验。
>
> **实用建议：** SunCalc（影子分析）+ ShadowMap + Mapillary 组合可做精确图像定位。

| 工具 | 说明 | 链接 |
|------|-------------|------|
| **Google Earth Pro** | 高级卫星影像 | [earth.google.com](https://earth.google.com/) |
| **Overpass Turbo** | OpenStreetMap 数据查询 | [overpass-turbo.eu](https://overpass-turbo.eu/) |
| **SunCalc** | 从照片计算太阳位置与时间 | [suncalc.org](https://suncalc.org/) |
| **GeoGuessr** | 地理定位训练游戏 | [geoguessr.com](https://geoguessr.com/) |
| **Sentinel Hub** | 卫星影像访问 | [sentinel-hub.com](https://sentinel-hub.com/) |
| **FIRMS** | NASA 火点/热异常数据 | [firms.modaps.eosdis.nasa.gov](https://firms.modaps.eosdis.nasa.gov/) |
| **Wikimapia** | 协作世界地图 | [wikimapia.org](https://wikimapia.org/) |
| **OpenStreetMap** | 免费世界地图 | [openstreetmap.org](https://openstreetmap.org/) |
| **GeoSpy** | AI 驱动的图像地理定位 | [geospy.ai](https://geospy.ai/) |
| **Mapillary** | 街景影像 | [mapillary.com](https://mapillary.com/) |
| **Maxar** | 商业卫星影像 | [maxar.com](https://maxar.com/) |
| **F4map** | 3D 交互世界地图 | [demo.f4map.com](https://demo.f4map.com/) |
| **Zoom Earth** | 实时卫星与天气 | [zoom.earth](https://zoom.earth/) |
| **KartaView** | 街景影像（OpenStreetCam） | [kartaview.org](https://kartaview.org/) |
| **ShadowMap** | 影子分析推算拍摄时间 | [shadowmap.org](https://shadowmap.org/) |
| **Crime Brasil** | 巴西犯罪与事故开放数据，按街区（RS 州到街区级；MG/RJ 市级；联邦公路事故） | [crimebrasil.com.br](https://crimebrasil.com.br) |

---

## 6. 图像与视频 OSINT

> 🖼️ Extract metadata, reverse search images, verify authenticity, and detect AI-generated content.
>
> **实用建议：** 找人脸和地点时，Yandex 反向图搜始终比 Google 好用。

| 工具 | 说明 | 安装 / 链接 |
|------|-------------|----------------|
| **TinEye** | 反向图搜 | [tineye.com](https://tineye.com/) |
| **Google Reverse Image** | Google 图片搜索 | [images.google.com](https://images.google.com/) |
| **Yandex Images** | 人脸/地点最佳反向图搜 | [yandex.com/images](https://yandex.com/images) |
| **ExifTool** | 图片/文档元数据提取 | `apt install libimage-exiftool-perl` |
| **FOCA** | 从文档提取元数据 | [github.com/ElevenPaths/FOCA](https://github.com/ElevenPaths/FOCA) |
| **InVID** | 视频验证工具包 | [invid-project.eu](https://www.invid-project.eu/) |
| **FotoForensics** | 图像取证分析（ELA 误差水平分析） | [fotoforensics.com](https://fotoforensics.com/) |
| **Fake Image Detector** | 基于 AI 的虚假图像检测 | [fakeimagedetector.com](https://www.fakeimagedetector.com/) |
| **Search by Image** | 多引擎反向图搜（浏览器扩展） | Chrome / Firefox 扩展 |
| **Depix** | 从截图中恢复打码文字 | `git clone https://github.com/beurtschipper/Depix` |
| **Forensically** | 在线图像取证套件 | [29a.ch/photo-forensics](https://29a.ch/photo-forensics) |
| **AI or Not** | 检测 AI 生成图像 | [aiornot.com](https://aiornot.com/) |
| **Hive Moderation** | AI 内容检测 | [hivemoderation.com](https://hivemoderation.com/) |
| **Illuminarty** | AI 图像检测 | [illuminarty.ai](https://illuminarty.ai/) |

<details>
<summary><b>💻 ExifTool——安装与用法</b></summary>

```bash
# Install
apt-get install libimage-exiftool-perl

# 读取基本元数据
exiftool image.jpg

# 专门提取 GPS 坐标
exiftool -GPSLatitude -GPSLongitude image.jpg

# 清除全部元数据（保护隐私）
exiftool -all= image.jpg

# 显示全部元数据分组
exiftool -a -u -g1 image.jpg

# 批量处理整个文件夹
exiftool /path/to/images/
```
</details>

---

## 7. 人脸识别与人物搜索

> 👤 用照片、姓名或用户名在网上找人。
>
> ⚠️ **警告：** 人脸识别涉及严重的隐私与法律问题，仅在明确授权下使用。

| 工具 | 说明 | 安装 / 链接 |
|------|-------------|----------------|
| **FaceSeek** | AI 驱动的人脸反向搜索 | [faceseek.online](https://faceseek.online/) |
| **FaceCheck.ID** | 人脸识别搜索引擎 | [facecheck.id](https://facecheck.id/) |
| **PimEyes** | 以图搜人的搜索引擎 | [pimeyes.com](https://pimeyes.com/) |
| **Search4faces** | VK/OK 社交网络人脸搜索 | [search4faces.com](https://search4faces.com/) |
| **face_recognition** | Python 人脸识别库 | `pip install face_recognition` |
| **DeepFace** | AI 人脸分析（年龄、性别、情绪） | `pip install deepface` |
| **ThatsThem** | 免费人物搜索 | [thatsthem.com](https://thatsthem.com/) |
| **Pipl** | 深度人物搜索引擎 | [pipl.com](https://pipl.com/) |
| **BeenVerified** | 人物搜索与背景调查 | [beenverified.com](https://beenverified.com/) |
| **Spokeo** | 人物搜索聚合器 | [spokeo.com](https://spokeo.com/) |
| **FastPeopleSearch** | 免费人物查找 | [fastpeoplesearch.com](https://fastpeoplesearch.com/) |
| **WebMii** | 人物搜索引擎 | [webmii.com](https://webmii.com/) |
| **OSINT Industries** | 人物搜索 + 社交媒体查询 | [osint.industries](https://www.osint.industries/) |
| **IDCrawl** | 免费人物搜索引擎 | [idcrawl.com](https://www.idcrawl.com/) |

---

## 8. 社交媒体监控

> 📡 监控、爬取并调查社交媒体账号与社区。
>
> **实用建议：** Osintgram（Instagram）+ Telepathy（Telegram）+ snscrape（Twitter/X）组合可覆盖全部主流平台。

| 工具 | 说明 | 安装 / 链接 |
|------|-------------|----------------|
| **Osintgram** | Instagram OSINT 工具 | `git clone https://github.com/Datalux/Osintgram` |
| **Instaloader** | Instagram 数据下载器 | `pip install instaloader` |
| **insta-dl** | 异步 Instagram 下载器，HikerAPI 后端，可选 aiograpi | `pip install instagram-dl` |
| **insto** | 交互式 Instagram OSINT 命令行，带 REPL、快照、差异对比与 Maltego 导出 | `pip install insto` |
| **Twint** | Twitter OSINT（无需 API） | `pip install twint` |
| **snscrape** | 社交媒体爬虫（Twitter、Reddit 等） | `pip install snscrape` |
| **Toutatis** | 通过手机/邮箱做 Instagram OSINT | `pip install toutatis` |
| **TikTok Scraper** | TikTok 数据提取 | `npm install -g tiktok-scraper` |
| **Reddit Investigator** | Reddit 用户分析 | [reddit-user-analyser.netlify.app](https://reddit-user-analyser.netlify.app/) |
| **socialscan** | 社交媒体存在性检查 | `pip install socialscan` |
| **Telepathy** | Telegram OSINT 分析 | `pip install telepathy` |
| **Twayback** | 查找已删除推文 | `pip install twayback` |
| **Xquik** | X/Twitter 数据 API 与 MCP 技能 | [github.com](https://github.com/Xquik-dev/x-twitter-scraper) |
| **SocialBlade** | 社交媒体分析 | [socialblade.com](https://socialblade.com/) |
| **Social-Searcher** | 免费社交媒体搜索引擎 | [social-searcher.com](https://www.social-searcher.com/) |
| **Mention** | 社交媒体监控 | [mention.com](https://mention.com/) |
| **BrandWatch** | 社媒舆情平台 | [brandwatch.com](https://www.brandwatch.com/) |

---

## 9. 数据泄露与拖库搜索引擎

> 💥 检查凭据、邮箱、手机号是否已在数据泄露中暴露。
>
> **实用建议：** HIBP 免费且安全。DeHashed 和 LeakCheck 的付费档数据量最大。

| 工具 | 说明 | 类型 | 链接 |
|------|-------------|:----:|------|
| **Have I Been Pwned** | 查邮箱/手机号是否在泄露库中 | 🟢 Free | [haveibeenpwned.com](https://haveibeenpwned.com/) |
| **DeHashed** | 泄露数据搜索引擎 | 💰 Paid | [dehashed.com](https://dehashed.com/) |
| **LeakCheck** | 邮箱/用户名/手机号泄露查询 | 🟡 Freemium | [leakcheck.net](https://leakcheck.net/) |
| **Intelligence X** | 搜索泄露库、暗网与拖库数据 | 💰 Paid | [intelx.io](https://intelx.io/) |
| **BreachDirectory** | 免费泄露查询 | 🟢 Free | [breachdirectory.org](https://breachdirectory.org/) |
| **LeakPeek** | 搜索泄露数据库 | 🟡 Freemium | [leakpeek.com](https://leakpeek.com/) |
| **Snusbase** | 泄露数据搜索引擎 | 💰 Paid | [snusbase.com](https://snusbase.com/) |
| **CheckLeaked** | 泄露搜索引擎（150 亿+ 账号） | 🟡 Freemium | [checkleaked.cc](https://checkleaked.cc/) |
| **DataBreach.com** | 数据泄露查询 | 🟢 Free | [databreach.com](https://databreach.com/) |
| **Hudson Rock Cavalier** | 信息窃取木马情报与泄露数据 | 🟡 Freemium | [hudsonrock.com](https://www.hudsonrock.com/free-report) |
| **h8mail** | 泄露狩猎自动化命令行 | 🟢 Free | `pip install h8mail` |
| **XposedOrNot** | 泄露暴露查询 | 🟢 Free | [xposedornot.com](https://xposedornot.com/) |
| **ScatteredSecrets** | 泄露通知服务 | 🟡 Freemium | [scatteredsecrets.com](https://scatteredsecrets.com/) |
| **The OSINT Rack** | 勒索软件与数据泄露监控 | 🟢 Free | [osintrack.com](https://osintrack.com/) |
| **Pwndb** | 暗网泄露数据库（Tor） | 🟢 Free | Requires Tor Browser |
| **OsintCat** | 邮箱/用户名/手机号泄露查询——真实数据、出结果快 | 🟡 Freemium | [osintcat.net](https://www.osintcat.net/) |

<details>
<summary><b>💻 Pwndb——暗网泄露查询（需 Tor）</b></summary>

```bash
# 先启动 Tor 服务
sudo systemctl start tor

# 克隆 pwndb
git clone https://github.com/coj337/pwndb.git
cd pwndb

# 安装依赖
pip install -r requirements.txt

# Search by email
python3 pwndb.py --target email@example.com

# .onion 地址（用 Tor 浏览器打开）
# pwndb2am33lno4bq.onion
```
</details>

---

## 10. WikiLeaks、DDoSecrets 与爆料平台

> 📁 泄露的政府、企业与机密文档档案。

| Platform | 说明 | 链接 |
|----------|-------------|------|
| **WikiLeaks** | 泄露的政府与企业文档 | [wikileaks.org](https://wikileaks.org/) |
| **DDoSecrets** | Distributed Denial of Secrets（分布式拒绝秘密） | [ddosecrets.com](https://ddosecrets.com/) |
| **Cryptome** | 1996 年以来的文档档案 | [cryptome.org](https://cryptome.org/) |
| **The Intercept** | 调查报道 | [theintercept.com](https://theintercept.com/) |
| **SecureDrop** | 爆料人提交系统 | [securedrop.org](https://securedrop.org/) |
| **ICIJ Offshore Leaks** | 巴拿马文件、潘多拉文件 | [offshoreleaks.icij.org](https://offshoreleaks.icij.org/) |
| **DocumentCloud** | 公开文档研究 | [documentcloud.org](https://documentcloud.org/) |
| **Wayback Machine** | 网页存档 | [web.archive.org](https://web.archive.org/) |
| **FBI Vault** | FBI 电子阅览室 | [vault.fbi.gov](https://vault.fbi.gov/) |
| **CIA Reading Room** | CIA 解密文档 | [cia.gov/readingroom](https://www.cia.gov/readingroom) |
| **NSA Declassified** | NSA 解密档案 | [nsa.gov](https://nsa.gov/) |
| **PACER** | 美国联邦法院记录 | [pacer.uscourts.gov](https://pacer.uscourts.gov/) |

---

## 11. 密码破解与凭据工具

> 🔑 用于自有系统授权密码审计与凭据恢复的工具。

| 工具 | 说明 | 安装 / 链接 |
|------|-------------|----------------|
| **Hashcat** | 高级密码恢复（GPU 加速） | `apt install hashcat` |
| **John the Ripper** | 经典密码破解工具 | `apt install john` |
| **Hydra** | 网络登录爆破工具 | `apt install hydra` |
| **Medusa** | 并行爆破工具 | `apt install medusa` |
| **CeWL** | 从网站生成自定义字典 | `apt install cewl` |
| **Crunch** | 基于模式的字典生成器 | `apt install crunch` |
| **RainbowCrack** | 彩虹表破解工具 | [project-rainbowcrack.com](https://project-rainbowcrack.com/) |
| **Ophcrack** | Windows 密码破解（彩虹表） | [ophcrack.sourceforge.io](https://ophcrack.sourceforge.io/) |
| **LaZagne** | 凭据恢复工具（后渗透） | `git clone https://github.com/AlessandroZ/LaZagne` |
| **Mimikatz** | Windows 凭据抓取器 | `git clone https://github.com/gentilkiwi/mimikatz` |
| **Responder** | LLMNR/NBT-NS/MDNS 毒化工具 | `git clone https://github.com/lgandx/Responder` |

<details>
<summary><b>💻 Hashcat——速查</b></summary>

```bash
# Install
apt install hashcat

# 用字典破解 MD5 哈希
hashcat -m 0 hash.txt /usr/share/wordlists/rockyou.txt

# 带规则破解 SHA-256
hashcat -m 1400 hash.txt wordlist.txt -r rules/best64.rule

# 常见哈希类型：
# -m 0    = MD5
# -m 100  = SHA-1
# -m 1400 = SHA-256
# -m 1800 = SHA-512crypt (Linux)
# -m 1000 = NTLM (Windows)
# -m 2500 = WPA/WPA2 (Wi-Fi)
```
</details>

---

## 12. 暗网搜索引擎与工具

> 🕶️ Search .onion sites, darknet markets, and hidden services.
>
> **前置条件：** Tor 浏览器，或运行在 9050 端口的 Tor 服务。

| 工具 | 说明 | 链接 / 洋葱地址 |
|------|-------------|----------------------|
| **Torch** | 最老牌、最大的暗网搜索引擎 | `xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion` |
| **Haystak** | 支持过滤的暗网搜索 | `haystak5njsmn2hqkewecpaxetahtwhsbsa64jom2k22z5afxhnpxfid.onion` |
| **Ahmia** | 明网暗网搜索 | [ahmia.fi](https://ahmia.fi/) |
| **DuckDuckGo Onion** | Tor 上的私密搜索 | `duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion` |
| **Phobos** | 暗网搜索引擎 | `phobosxilamwcg75xt22id7aywkzol6q6rfl2flipcqoc4e4ahima5id.onion` |
| **DarkSearch** | 暗网搜索 API（明网） | [darksearch.io](https://darksearch.io/) |
| **OnionScan** | 扫描与分析 .onion 站点 | `go install github.com/s-rah/onionscan@latest` |
| **Dark.fail** | 已验证暗网链接目录 | [dark.fail](https://dark.fail/) |
| **OSINT-SPY** | 支持 Tor 的 OSINT 工具 | `git clone https://github.com/SharadKumar97/OSINT-SPY` |

<details>
<summary><b>💻 为暗网工具配置 Tor</b></summary>

```bash
# 安装 Tor
sudo apt install tor proxychains4

# 启动 Tor 服务
sudo systemctl start tor
sudo systemctl enable tor

# 测试 Tor 是否可用
curl --socks5 127.0.0.1:9050 https://check.torproject.org/api/ip

# 任意工具配 proxychains 使用
proxychains4 nmap -sT target.onion
proxychains4 curl http://example.onion

# Edit /etc/proxychains4.conf if needed
# 确认包含这一行：socks5 127.0.0.1 9050
```
</details>

---

## 13. 匿名化与隐私工具

> 🔒 在 OSINT 调查中保持匿名、保护身份。
>
> **实用建议：** 需要完全匿名的调查用 Tails 系统——磁盘上不留任何痕迹。

| 工具 | 说明 | 安装 / 链接 |
|------|-------------|----------------|
| **Tor Browser** | 匿名网页浏览 | [torproject.org](https://torproject.org/) |
| **Tails OS** | 无痕 Live 系统（不留痕迹） | [tails.boum.org](https://tails.boum.org/) |
| **Whonix** | 基于 Tor 的匿名系统（虚拟机） | [whonix.org](https://whonix.org/) |
| **ProtonVPN** | 免费加密 VPN | [protonvpn.com](https://protonvpn.com/) |
| **ProtonMail** | 加密邮箱 | [proton.me](https://proton.me/) |
| **Signal** | 加密即时通讯 | [signal.org](https://signal.org/) |
| **OnionShare** | 通过 Tor 的匿名文件分享 | [onionshare.org](https://onionshare.org/) |
| **Anonsurf** | 匿名化整个系统流量 | `git clone https://github.com/Und3rf10w/kali-anonsurf` |
| **MAC Changer** | 修改/伪造 MAC 地址 | `apt install macchanger` |
| **BleachBit** | 数字足迹清理 | [bleachbit.org](https://bleachbit.org/) |
| **VeraCrypt** | 磁盘加密 | [veracrypt.fr](https://veracrypt.fr/) |
| **KeePassXC** | 离线密码管理器 | [keepassxc.org](https://keepassxc.org/) |
| **Mullvad VPN** | 隐私 VPN（无需邮箱） | [mullvad.net](https://mullvad.net/) |
| **Anon-SMS** | 匿名短信发送 | `git clone https://github.com/HACK3RY2J/Anon-SMS.git` |

---

## 14. Web 应用 OSINT 与扫描

> 🕸️ 识别网站技术栈、发现隐藏目录、爬取接口端点。
>
> **实用建议：** 先 Whatweb 识别技术栈，再 Nikto 快扫漏洞，最后 Nuclei 深度扫描。

| 工具 | 说明 | 安装 / 链接 |
|------|-------------|----------------|
| **Nikto** | Web 服务器漏洞扫描器 | `apt install nikto` |
| **WPScan** | WordPress 漏洞扫描器 | `gem install wpscan` |
| **Wappalyzer** | 网站技术栈识别（浏览器扩展） | Browser Extension |
| **Whatweb** | 网站技术栈识别 | `apt install whatweb` |
| **Dirb** | Web 目录爆破工具 | `apt install dirb` |
| **Gobuster** | URI/DNS 爆破工具（Go） | `go install github.com/OJ/gobuster/v3@latest` |
| **Feroxbuster** | 快速递归内容发现 | `apt install feroxbuster` |
| **HTTPx** | 快速 HTTP 工具包/探测 | `go install github.com/projectdiscovery/httpx/cmd/httpx@latest` |
| **Katana** | 网页爬虫 | `go install github.com/projectdiscovery/katana/cmd/katana@latest` |
| **LinkFinder** | 从 JavaScript 发现接口端点 | `git clone https://github.com/GerbenJavado/LinkFinder` |
| **Photon** | OSINT 数据爬虫 | `git clone https://github.com/s0md3v/Photon` |
| **Wfuzz** | Web 模糊测试工具 | `pip install wfuzz` |
| **ParamSpider** | 从网页存档发现参数 | `pip install paramspider` |
| **WebHack** | Web 黑客工具包 | `git clone https://github.com/yan4ikyt/webhack` |

---

## 15. 社会工程与钓鱼

> 🎭 用于授权红队项目的钓鱼演练框架。
>
> ⚠️ **仅限授权渗透测试与安全意识培训。**

| 工具 | 说明 | 安装 / 链接 |
|------|-------------|----------------|
| **SET (Social Engineering Toolkit)** | 完整社会工程框架 | `apt install set` |
| **Gophish** | 企业钓鱼演练平台 | [getgophish.com](https://getgophish.com/) |
| **Zphisher** | 30+ 钓鱼模板 | `git clone https://github.com/htr-tech/zphisher` |
| **NexPhisher** | 多平台钓鱼工具 | `git clone https://github.com/htr-tech/nexphisher` |
| **Storm-Breaker** | 访问摄像头/麦克风/位置（社会工程） | `git clone https://github.com/ultrasecurity/Storm-Breaker` |
| **Evilginx2** | 中间人反向代理 | `go install github.com/kgretzky/evilginx2@latest` |
| **Modlishka** | 反向代理钓鱼框架 | `go install github.com/drk1wi/Modlishka@latest` |
| **King Phisher** | 钓鱼活动工具包 | [github.com/rsmusllp/king-phisher](https://github.com/rsmusllp/king-phisher) |
| **SocialFish** | 社交媒体钓鱼 | `git clone https://github.com/UndeadSec/SocialFish` |
| **AdvPhishing** | 高级钓鱼工具 | `git clone https://github.com/Ignitetch/AdvPhishing` |
| **URLCADIZ** | URL 掩蔽工具 | `git clone https://github.com/PerezMascato/URLCADIZ` |

<details>
<summary><b>💻 Zphisher——安装与用法</b></summary>

```bash
git clone https://github.com/htr-tech/zphisher.git
cd zphisher
chmod +x zphisher.sh
bash zphisher.sh

# 从菜单选模板（Facebook、Google、Instagram 等）
# 工具通过 Cloudflare/Serveo 隧道生成钓鱼 URL
# 捕获的凭据保存在本地
```
</details>

---

## 16. 漏洞扫描与利用

> 💣 在授权目标上发现并验证漏洞的框架。
>
> ⚠️ **运行这些工具前务必持有书面授权。**

| 工具 | 说明 | 安装 / 链接 |
|------|-------------|----------------|
| **Metasploit** | 行业标准渗透测试框架 | `apt install metasploit-framework` |
| **Nuclei** | 基于模板的快速漏洞扫描器 | `go install github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest` |
| **SQLMap** | SQL 注入自动化工具 | `apt install sqlmap` |
| **Burp Suite** | Web 应用安全测试代理 | [portswigger.net/burp](https://portswigger.net/burp) |
| **OWASP ZAP** | 开源 Web 应用扫描器 | [zaproxy.org](https://zaproxy.org/) |
| **OpenVAS** | 开源漏洞扫描器 | `apt install openvas` |
| **Commix** | 命令注入利用工具 | `git clone https://github.com/commixproject/commix` |
| **GoldenEye** | HTTP DoS 工具（授权压测用） | `git clone https://github.com/jseidl/GoldenEye` |
| **ExploitDB** | 漏洞利用数据库（searchsploit） | [exploit-db.com](https://www.exploit-db.com/) |
| **Criminal IP** | 漏洞与 CVE 搜索 | [criminalip.io](https://www.criminalip.io/) |

---

## 17. 网络与无线工具

> 📶 分析流量、审计 Wi-Fi 网络，在授权目标上做中间人测试。

| 工具 | 说明 | 安装 / 链接 |
|------|-------------|----------------|
| **Wireshark** | 网络协议分析器 | `apt install wireshark` |
| **Aircrack-ng** | Wi-Fi 安全审计套件 | `apt install aircrack-ng` |
| **Kismet** | 无线网络探测与嗅探 | `apt install kismet` |
| **Bettercap** | 中间人框架（ARP、DNS、HTTP） | `apt install bettercap` |
| **Ettercap** | 中间人攻击套件 | `apt install ettercap-common` |
| **Wifite** | Wi-Fi 自动化审计工具 | `apt install wifite` |
| **Reaver** | WPS 爆破工具 | `apt install reaver` |
| **Fern Wifi Cracker** | 图形界面 Wi-Fi 审计工具 | `apt install fern-wifi-cracker` |
| **Fluxion** | Wi-Fi 社会工程（邪恶双子） | `git clone https://github.com/FluxionNetwork/fluxion` |
| **hcxtools** | Wi-Fi 抓包格式转换 | `apt install hcxtools` |
| **Netcat** | TCP/IP 瑞士军刀 | `apt install netcat-openbsd` |
| **tcpdump** | 命令行抓包分析器 | `apt install tcpdump` |

---

## 18. 移动黑客与手机利用

> 📲 面向授权评估的 Android/iOS 安全测试。

| 工具 | 说明 | 安装 / 链接 |
|------|-------------|----------------|
| **PhoneSploit** | 基于 ADB 的手机利用 | `git clone https://github.com/aerosol-can/PhoneSploit` |
| **AhMyth Android RAT** | Android 远程访问工具 | `git clone https://github.com/AhMyth/AhMyth-Android-RAT` |
| **Apktool** | Android APK 反编译/重打包 | `apt install apktool` |
| **jadx** | Android APK 反编译器（图形界面） | `apt install jadx` |
| **Frida** | 动态插桩工具包 | `pip install frida-tools` |
| **Objection** | 运行时移动应用探查 | `pip install objection` |
| **MobSF** | 移动安全框架（静态 + 动态） | [github.com/MobSF/Mobile-Security-Framework-MobSF](https://github.com/MobSF/Mobile-Security-Framework-MobSF) |
| **MSFPC** | MSF 载荷生成器 | `git clone https://github.com/g0tmi1k/msfpc` |

---

## 19. AI 驱动的 OSINT 与免费 AI 工具

> 🤖 用于自动化研究、图像分析与加速调查的 AI 工具。
>
> **实用建议：** Perplexity AI 很适合 OSINT 研究——它引用来源，一切可验证。

### AI 驱动的 OSINT 工具

| 工具 | 说明 | 安装 / 链接 |
|------|-------------|----------------|
| **GeoSpy** | 从图像做 AI 地理定位 | [geospy.ai](https://geospy.ai/) |
| **DeepFace** | 人脸分析（年龄、性别、情绪） | `pip install deepface` |
| **face_recognition** | Python 人脸识别库 | `pip install face_recognition` |
| **OpenCV** | 计算机视觉库 | `pip install opencv-python` |
| **ReconAIzer** | AI 增强的 Burp Suite 扩展 | [github.com/hisxo/ReconAIzer](https://github.com/hisxo/ReconAIzer) |
| **AI or Not** | 检测 AI 生成内容 | [aiornot.com](https://aiornot.com/) |
| **HARPA AI** | 面向 OSINT 的 AI 浏览器代理 | [harpa.ai](https://harpa.ai/) |

### OSINT 研究免费 AI 工具

| 工具 | 说明 | 免费档 | 链接 |
|------|-------------|:---------:|------|
| **Claude** | 最擅长推理与分析 | ✅ 有免费档 | [claude.ai](https://claude.ai/) |
| **ChatGPT** | OpenAI 的 AI 助手 | ✅ GPT-4o mini | [chat.openai.com](https://chat.openai.com/) |
| **Perplexity AI** | 带来源引用的 AI 搜索 | ✅ 每天 5 次 Pro | [perplexity.ai](https://perplexity.ai/) |
| **Google Gemini** | 带网页搜索的 Google AI | ✅ Free | [gemini.google.com](https://gemini.google.com/) |
| **DeepSeek** | 开源、推理能力强 | ✅ Free | [chat.deepseek.com](https://chat.deepseek.com/) |
| **Grok** | 实时 X/Twitter 数据 | ✅ X 上免费 | [x.com/grok](https://x.com/grok) |
| **Microsoft Copilot** | 集成 Bing 搜索的 AI | ✅ Free | [copilot.microsoft.com](https://copilot.microsoft.com/) |
| **NotebookLM** | Google 的文档分析 AI | ✅ Free | [notebooklm.google.com](https://notebooklm.google.com/) |
| **Phind** | 面向开发者的 AI 搜索 | ✅ Free | [phind.com](https://www.phind.com/) |
| **HuggingChat** | 开源 AI 对话 | ✅ Free | [huggingface.co/chat](https://huggingface.co/chat/) |

---

## 20. 金融与企业情报

> 💰 调查公司、追踪加密货币、挖掘金融关联关系。

| 工具 | 说明 | 链接 |
|------|-------------|------|
| **OpenCorporates** | 全球公司数据库 | [opencorporates.com](https://opencorporates.com/) |
| **ICIJ Offshore Leaks** | 巴拿马/潘多拉/天堂文件 | [offshoreleaks.icij.org](https://offshoreleaks.icij.org/) |
| **SEC EDGAR** | 美国公司档案 | [sec.gov/edgar](https://sec.gov/edgar) |
| **Companies House (UK)** | 英国公司注册查询 | [beta.companieshouse.gov.uk](https://beta.companieshouse.gov.uk/) |
| **Aleph (OCCRP)** | 全球公司公共记录 | [aleph.occrp.org](https://aleph.occrp.org/) |
| **Orbit** | 比特币地址调查工具 | `git clone https://github.com/s0md3v/Orbit` |
| **Blockchain.com** | 比特币浏览器 | [blockchain.com/explorer](https://blockchain.com/explorer) |
| **Etherscan** | 以太坊区块链浏览器 | [etherscan.io](https://etherscan.io/) |
| **BinCheck** | 银行卡 BIN 查询 | [bincheck.io](https://bincheck.io/) |
| **Crunchbase** | 公司/创业企业数据库 | [crunchbase.com](https://crunchbase.com/) |
| **LEI Search** | 法人实体识别码（LEI）查询 | [search.gleif.org](https://search.gleif.org/) |

---

## 21. 车辆、房产与公共记录

> 🚗 Access public records, vehicle history, property data, and court documents.

| Tool/Service | 说明 | 链接 |
|-------------|-------------|------|
| **FAXVIN** | 免费 VIN 解码 | [faxvin.com](https://faxvin.com/) |
| **AutoCheck** | 车辆历史报告 | [autocheck.com](https://autocheck.com/) |
| **NICB VINCheck** | 盗抢车辆查询 | [nicb.org/vincheck](https://www.nicb.org/vincheck) |
| **PACER** | 美国联邦法院记录 | [pacer.uscourts.gov](https://pacer.uscourts.gov/) |
| **Zillow** | 房产记录与估价 | [zillow.com](https://zillow.com/) |
| **Who Owns What** | 纽约市房东资产查询 | [whoownswhat.justfix.org](https://whoownswhat.justfix.org/en/) |
| **FOIA.gov** | 信息自由法案（FOIA）申请门户 | [foia.gov](https://foia.gov/) |
| **Court Listener** | 免费美国法院判例检索 | [courtlistener.com](https://courtlistener.com/) |

---

## 22. 元数据与数字取证

> 🔬 提取隐藏数据、恢复被删文件、分析数字证据。
>
> **实用建议：** CyberChef 必须收藏——编码、加密、数据处理全在浏览器里完成。

| 工具 | 说明 | 安装 / 链接 |
|------|-------------|----------------|
| **Autopsy** | 全功能数字取证平台 | [autopsy.com](https://autopsy.com/) |
| **Volatility** | 内存取证框架 | `pip install volatility3` |
| **Wireshark** | 网络数据包分析 | `apt install wireshark` |
| **Binwalk** | 固件分析与提取 | `apt install binwalk` |
| **Foremost** | 文件雕复（恢复被删文件） | `apt install foremost` |
| **Bulk Extractor** | 从磁盘镜像提取特征 | `apt install bulk-extractor` |
| **ExifTool** | 完整元数据提取 | `apt install libimage-exiftool-perl` |
| **Metagoofil** | 文档元数据收集器 | `pip install metagoofil` |
| **CyberChef** | 数据分析瑞士军刀 | [gchq.github.io/CyberChef](https://gchq.github.io/CyberChef) |
| **Scalpel** | 文件雕复工具 | `apt install scalpel` |

---

## 23. 网络摄像头与 IP Camera OSINT

> ⚠️ **警告：** 未经授权访问摄像头**在任何地方都违法**。本节仅用于教育认知——理解暴露设备如何被发现，以便**保护它们**。

### 发现暴露摄像头的 Shodan 检索

| 搜索式 | 能查到什么 |
|-------------|---------------|
| `screenshot.label:webcam` | Shodan 收录的摄像头 |
| `port:554 has_screenshot:true` | 带截图的 RTSP 摄像头 |
| `Server: yawcam` | Yawcam 摄像头 |
| `webcamXP` | WebcamXP 服务器 |
| `port:8080 title:"Blue Iris"` | Blue Iris 视频监控 |
| `port:37777 "DVR"` | 大华 DVR 录像系统 |
| `port:80 title:"DVR"` | 可 Web 访问的 DVR |

### 发现摄像头的 Google Dork

| Google Dork | Target |
|------------|--------|
| `inurl:"viewerframe?mode="` | Axis 网络摄像头 |
| `intitle:"webcamXP 5"` | WebcamXP 5 服务器 |
| `inurl:"videostream.cgi"` | CGI 视频流 |
| `intitle:"Live View / - AXIS"` | AXIS 摄像头 |
| `inurl:/view/view.shtml` | Mobotix 摄像头 |

---

## 24. Google Dork 圣经

> 🔍 用于发现不易检索信息的高级搜索运算符。
>
> **实用建议：** 组合多个运算符可获最高精度。务必在无痕/隐私窗口测试。

### 核心运算符

| Operator | 说明 | Example |
|----------|-------------|---------|
| `site:` | 在域名内搜索 | `site:example.com admin` |
| `inurl:` | 搜 URL 路径 | `inurl:admin login` |
| `intitle:` | 搜页面标题 | `intitle:"index of" passwords` |
| `intext:` | 搜页面正文 | `intext:"username" "password"` |
| `filetype:` | 按文件类型搜索 | `filetype:pdf "confidential"` |
| `ext:` | 按扩展名搜索 | `ext:sql "dump"` |
| `cache:` | 查看 Google 缓存版本 | `cache:example.com` |
| `allintext:` | 全部词出现在正文中 | `allintext:username password email` |

### 高价值 OSINT Dork

| Purpose | Google Dork |
|---------|-------------|
| **Exposed passwords** | `intitle:"index of" "passwords.txt"` |
| **SQL database dumps** | `filetype:sql "CREATE TABLE" "INSERT INTO"` |
| **Config files** | `ext:conf OR ext:cnf "password"` |
| **Exposed .env files** | `intitle:"index of" ".env"` |
| **Open FTP servers** | `intitle:"index of" inurl:ftp` |
| **Exposed git repos** | `intitle:"index of" ".git"` |
| **SSH private keys** | `filetype:pem "PRIVATE KEY"` |
| **phpinfo pages** | `ext:php intitle:phpinfo` |
| **Exposed log files** | `filetype:log "password" OR "username"` |

### Dork 生成工具

| 工具 | 链接 |
|------|------|
| **DorkSearch** | [dorksearch.com](https://dorksearch.com/) |
| **Google Hacking DB (GHDB)** | [exploit-db.com/google-hacking-database](https://exploit-db.com/google-hacking-database) |
| **Pagodo** | `git clone https://github.com/opsdisk/pagodo` |
| **GooFuzz** | `git clone https://github.com/m3n0sd0n4ld/GooFuzz` |

---

## 25. 凭据与数据 Dork

> 🗄️ 用于发现网上无意暴露敏感数据的高级 Dork。

| Purpose | Google Dork |
|---------|-------------|
| **Gmail in spreadsheets** | `allintext:"@gmail.com" "password" filetype:xlsx` |
| **Exposed credentials in CSV** | `filetype:csv "email" "password"` |
| **Pastebin credential dumps** | `filetype:txt "username" "password" site:pastebin.com` |
| **Database dumps** | `filetype:sql "INSERT INTO" "password" "email"` |
| **Config files with API keys** | `filetype:env "DB_PASSWORD" OR "API_KEY" OR "SECRET"` |
| **Exposed .htpasswd** | `filetype:htpasswd htpasswd` |
| **phpMyAdmin without auth** | `inurl:phpmyadmin/index.php intitle:"phpMyAdmin"` |
| **Exposed Jenkins** | `intitle:"Dashboard [Jenkins]" inurl:"/login"` |
| **AWS keys exposed** | `filetype:pem "AKIA" OR "ASIA"` |
| **GitHub secrets** | `site:github.com "API_KEY" OR "api_secret" filetype:env` |

---

## 26. IP 追踪与地理定位链接

> 📍 通过构造链接追踪 IP 的工具。
>
> ⚠️ **仅限授权使用**——例如追踪自己的邮件营销活动，或授权的钓鱼演练。

| 工具 | 说明 | 链接 |
|------|-------------|------|
| **Grabify** | IP 抓取与短链接服务 | [grabify.link](https://grabify.link/) |
| **IPLogger** | 带 IP 记录的短链接服务 | [iplogger.org](https://iplogger.org/) |
| **Canary Tokens** | 追踪令牌（URL、邮件、DNS、文件） | [canarytokens.org](https://canarytokens.org/) |
| **GetNotify** | 邮件打开追踪 + 地理定位 | [getnotify.com](https://getnotify.com/) |
| **IPinfo** | IP 地址数据 API | [ipinfo.io](https://ipinfo.io/) |
| **IP-API** | IP 地理定位 API | [ip-api.com](http://ip-api.com/) |
| **MaxMind GeoIP** | IP 地理定位数据库 | [maxmind.com](https://maxmind.com/) |

> 💡 **小技巧：** 用 VK 跳转链接掩蔽记录器 URL：
> `https://vk.com/away.php?to=YOUR_LOGGER_URL`

---

## 27. Telegram OSINT 机器人与频道

> 💬 Telegram-based OSINT tools, bots, and intelligence communities.

### OSINT 机器人

| Bot | 说明 | Handle |
|-----|-------------|--------|
| **Eye of God (Glaz Boga)** | 按电话/邮箱/照片/VK 查人 | @glazzz_rus_bot |
| **@No_BlackMail_bot** | 按手机号搜邮箱 | @No_BlackMail_bot |
| **@OverSerchBot** | 多平台搜索 OSINT 机器人 | @OverSerchBot |
| **GetContact Bot** | 电话号码来电识别 | @getcontact_real_bot |
| **Quick OSINT** | 快速人物查询 | @Quick_OSINT_bot |
| **@CreationDateBot** | 查 Telegram 账号注册时间 | @creationdatebot |
| **@SangMataBot** | 查 Telegram 账号用户名历史 | @SangMataInfo_bot |

### OSINT 频道

| Channel | Content | 链接 |
|---------|---------|------|
| **@overbafer1** | 黑客与网络安全 | [t.me/overbafer1](https://t.me/overbafer1) |
| **@Social_engineering** | 社会工程技术 | [t.me/Social_engineering](https://t.me/Social_engineering) |
| **@cyberbezopasno** | 网络安全新闻与工具 | [t.me/cyberbezopasno](https://t.me/cyberbezopasno) |
| **@OSINT_group** | OSINT 社区 | [t.me/OSINT_group](https://t.me/OSINT_group) |

### Telegram 爬取工具

| 工具 | 说明 | Install |
|------|-------------|---------|
| **Telepathy** | Telegram OSINT 分析 | `pip install telepathy` |
| **Telethon** | Python Telegram API 库 | `pip install telethon` |
| **TeleGram-OSINTer** | Telegram 档案调查 | `git clone https://github.com/Alb-310/TeleGram-OSINTer` |

---

## 28. 俄罗斯 OSINT 与人物查询服务

> 🇷🇺 俄语 OSINT 社区广泛使用的服务。

| # | Service | 说明 | 链接 |
|:-:|---------|-------------|------|
| 1 | **FNS (Tax Service)** | 取 INN 税号、查欠税 | [service.nalog.ru](https://service.nalog.ru/) |
| 2 | **TelPoisk** | 电话簿——按姓名查地址 | [telpoisk.com](https://telpoisk.com/) |
| 3 | **GetContact** | 看别人把你的号码备注成什么 | [getcontact.com](https://getcontact.com/) |
| 4 | **Eye of God** | 按电话/邮箱/照片查人 | @glazzz_rus_bot |
| 5 | **Search4faces** | VK 与 OK 人脸搜索 | [search4faces.com](https://search4faces.com/) |
| 6 | **GetNotify** | 邮件追踪 + 地理定位 | [getnotify.com](https://getnotify.com/) |
| 7 | **BinCheck** | 银行卡 BIN 查询（银行、地区） | [bincheck.io](https://bincheck.io/) |

### VK (VKontakte) OSINT

| Purpose | Tool/URL |
|---------|----------|
| **Registration data** | [regvk.com](https://regvk.com/) |
| **FOAF data** | `https://vk.com/foaf.php?id=USER_ID` |
| **VK page archive** | [vk.watch/ID/profile](https://vk.watch/ID/profile) |
| **Activity tracking** | [nebaz.ru](https://nebaz.ru/) |
| **VK tools** | [220vk.com](https://220vk.com/) |

---

## 29. 社交媒体搜索平台

| 工具 | 说明 | Free? | 链接 |
|------|-------------|:-----:|------|
| **Social Searcher** | 实时社交媒体搜索 | ✅ Yes | [social-searcher.com](https://www.social-searcher.com/) |
| **Social Mention** | 社交媒体聚合器 | ✅ Yes | [socialmention.com](http://socialmention.com/) |
| **Google Alerts** | 免费网页监控 | ✅ Free | [google.com/alerts](https://www.google.com/alerts) |
| **Who Posted What** | Facebook 关键词搜索 | ✅ Free | [whopostedwhat.com](https://whopostedwhat.com/) |
| **Mention** | 社交媒体与网页监控 | 🟡 Freemium | [mention.com](https://mention.com/) |
| **Talkwalker** | 社媒舆情倾听与分析 | 💰 Paid | [talkwalker.com](https://www.talkwalker.com/) |
| **BrandWatch** | 社会情报平台 | 💰 Paid | [brandwatch.com](https://www.brandwatch.com/) |
| **Hootsuite** | 社交媒体管理 | 🟡 Freemium | [hootsuite.com](https://www.hootsuite.com/) |

---

## 30. Termux 黑客工具箱（完整版）

> 📱 通过 Termux 在 Android 上部署完整 OSINT 与安全工具箱。

### 初始配置

```bash
# Termux 首次配置
pkg update -y && pkg upgrade -y
pkg install python python2 git wget curl nmap
pip install requests colorama
termux-setup-storage
```

### 工具清单

| # | 工具 | Purpose | Install |
|:-:|------|---------|---------| 
| 1 | **Sherlock** | Username OSINT | `pip install sherlock-project` |
| 2 | **Maigret** | 用户名 OSINT（3000+ 网站） | `pip install maigret` |
| 3 | **h8mail** | 邮箱泄露狩猎 | `pip install h8mail` |
| 4 | **Zphisher** | 钓鱼（30+ 模板） | `git clone https://github.com/htr-tech/zphisher` |
| 5 | **NexPhisher** | 高级钓鱼 | `git clone https://github.com/htr-tech/nexphisher` |
| 6 | **Storm-Breaker** | Camera/Mic/Location SE | `git clone https://github.com/ultrasecurity/Storm-Breaker` |
| 7 | **UserRecon** | 用户名搜索 | `git clone https://github.com/wishihab/userrecon` |
| 8 | **IPGeoLocation** | IP 地理定位 | `git clone https://github.com/maldevel/IPGeoLocation` |
| 9 | **Orbit** | 比特币地址搜索 | `git clone https://github.com/s0md3v/Orbit` |
| 10 | **Nmap** | 网络扫描器 | `pkg install nmap` |
| 11 | **Hydra** | 登录爆破 | `pkg install hydra` |
| 12 | **PhoneSploit** | 通过 ADB 利用手机 | `git clone https://github.com/aerosol-can/PhoneSploit` |
| 13 | **fsociety** | 一体化黑客工具包 | `git clone https://github.com/Manisso/fsociety` |

<details>
<summary><b>💻 Termux 一键安装</b></summary>

```bash
pkg update -y && pkg upgrade -y && \
pkg install -y python git wget curl nmap hydra perl openssh php clang make openssl && \
pip install requests colorama sherlock-project maigret holehe h8mail && \
cd ~ && \
git clone https://github.com/htr-tech/zphisher && \
git clone https://github.com/Manisso/fsociety && \
git clone https://github.com/ultrasecurity/Storm-Breaker && \
git clone https://github.com/wishihab/userrecon && \
echo "Done! All tools installed."
```
</details>

---

## 31. Kali Linux OSINT 工具包

> 🐉 Kali 预装工具，外加推荐补充。

### Pre-installed on Kali

| 工具 | Category | Command |
|------|----------|---------|
| **Nmap** | 网络扫描 | `nmap` |
| **Wireshark** | 数据包分析 | `wireshark` |
| **Metasploit** | Exploitation | `msfconsole` |
| **SQLMap** | SQL 注入 | `sqlmap` |
| **Hydra** | 暴力破解 | `hydra` |
| **John the Ripper** | 密码破解 | `john` |
| **Hashcat** | GPU 密码破解 | `hashcat` |
| **Aircrack-ng** | Wi-Fi 破解 | `aircrack-ng` |
| **Nikto** | Web 扫描器 | `nikto` |
| **Dirb** | 目录暴力破解 | `dirb` |
| **WPScan** | WordPress 扫描器 | `wpscan` |
| **theHarvester** | 邮箱/子域名 OSINT | `theHarvester` |
| **Maltego** | 可视化关联分析 | `maltego` |
| **Recon-ng** | Web 侦察框架 | `recon-ng` |
| **SET** | 社会工程工具包 | `setoolkit` |
| **Burp Suite** | 网页代理 | `burpsuite` |

### Kali 快速配置（附加工具）

```bash
# 用本仓库安装器（推荐——一次装齐）
sudo bash install.sh

# 或手动添加特定工具：
sudo apt update && sudo apt install -y \
  amass subfinder httpx nuclei gobuster feroxbuster \
  spiderfoot eyewitness phoneinfoga metagoofil

pip install maigret holehe h8mail socialscan social-analyzer \
  deepface face_recognition volatility3 telepathy
```

---

## 32. 一体化黑客框架

> 🧰 把数十个工具收进一个屋檐下的综合框架。

| Framework | 说明 | Install |
|-----------|-------------|---------|
| **fsociety** | 《黑客军团》风格的黑客工具包 | `git clone https://github.com/Manisso/fsociety` |
| **Hackingtool** | 一体化工具（100+ 分类） | `git clone https://github.com/Z4nzu/hackingtool` |
| **SpiderFoot** | OSINT 自动化平台 | `pip install spiderfoot` |
| **Maltego** | 可视化 OSINT 与关联分析 | Kali 预装 |
| **Recon-ng** | 模块化侦察框架 | `pip install recon-ng` |
| **Lazy Script** | 自动化渗透测试助手 | `git clone https://github.com/arismelachroinos/lscript` |
| **osmedeus** | 全自动侦察工作流 | `git clone https://github.com/j3ssie/osmedeus` |

---

## 33. 字典生成与暴力破解

> 📖 自建字典，或用久经考验的现成合集。
>
> **实用建议：** CeWL 很适合定向攻击——从目标自己的网站生成字典。

| 工具 | 说明 | Install |
|------|-------------|---------|
| **Crunch** | 基于模式的字典生成器 | `apt install crunch` |
| **CeWL** | 从任意网站生成自定义字典 | `apt install cewl` |
| **Cupp** | 基于目标画像的字典生成器 | `git clone https://github.com/Mebus/cupp` |
| **SecLists** | 终极安全字典合集 | `git clone https://github.com/danielmiessler/SecLists` |
| **RockYou** | 经典泄露密码列表 | Kali 预装（`/usr/share/wordlists/`） |
| **Weakpass** | 大型字典合集 | [weakpass.com](https://weakpass.com/) |

<details>
<summary><b>💻 字典速查</b></summary>

```bash
# 用 RockYou（Kali 自带）
/usr/share/wordlists/rockyou.txt.gz
gunzip /usr/share/wordlists/rockyou.txt.gz

# 用 Crunch 按模式生成字典
# 格式：crunch <最短> <最长> <字符集>
crunch 8 10 abcdefghijklmnopqrstuvwxyz0123456789 -o wordlist.txt

# 从目标网站生成自定义字典
cewl https://example.com -m 6 -w cewl_wordlist.txt

# 基于画像的字典（调研目标信息）
python3 cupp.py -i
```
</details>

---

## 34. 硬件黑客工具

> 🔧 用于授权渗透测试与硬件安全研究的物理设备。

| Device | 说明 | Price |
|--------|-------------|:-----:|
| **Flipper Zero** | 多功能工具：RFID、NFC、红外、Sub-GHz、BadUSB | ~$170 |
| **HackRF One** | 软件无线电（1MHz–6GHz） | ~$300 |
| **Proxmark3** | RFID/NFC 研究与克隆工具 | ~$60–300 |
| **WiFi Pineapple** | Wi-Fi 审计与恶意 AP 平台 | ~$100–300 |
| **USB Rubber Ducky** | USB 键击注入设备 | ~$80 |
| **Bash Bunny** | 多功能 USB 攻击平台 | ~$120 |
| **LAN Turtle** | 隐蔽网络接入与中间人攻击 | ~$60 |
| **RTL-SDR** | 入门价软件无线电（SDR）接收棒 | ~$25 |
| **Alfa AWUS036ACH** | 远距离双频 Wi-Fi 网卡 | ~$50 |
| **O.MG Cable** | 内置植入芯片的 USB 线 | ~$120 |

---

## 35. OSINT 操作系统

> 🖥️ 为安全研究、OSINT 与隐私打造的专业操作系统。

| OS | Focus | 链接 |
|----|-------|------|
| **Kali Linux** | 渗透测试（600+ 工具） | [kali.org](https://kali.org/) |
| **Parrot OS** | 安全与隐私 | [parrotsec.org](https://parrotsec.org/) |
| **Tails** | 隐私与匿名（无痕） | [tails.boum.org](https://tails.boum.org/) |
| **Whonix** | 基于 Tor 的匿名系统 | [whonix.org](https://whonix.org/) |
| **CSI Linux** | 专注 OSINT 与取证 | [csilinux.com](https://csilinux.com/) |
| **Trace Labs OSINT VM** | OSINT 专用虚机 | [tracelabs.org](https://tracelabs.org/) |
| **BlackArch** | 2800+ 安全工具 | [blackarch.org](https://blackarch.org/) |
| **SIFT Workstation** | SANS 数字取证 | [digital-forensics.sans.org](https://digital-forensics.sans.org/) |
| **REMnux** | 恶意软件分析 | [remnux.org](https://remnux.org/) |
| **Qubes OS** | 通过隔离分区保安全 | [qubes-os.org](https://qubes-os.org/) |
| **CommandoVM** | Windows 渗透虚机 | [github.com/mandiant/commando-vm](https://github.com/mandiant/commando-vm) |

---

## 36. OSINT API 与开发者工具

> 🔌 面向自研工具的 OSINT 数据源编程接口。

| API | 说明 | 链接 |
|-----|-------------|------|
| **Shodan API** | IoT/设备搜索 | [developer.shodan.io](https://developer.shodan.io/) |
| **VirusTotal API** | 文件/URL 分析 | [developers.virustotal.com](https://developers.virustotal.com/) |
| **Hunter.io API** | 邮箱发现 | [hunter.io/api](https://hunter.io/api) |
| **Have I Been Pwned API** | 泄露检查 | [haveibeenpwned.com/API](https://haveibeenpwned.com/API) |
| **IPinfo API** | IP 地理定位 | [ipinfo.io/developers](https://ipinfo.io/developers) |
| **Censys API** | 互联网扫描 | [search.censys.io/api](https://search.censys.io/api) |
| **GitHub API** | 仓库/用户数据 | [api.github.com](https://api.github.com/) |
| **Dehashed API** | 泄露数据查询 | [dehashed.com/docs](https://dehashed.com/docs) |
| **urlscan.io API** | URL 分析 | [urlscan.io/docs/api](https://urlscan.io/docs/api/) |
| **AbuseIPDB API** | IP 信誉 | [abuseipdb.com/api](https://www.abuseipdb.com/api) |
| **Google Custom Search API** | 可编程搜索 | [developers.google.com/custom-search](https://developers.google.com/custom-search) |
| **WhoisXML API** | 域名情报 | [whoisxmlapi.com](https://whoisxmlapi.com/) |
| **Criminal IP API** | 威胁情报 | [criminalip.io/developer](https://www.criminalip.io/developer) |

---

## 37. OSINT 浏览器扩展

> 🧩 每个 OSINT 调查者必备的浏览器扩展。

| Extension | 说明 | Browser |
|-----------|-------------|:-------:|
| **Search by Image** | 多引擎反向图搜 | Chrome / Firefox |
| **Wappalyzer** | 技术栈识别 | Chrome / Firefox |
| **Shodan** | 任意网站的服务器信息 | Chrome / Firefox |
| **Wayback Machine** | 即时查看网页存档 | Chrome / Firefox |
| **EXIF Viewer** | 查看图片元数据 | Chrome / Firefox |
| **User-Agent Switcher** | 更改浏览器指纹身份 | Chrome / Firefox |
| **FoxyProxy** | 代理管理 | Chrome / Firefox |
| **Hunchly** | OSINT 网页取证与案例管理 | Chrome |
| **InVID/WeVerify** | 视频/图像验证 | Chrome / Firefox |
| **SingleFile** | 保存完整网页 | Chrome / Firefox |

---

## 38. OSINT 学习资源

> 📚 最好的 OSINT 学习资源——从入门到专业。

| 资源 | 类型 | 链接 |
|----------|------|------|
| **OSINT Framework** | 交互式工具目录 | [osintframework.com](https://osintframework.com/) |
| **IntelTechniques** | Michael Bazzell 的资源与播客 | [inteltechniques.com](https://inteltechniques.com/) |
| **Bellingcat** | OSINT 调查报道 | [bellingcat.com](https://bellingcat.com/) |
| **Trace Labs** | 寻人主题 CTF 的 OSINT | [tracelabs.org](https://tracelabs.org/) |
| **OSINT Curious Project** | 社区与培训 | [osintcurio.us](https://osintcurio.us/) |
| **Sector035 Week in OSINT** | 每周 OSINT 简报 | [sector035.nl](https://sector035.nl/) |
| **OSINT Dojo** | 训练平台与挑战 | [osintdojo.com](https://osintdojo.com/) |
| **CTF Time** | 动手型 CTF 竞赛 | [ctftime.org](https://ctftime.org/) |
| **GIJN** | 全球调查记者网络 | [gijn.org](https://gijn.org/) |
| **SANS OSINT** | 专业网络安全训练 | [sans.org](https://sans.org/) |

### 📺 YouTube 频道

| Channel | Focus |
|---------|-------|
| **John Hammond** | Cybersecurity & CTFs |
| **The Cyber Mentor** | 道德黑客 |
| **David Bombal** | 网络与安全 |
| **NetworkChuck** | 网络安全教程 |
| **HackerSploit** | 渗透测试 |
| **Null Byte** | 黑客教程 |
| **13Cubed** | DFIR 与取证 |

---

## 39. Awesome OSINT GitHub 仓库

> ⭐ GitHub 上最好的 OSINT 精选资源清单。

| Repository | Stars | 链接 |
|-----------|:-----:|------|
| **jivoi/awesome-osint** | 20k+ | [github.com/jivoi/awesome-osint](https://github.com/jivoi/awesome-osint) |
| **danielmiessler/SecLists** | 55k+ | [github.com/danielmiessler/SecLists](https://github.com/danielmiessler/SecLists) |
| **Z4nzu/hackingtool** | 40k+ | [github.com/Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) |
| **cipher387/osint_stuff_tool_collection** | 6k+ | [github.com/cipher387/osint_stuff_tool_collection](https://github.com/cipher387/osint_stuff_tool_collection) |
| **Manisso/fsociety** | 10k+ | [github.com/Manisso/fsociety](https://github.com/Manisso/fsociety) |
| **sinwindie/OSINT** | 3k+ | [github.com/sinwindie/OSINT](https://github.com/sinwindie/OSINT) |
| **Astrosp/Awesome-OSINT-For-Everything** | 2k+ | [github.com/Astrosp/Awesome-OSINT-For-Everything](https://github.com/Astrosp/Awesome-OSINT-For-Everything) |
| **tracelabs/awesome-osint** | 1k+ | [github.com/tracelabs/awesome-osint](https://github.com/tracelabs/awesome-osint) |

---

## 40. 一键安装脚本

### 🐉 Kali Linux——完整军火库

```bash
# 方式一：直接用本仓库（一条命令）
curl -sL https://raw.githubusercontent.com/rawfilejson/awesome-osint-arsenal/main/install.sh | sudo bash

# 方式二：先克隆（推荐——先审查再运行）
git clone https://github.com/rawfilejson/awesome-osint-arsenal.git
cd awesome-osint-arsenal
sudo bash install.sh
```

### 📱 Termux（Android）

```bash
pkg update -y && pkg upgrade -y
pkg install -y python git wget curl nmap hydra perl openssh php clang make openssl
pip install requests colorama sherlock-project maigret holehe h8mail
cd ~ && git clone https://github.com/htr-tech/zphisher && git clone https://github.com/Manisso/fsociety
```

### 🔧 Kali 手动安装片段

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y git python3 python3-pip golang-go nmap wireshark \
  sqlmap hydra john hashcat aircrack-ng nikto dirb wpscan \
  theharvester maltego spiderfoot set exiftool masscan whatweb \
  gobuster feroxbuster wfuzz libimage-exiftool-perl binwalk \
  foremost bulk-extractor macchanger tor proxychains4

pip3 install sherlock-project maigret holehe h8mail socialscan \
  social-analyzer phoneinfoga snscrape instaloader deepface \
  face_recognition volatility3 blackbird-osint nexfil \
  socid-extractor osrframework telepathy twayback toutatis \
  dnstwist waybackpy trufflehog

cd /opt
sudo git clone https://github.com/Manisso/fsociety
sudo git clone https://github.com/Z4nzu/hackingtool
sudo git clone https://github.com/ultrasecurity/Storm-Breaker
sudo git clone https://github.com/htr-tech/zphisher
sudo git clone https://github.com/s0md3v/Orbit
sudo git clone https://github.com/s0md3v/Photon
sudo git clone https://github.com/danielmiessler/SecLists
sudo git clone https://github.com/lgandx/Responder
sudo git clone https://github.com/commixproject/commix
sudo git clone https://github.com/opsdisk/pagodo
sudo git clone https://github.com/RedSiege/EyeWitness
```

---

## 41. 必备工具 Top 50（速查）

| # | 工具 | Category | Install |
|:-:|------|----------|---------|
| 1 | **Sherlock** | Username OSINT | `pip install sherlock-project` |
| 2 | **Maigret** | 用户名 OSINT（3000+ 网站） | `pip install maigret` |
| 3 | **h8mail** | 邮箱泄露狩猎 | `pip install h8mail` |
| 4 | **Holehe** | 邮箱注册检查 | `pip install holehe` |
| 5 | **theHarvester** | 域名/邮箱侦察 | `apt install theharvester` |
| 6 | **PhoneInfoga** | 电话号码 OSINT | 见安装指南 |
| 7 | **Nmap** | 网络扫描 | `apt install nmap` |
| 8 | **Amass** | DNS 枚举 | `go install ...amass@master` |
| 9 | **Subfinder** | 子域名发现 | `go install ...subfinder@latest` |
| 10 | **Nuclei** | 漏洞扫描 | `go install ...nuclei@latest` |
| 11 | **SQLMap** | SQL 注入 | `apt install sqlmap` |
| 12 | **Metasploit** | 漏洞利用框架 | `apt install metasploit-framework` |
| 13 | **Hashcat** | 密码破解（GPU） | `apt install hashcat` |
| 14 | **Hydra** | 登录爆破 | `apt install hydra` |
| 15 | **Wireshark** | 网络分析 | `apt install wireshark` |
| 16 | **Aircrack-ng** | Wi-Fi 安全 | `apt install aircrack-ng` |
| 17 | **Burp Suite** | Web 代理/测试 | [portswigger.net](https://portswigger.net/) |
| 18 | **SpiderFoot** | OSINT 自动化 | `pip install spiderfoot` |
| 19 | **Maltego** | 可视化关联分析 | Kali 预装 |
| 20 | **Recon-ng** | 侦察框架 | `pip install recon-ng` |
| 21 | **PimEyes** | 人脸搜索引擎 | [pimeyes.com](https://pimeyes.com/) |
| 22 | **Shodan** | IoT 设备搜索 | [shodan.io](https://shodan.io/) |
| 23 | **Censys** | 互联网扫描 | [censys.io](https://censys.io/) |
| 24 | **Zphisher** | 钓鱼工具 | `git clone .../zphisher` |
| 25 | **Storm-Breaker** | 摄像头/麦克风社会工程工具 | `git clone .../Storm-Breaker` |
| 26 | **ExifTool** | 图片元数据 | `apt install libimage-exiftool-perl` |
| 27 | **Autopsy** | 数字取证 | [autopsy.com](https://autopsy.com/) |
| 28 | **Volatility** | 内存取证 | `pip install volatility3` |
| 29 | **Tor Browser** | 匿名浏览 | [torproject.org](https://torproject.org/) |
| 30 | **DeHashed** | 泄露数据搜索引擎 | [dehashed.com](https://dehashed.com/) |
| 31 | **Have I Been Pwned** | 泄露检查器 | [haveibeenpwned.com](https://haveibeenpwned.com/) |
| 32 | **fsociety** | 一体化框架 | `git clone .../fsociety` |
| 33 | **Hackingtool** | 100+ 工具合一 | `git clone .../hackingtool` |
| 34 | **SecLists** | 安全字典 | `git clone .../SecLists` |
| 35 | **Osintgram** | Instagram OSINT | `git clone .../Osintgram` |
| 36 | **VirusTotal** | 恶意软件/文件分析 | [virustotal.com](https://virustotal.com/) |
| 37 | **Canary Tokens** | IP 追踪令牌 | [canarytokens.org](https://canarytokens.org/) |
| 38 | **CyberChef** | 数据分析工具 | [gchq.github.io/CyberChef](https://gchq.github.io/CyberChef) |
| 39 | **DeepFace** | AI 人脸分析 | `pip install deepface` |
| 40 | **dnsrecon** | DNS 枚举 | `pip install dnsrecon` |
| 41 | **Gobuster** | 目录暴力破解 | `go install ...gobuster@latest` |
| 42 | **HTTPx** | HTTP 探测 | `go install ...httpx@latest` |
| 43 | **EyeWitness** | 网页截图 | `git clone .../EyeWitness` |
| 44 | **Responder** | LLMNR/NBT-NS 毒化工具 | `git clone .../Responder` |
| 45 | **Bettercap** | 中间人框架 | `apt install bettercap` |
| 46 | **Photon** | Web OSINT 爬虫 | `git clone .../Photon` |
| 47 | **Perplexity AI** | AI 研究助手 | [perplexity.ai](https://perplexity.ai/) |
| 48 | **GeoSpy** | AI 图像地理定位 | [geospy.ai](https://geospy.ai/) |
| 49 | **osmedeus** | 完整侦察工作流 | `git clone .../osmedeus` |
| 50 | **trufflehog** | git 机密扫描器 | `pip install trufflehog` |

---


<div align="center">

☕ *喜欢以上内容？42-50 章刚刚更新——支持一下下一批：*

<a href="https://www.buymeacoffee.com/rawfilejson" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me a Coffee" style="height: 60px !important;width: 217px !important;" ></a>

</div>

---

## 42. ⚔️ 红队与攻击安全

> C2 frameworks, AD attacks, exploitation kits, post-exploitation. Authorized testing only.
>
> **实用建议：** Sliver 和 Havoc 是现代化的开源 Cobalt Strike 替代品——付费前先从它们入手。

| 工具 | 说明 | 安装 / 链接 |
|------|-------------|----------------|
| **AD Attack & Defense** | Active Directory 攻击大全参考 | `git clone https://github.com/infosecn1nja/AD-Attack-Defense.git` |
| **Arjun** | HTTP 参数发现套件 | `pip3 install arjun` |
| **BloodHound** | AD 攻击路径图分析 | `git clone https://github.com/BloodHoundAD/BloodHound.git` |
| **BloodHound CE** | BloodHound 社区版——技术栈现代化 | `docker pull specterops/bloodhound:latest` |
| **[Brute Ratel C4](https://bruteratel.com)** | 付费 C2，AV/EDR 绕过能力强 | [bruteratel.com](https://bruteratel.com) |
| **Certipy** | Active Directory 证书服务枚举与滥用 | `pip3 install certipy-ad` |
| **[Cobalt Strike](https://www.cobaltstrike.com)** | 付费攻击者仿真/红队框架 | [cobaltstrike.com](https://www.cobaltstrike.com) |
| **CrackMapExec** | 面向 AD 网络的后渗透工具 | `pip3 install crackmapexec` |
| **CRLFuzz** | Go 编写的快速 CRLF 注入扫描器 | `go install github.com/dwisiswant0/crlfuzz/cmd/crlfuzz@latest` |
| **Dalfox** | 快速智能的 XSS 扫描器 | `go install github.com/hahwul/dalfox/v2@latest` |
| **Evil-WinRM** | 渗透测试终极 WinRM Shell | `apt install evil-winrm` |
| **Ghauri** | 跨平台 SQL 注入检测/利用高级工具 | `git clone https://github.com/r0oth3x49/ghauri.git` |
| **Gxss** | 测试参数的 XSS 反射 | `go install github.com/KathanP19/Gxss@latest` |
| **[HackTricks](https://book.hacktricks.xyz)** | carlospolop 的渗透/黑客知识库 | [book.hacktricks.xyz](https://book.hacktricks.xyz) |
| **Havoc** | 现代、可塑的后渗透 C2 框架 | `git clone https://github.com/HavocFramework/Havoc.git` |
| **Impacket** | 处理网络协议的 Python 类库（Windows 攻击用） | `pip3 install impacket` |
| **Kerbrute** | Kerberos 预认证爆破工具 | `go install github.com/ropnop/kerbrute@latest` |
| **kiterunner** | 面向现代 API 端点的上下文内容发现 | `go install github.com/assetnote/kiterunner/cmd/kr@latest` |
| **Merlin** | Go 编写的跨平台 HTTP/2 后渗透服务端与客户端 | `go install github.com/Ne0nd0g/merlin@latest` |
| **Metasploit Framework** | 行业标准的漏洞利用框架，2000+ 模块 | `apt install metasploit-framework` |
| **Mythic** | 跨平台后渗透多用户红队框架 | `git clone https://github.com/its-a-feature/Mythic.git` |
| **NetExec (nxc)** | CrackMapExec 的持续维护后继——AD 网络利用 | `pip3 install git+https://github.com/Pennyw0rth/NetExec` |
| **[Nighthawk](https://www.mdsec.co.uk/nighthawk/)** | MDSec 出品的付费高免杀 C2（Cobalt Strike 替代） | [mdsec.co.uk](https://www.mdsec.co.uk/nighthawk/) |
| **NoSQLMap** | NoSQL 数据库自动化枚举与利用 | `git clone https://github.com/codingo/NoSQLMap.git` |
| **Nuclei Templates** | 社区维护的 Nuclei 模板库 | `git clone https://github.com/projectdiscovery/nuclei-templates.git` |
| **ParamMiner (Burp ext)** | 在 Burp 中发现隐藏的未链接 HTTP 参数 | `git clone https://github.com/PortSwigger/param-miner.git` |
| **PayloadsAllTheThings** | Web 应用渗透载荷、绕过技巧与方法论 | `git clone https://github.com/swisskyrepo/PayloadsAllTheThings.git` |
| **PetitPotam** | 迫使 Windows 主机向攻击者发起认证的 PoC 工具 | `git clone https://github.com/topotam/PetitPotam.git` |
| **PowerShell Empire** | 基于 PowerShell agent 的后渗透框架 | `git clone https://github.com/BC-SECURITY/Empire.git` |
| **Rubeus** | Kerberos 原始交互与滥用的 C# 工具集 | `git clone https://github.com/GhostPack/Rubeus.git` |
| **SharpHound** | BloodHound 的 C# 数据收集器 | `git clone https://github.com/BloodHoundAD/SharpHound.git` |
| **Sliver** | 开源攻击者仿真/红队框架（Cobalt Strike 替代） | `go install github.com/bishopfox/sliver/server@latest` |
| **SSRFmap** | SSRF 自动化检测与利用框架 | `git clone https://github.com/swisskyrepo/SSRFmap.git` |
| **Villain** | 管理同级 agent 的高层 0/1 阶段 C2 框架 | `git clone https://github.com/t3l3machus/Villain.git` |
| **XSStrike** | 带爬虫与载荷生成器的高级 XSS 扫描器 | `git clone https://github.com/s0md3v/XSStrike.git` |

---

## 43. 🛡️ 蓝队与防御安全

> SIEM, EDR, network monitoring, detection engineering, IR.
>
> **实用建议：** Wazuh 是免费的 Splunk 替代。配上 Sigma 规则 + Suricata，普通硬件就能跑起完整 SOC 技术栈。

| 工具 | 说明 | 安装 / 链接 |
|------|-------------|----------------|
| **Atomic Red Team** | 映射到 MITRE ATT&CK 的小型检测验证脚本库 | `git clone https://github.com/redcanaryco/atomic-red-team.git` |
| **Chainsaw** | 在 Windows 事件日志中狩猎威胁——快速取证 | `git clone https://github.com/WithSecureLabs/chainsaw.git` |
| **Cortex (TheHive)** | 观测对象分析与主动响应引擎 | `docker pull thehiveproject/cortex:latest` |
| **Elastic Stack (ELK)** | Elasticsearch + Logstash + Kibana——日志分析 | `docker pull docker.elastic.co/elasticsearch/elasticsearch:latest` |
| **Falco** | 云原生运行时安全 | `git clone https://github.com/falcosecurity/falco.git` |
| **Graylog** | 开源日志管理 / SIEM | `docker pull graylog/graylog:latest` |
| **Hayabusa** | Windows 事件日志快速取证时间线生成器 | `git clone https://github.com/Yamato-Security/hayabusa.git` |
| **Loki** | Florian Roth 出品的简洁 IOC 与 YARA 扫描器 | `git clone https://github.com/Neo23x0/Loki.git` |
| **[MITRE ATT&CK](https://attack.mitre.org)** | 攻击者战术、技术与程序知识库 | [attack.mitre.org](https://attack.mitre.org) |
| **MITRE CALDERA** | 网络攻击者仿真平台 | `git clone https://github.com/mitre/caldera.git` |
| **[MITRE D3FEND](https://d3fend.mitre.org)** | 防御措施知识图谱 | [d3fend.mitre.org](https://d3fend.mitre.org) |
| **osquery** | SQL 驱动的操作系统监控与分析 | `apt install osquery` |
| **RITA** | Real Intelligence Threat Analytics——信标/长连接检测 | `git clone https://github.com/activecm/rita.git` |
| **[Security Onion](https://securityonionsolutions.com)** | 面向威胁狩猎、监控与日志管理的 Linux 发行版 | [securityonionsolutions.com](https://securityonionsolutions.com) |
| **Sigma** | SIEM 检测用的通用规则格式 | `git clone https://github.com/SigmaHQ/sigma.git` |
| **sigma-cli** | 把 Sigma 规则转换为原生 SIEM 查询 | `pip3 install sigma-cli` |
| **Snort** | 开源入侵防御/检测系统 | `apt install snort` |
| **Suricata** | 高性能网络 IDS / IPS / NSM | `apt install suricata` |
| **TheHive** | 面向 SOC 的可扩展免费开源案例管理 | `docker pull strangebee/thehive:latest` |
| **Tracee** | 基于 eBPF 的运行时安全与取证（Aqua） | `git clone https://github.com/aquasecurity/tracee.git` |
| **Velociraptor** | 端点可见性与数字取证——查询驱动 | `git clone https://github.com/Velocidex/velociraptor.git` |
| **[Velociraptor Server](https://docs.velociraptor.app)** | Velociraptor 客户端的集中式服务器 | [docs.velociraptor.app](https://docs.velociraptor.app) |
| **Wazuh** | 开源 XDR / SIEM 平台 | `git clone https://github.com/wazuh/wazuh.git` |
| **Zeek (Bro)** | 面向安全监控的强大网络分析框架 | `apt install zeek` |

---

## 44. 🛰️ 威胁情报平台

> 网络威胁情报（CTI）平台——开源与企业级。
>
> **实用建议：** MISP 免费且强大。OpenCTI 提供原生 STIX2 图数据库。两者都能以 Docker 编排运行。

| 工具 | 说明 | 安装 / 链接 |
|------|-------------|----------------|
| **[Anomali ThreatStream](https://www.anomali.com)** | 企业威胁情报聚合平台 | [anomali.com](https://www.anomali.com) |
| **[CrowdStrike Falcon Intelligence](https://www.crowdstrike.com/products/threat-intelligence/)** | CrowdStrike 的付费攻击者情报 | [crowdstrike.com](https://www.crowdstrike.com/products/threat-intelligence/) |
| **[Digital Shadows SearchLight](https://www.reliaquest.com)** | 品牌保护 + 暗网监控（现为 ReliaQuest GreyMatter DRP） | [reliaquest.com](https://www.reliaquest.com) |
| **[EclecticIQ Intelligence Center](https://www.eclecticiq.com)** | 原生 STIX/TAXII 威胁情报平台 | [eclecticiq.com](https://www.eclecticiq.com) |
| **[Flashpoint](https://flashpoint.io)** | 来自犯罪论坛与暗网的商业风险情报 | [flashpoint.io](https://flashpoint.io) |
| **[Intel471](https://intel471.com)** | 付费攻击者情报与地下社区监控平台 | [intel471.com](https://intel471.com) |
| **[IntSights](https://intsights.com)** | 外部威胁防护与情报（已并入 Rapid7） | [intsights.com](https://intsights.com) |
| **[KELA](https://kelacyber.com)** | 网络犯罪情报与暗网监控 | [kelacyber.com](https://kelacyber.com) |
| **[Mandiant Advantage](https://www.mandiant.com/advantage)** | Google Mandiant 团队的威胁情报 | [mandiant.com](https://www.mandiant.com/advantage) |
| **OpenCTI** | 围绕 STIX2 构建的开源网络威胁情报平台 | `docker pull opencti/platform` |
| **[SOCRadar](https://socradar.io)** | 扩展威胁情报——攻击面 + 暗网 + 品牌 | [socradar.io](https://socradar.io) |
| **[ThreatConnect](https://threatconnect.com)** | 情报与 SOAR 一体的威胁情报平台 | [threatconnect.com](https://threatconnect.com) |
| **[ThreatQ](https://www.threatq.com)** | 面向 SOC 的威胁情报平台 | [threatq.com](https://www.threatq.com) |
| **Yeti** | 开源分布式威胁情报平台 | `git clone https://github.com/yeti-platform/yeti.git` |

---

## 45. 🔬 数字取证与逆向工程

> Disk/memory forensics, malware reverse engineering, timeline tools, binary analysis.
>
> **实用建议：** Volatility 3 + Plaso (log2timeline) + KAPE 就是现代 DFIR 分诊组合。静态分析选 Ghidra 而非 IDA Free。

| 工具 | 说明 | 安装 / 链接 |
|------|-------------|----------------|
| **[Binary Ninja](https://binary.ninja)** | 带 API 的现代逆向工程平台 | [binary.ninja](https://binary.ninja) |
| **Cutter** | radare2/rizin 逆向工程图形界面 | `git clone https://github.com/rizinorg/cutter.git` |
| **Dissect** | Fox-IT 出品的快速取证镜像分析框架 | `pip3 install dissect` |
| **[Eric Zimmerman's Tools](https://ericzimmerman.github.io)** | 免费 Windows 取响应工具套件 | [ericzimmerman.github.io](https://ericzimmerman.github.io) |
| **[FTK Imager](https://www.exterro.com/ftk-imager)** | AccessData 出品的取证磁盘镜像工具 | [exterro.com](https://www.exterro.com/ftk-imager) |
| **Ghidra** | NSA 的开源软件逆向套件 | `git clone https://github.com/NationalSecurityAgency/ghidra.git` |
| **[IDA Free](https://hex-rays.com/ida-free/)** | 免费版 IDA 反汇编器/反编译器 | [hex-rays.com](https://hex-rays.com/ida-free/) |
| **[KAPE](https://www.kroll.com/kape)** | Kroll 取证工件解析提取器——快速分诊采集 | [kroll.com](https://www.kroll.com/kape) |
| **PhotoRec** | 文件数据恢复——专注多媒体 | `apt install testdisk` |
| **Plaso (log2timeline)** | 从取证工件生成超级时间线 | `pip3 install plaso` |
| **radare2** | 逆向工程框架 | `apt install radare2` |
| **RegRipper** | 开源 Windows 注册表解析工具 | `git clone https://github.com/keydet89/RegRipper3.0.git` |
| **Rekall** | 内存取证工具（Volatility 旧版分支） | `pip3 install rekall` |
| **rizin** | radare2 的现代分支，API 更干净 | `git clone https://github.com/rizinorg/rizin.git` |
| **The Sleuth Kit** | 取证磁盘分析的库与命令行工具 | `apt install sleuthkit` |
| **Volatility 3** | 内存取证框架 | `pip3 install volatility3` |

---

## 46. 🎓 训练、靶场与 CTF

> 动手练习——付费平台与免费本地靶场。
>
> **Pro tip:** Free path: TryHackMe → PortSwigger Academy → HackTheBox retired boxes. Paid path: HTB Academy + OffSec PG.

| 工具 | 说明 | 安装 / 链接 |
|------|-------------|----------------|
| **[BugBountyHunter](https://www.bugbountyhunter.com)** | Web 黑客训练与靶场 | [bugbountyhunter.com](https://www.bugbountyhunter.com) |
| **[CTFtime](https://ctftime.org)** | CTF 赛事日历（过往与即将举行） | [ctftime.org](https://ctftime.org) |
| **[Cybrary](https://www.cybrary.it)** | 免费 + 付费的网络安全课程 | [cybrary.it](https://www.cybrary.it) |
| **DVWA** | Damn Vulnerable Web Application——经典 Web 安全靶场 | `git clone https://github.com/digininja/DVWA.git` |
| **[Hack The Box](https://www.hackthebox.com)** | 在线渗透靶场与 CTF | [hackthebox.com](https://www.hackthebox.com) |
| **[Hacker101](https://www.hacker101.com)** | 免费的 HackerOne 课程库与 CTF | [hacker101.com](https://www.hacker101.com) |
| **[Immersive Labs](https://www.immersivelabs.com)** | 带动手练习的网络安全技能平台 | [immersivelabs.com](https://www.immersivelabs.com) |
| **[Metasploitable](https://docs.rapid7.com/metasploit/metasploitable-2/)** | 供 Metasploit 练习的故意不安全 Linux 虚机 | [docs.rapid7.com](https://docs.rapid7.com/metasploit/metasploitable-2/) |
| **[OffSec Proving Grounds](https://www.offsec.com/labs/individual/)** | Offensive Security 的 OSCP 风格训练靶场 | [offsec.com](https://www.offsec.com/labs/individual/) |
| **[OverTheWire Wargames](https://overthewire.org)** | 从零学攻击安全的免费闯关游戏 | [overthewire.org](https://overthewire.org) |
| **OWASP Juice Shop** | 现代的故意不安全 Web 应用——覆盖 OWASP Top 10 | `docker pull bkimminich/juice-shop` |
| **OWASP WebGoat** | 供训练用的故意不安全的 Java Web 应用 | `docker pull webgoat/webgoat` |
| **[PentesterLab](https://pentesterlab.com)** | 动手式 Web 应用渗透测试训练 | [pentesterlab.com](https://pentesterlab.com) |
| **[picoCTF](https://picoctf.org)** | CMU 打造的免费 CTF 与学习平台 | [picoctf.org](https://picoctf.org) |
| **[PortSwigger Web Security Academy](https://portswigger.net/web-security)** | 免费世界级 Web 安全培训（Burp Suite 团队出品） | [portswigger.net](https://portswigger.net/web-security) |
| **[pwn.college](https://pwn.college)** | ASU 的免费大学级网络安全课程 | [pwn.college](https://pwn.college) |
| **PwnedHub** | 供 Web 安全动手训练的故意不安全应用 | `git clone https://github.com/practisec/pwnedhub.git` |
| **[Root-Me](https://www.root-me.org)** | 500+ 挑战与 100+ 虚拟实验室 | [root-me.org](https://www.root-me.org) |
| **[TryHackMe](https://tryhackme.com)** | 对新手友好的网络安全训练平台 | [tryhackme.com](https://tryhackme.com) |
| **[VulnHub](https://www.vulnhub.com)** | 可免费下载的漏洞虚机，用于离线练习 | [vulnhub.com](https://www.vulnhub.com) |
| **[VulnYX](https://vulnyx.com)** | 带漏洞靶机的在线平台（免费 + 付费） | [vulnyx.com](https://vulnyx.com) |

---

## 47. 🎯 漏洞赏金平台

> 真正能把技术变现的地方。
>
> **实用建议：** 从 Bugcrowd 或 YesWeHack 公开项目起步——分诊更友好，竞争也比 HackerOne H1 小。

| 工具 | 说明 | 安装 / 链接 |
|------|-------------|----------------|
| **[Bugbase](https://bugbase.ai)** | 印度出身的漏洞赏金 + 漏洞披露平台 | [bugbase.ai](https://bugbase.ai) |
| **[Bugcrowd](https://bugcrowd.com)** | 众包安全平台——漏洞赏金 + 渗透测试 | [bugcrowd.com](https://bugcrowd.com) |
| **[Disclose.io](https://disclose.io)** | 标准化的漏洞披露语言与工具 | [disclose.io](https://disclose.io) |
| **[HackerOne](https://hackerone.com)** | 最大漏洞赏金平台——公开与私密项目 | [hackerone.com](https://hackerone.com) |
| **[HackTrophy](https://hacktrophy.com)** | 欧洲漏洞赏金平台 | [hacktrophy.com](https://hacktrophy.com) |
| **[Immunefi](https://immunefi.com)** | 专注 Web3/加密货币的漏洞赏金平台 | [immunefi.com](https://immunefi.com) |
| **[Intigriti](https://www.intigriti.com)** | 欧洲漏洞赏金平台，分诊迅速 | [intigriti.com](https://www.intigriti.com) |
| **[Open Bug Bounty](https://www.openbugbounty.org)** | 免费协调漏洞披露平台 | [openbugbounty.org](https://www.openbugbounty.org) |
| **[Public Bug Bounty Programs (chaos)](https://chaos.projectdiscovery.io)** | ProjectDiscovery 的免费漏洞赏金计划清单 | [chaos.projectdiscovery.io](https://chaos.projectdiscovery.io) |
| **[Synack](https://www.synack.com)** | 众包 + 认证研究者渗透测试平台 | [synack.com](https://www.synack.com) |
| **[YesWeHack](https://www.yeswehack.com)** | 欧洲的漏洞赏金与漏洞披露平台 | [yeswehack.com](https://www.yeswehack.com) |
| **[Zerodium](https://zerodium.com)** | 付费 0day 收购平台 | [zerodium.com](https://zerodium.com) |

---

## 48. 📚 学习资源

> Books, courses, blogs, YouTube channels, awesome lists.
>
> **实用建议：** IppSec.rocks 索引了全部 HackTheBox 通关视频——搜任意退役靶机，看职业选手怎么解。

| 工具 | 说明 | 安装 / 链接 |
|------|-------------|----------------|
| **[0xdf hacks stuff](https://0xdf.gitlab.io)** | HTB 与渗透测试通关记录 | [0xdf.gitlab.io](https://0xdf.gitlab.io) |
| **[awesome-hacking-resources](https://github.com/vitalysim/Awesome-Hacking-Resources)** | 对新手友好的黑客学习资源 | [github.com](https://github.com/vitalysim/Awesome-Hacking-Resources) |
| **[awesome-incident-response](https://github.com/meirwah/awesome-incident-response)** | 应急响应工具与资源精选清单 | [github.com](https://github.com/meirwah/awesome-incident-response) |
| **[awesome-malware-analysis](https://github.com/rshipp/awesome-malware-analysis)** | 恶意软件分析工具精选清单 | [github.com](https://github.com/rshipp/awesome-malware-analysis) |
| **[awesome-pentest](https://github.com/enaqx/awesome-pentest)** | 大型渗透测试工具与资源精选清单 | [github.com](https://github.com/enaqx/awesome-pentest) |
| **[Bellingcat's Online Investigations Toolkit](https://www.bellingcat.com/resources/)** | Bellingcat 精选工具与方法论指南 | [bellingcat.com](https://www.bellingcat.com/resources/) |
| **[BTFM: Blue Team Field Manual](https://www.amazon.com/dp/154101636X)** | 蓝队应急响应简明参考 | [amazon.com](https://www.amazon.com/dp/154101636X) |
| **[Hacking: The Art of Exploitation (book)](https://nostarch.com/hacking2.htm)** | Jon Erickson 经典著作——底层攻击原理 | [nostarch.com](https://nostarch.com/hacking2.htm) |
| **[IppSec.rocks](https://ippsec.rocks)** | HackTheBox 靶机通关索引（视频） | [ippsec.rocks](https://ippsec.rocks) |
| **[John Hammond](https://www.youtube.com/@_JohnHammond)** | 网络安全 YouTube——CTF、恶意软件、通关实录 | [youtube.com](https://www.youtube.com/@_JohnHammond) |
| **Linux for OSINT (cipher387)** | 21 天 Linux OSINT 课程（免费） | `git clone https://github.com/cipher387/linux-for-OSINT-21-days.git` |
| **[LiveOverflow](https://www.youtube.com/@LiveOverflow)** | 黑客与安全 YouTube——深度技术内容 | [youtube.com](https://www.youtube.com/@LiveOverflow) |
| **[NahamSec](https://www.youtube.com/@nahamsec)** | 漏洞赏金与攻击安全的 YouTube 内容 | [youtube.com](https://www.youtube.com/@nahamsec) |
| **[Netlas Cookbook](https://academy.netlas.io)** | 免费 OSINT 自动化手册 | [academy.netlas.io](https://academy.netlas.io) |
| **[OSINT Curious](https://osintcurio.us)** | 社区博客、播客与学习资源 | [osintcurio.us](https://osintcurio.us) |
| **[OSINT Techniques](https://inteltechniques.com)** | Michael Bazzell 的资源、著作与搜索工具 | [inteltechniques.com](https://inteltechniques.com) |
| **Python for OSINT (cipher387)** | 21 天 Python OSINT 课程（免费） | `git clone https://github.com/cipher387/python-for-OSINT-21-days.git` |
| **[Real-World Bug Hunting (book)](https://nostarch.com/bughunting)** | Peter Yaworski——漏洞赏金方法论与真实报告 | [nostarch.com](https://nostarch.com/bughunting) |
| **[RTFM: Red Team Field Manual](https://www.amazon.com/dp/B07RJG62SJ)** | 红队命令简明参考 | [amazon.com](https://www.amazon.com/dp/B07RJG62SJ) |
| **[The Web Application Hacker's Handbook (book)](https://www.amazon.com/dp/1118026470)** | Stuttard & Pinto——Web 安全圣经 | [amazon.com](https://www.amazon.com/dp/1118026470) |

---

## 49. ✨ 补充工具（精选新增）

> v2.x 新增工具——现代侦察、档案查询、小众服务与研究级拓展分析。
>
> **实用建议：** 本节每次发布都会更新——用老工具前先来翻一翻。

| 工具 | 说明 | 安装 / 链接 |
|------|-------------|----------------|
| **[abuse.ch Hunting](https://hunting.abuse.ch)** | 一次查询横扫 abuse.ch 全部恶意软件平台 | [hunting.abuse.ch](https://hunting.abuse.ch) |
| **[Aleph Open Search](https://open-search.aleph-networks.eu)** | Aleph Networks 出品的暗网搜索引擎 | [open-search.aleph-networks.eu](https://open-search.aleph-networks.eu) |
| **[Aletheia (image forensics)](https://www.aletheia.ai)** | 检测篡改/AI 生成图像 | [aletheia.ai](https://www.aletheia.ai) |
| **altdns** | 生成子域名的排列、变形与变异组合 | `pip3 install py-altdns` |
| **anew** | 把 stdin 的行追加到文件，已存在则跳过 | `go install github.com/tomnomnom/anew@latest` |
| **[ANY.RUN](https://any.run)** | 交互式在线恶意软件沙箱 | [any.run](https://any.run) |
| **[Apollo.io](https://www.apollo.io)** | B2B 电话/邮箱查找——每年 1200 次免费额度 | [apollo.io](https://www.apollo.io) |
| **[APT Groups and Operations](https://docs.google.com/spreadsheets/u/0/d/1H9_xaxQHpWaa4O_Son4Gx0YOIzlcBWMsdvePFX68EKU/pubhtml)** | 威胁行为体、支持国家与 TTPs 表格 | [docs.google.com](https://docs.google.com/spreadsheets/u/0/d/1H9_xaxQHpWaa4O_Son4Gx0YOIzlcBWMsdvePFX68EKU/pubhtml) |
| **Aquatone** | 跨主机网站可视化检视（HTTP 截图、攻击面巡览） | `go install github.com/michenriksen/aquatone@latest` |
| **[Archive.today](https://archive.ph)** | 网页存档——robots.txt 挡住 Wayback 时也能存快照 | [archive.ph](https://archive.ph) |
| **Arctic Shift** | 通过 API/网页访问 Reddit 大型数据导出的工具 | `git clone https://github.com/ArthurHeitmann/arctic_shift.git` |
| **[Arkham Intelligence](https://www.arkhamintelligence.com)** | 链上情报——标签、实体、历史资金流 | [arkhamintelligence.com](https://www.arkhamintelligence.com) |
| **assetfinder** | 查找与给定域名相关的域名与子域名 | `go install github.com/tomnomnom/assetfinder@latest` |
| **AutoRecon** | 多线程网络侦察与枚举框架 | `pip3 install git+https://github.com/Tib3rius/AutoRecon.git` |
| **Axiom** | 并行云端侦察的动态基础设施框架 | `git clone https://github.com/pry0cc/axiom.git` |
| **[BackgroundChecks.com](https://www.backgroundchecks.com)** | 背景调查聚合（BeenVerified 系） | [backgroundchecks.com](https://www.backgroundchecks.com) |
| **[Baidu](https://www.baidu.com)** | 中国主流搜索引擎——面向中国的 OSINT 必备 | [baidu.com](https://www.baidu.com) |
| **[BeVigil](https://bevigil.com/search)** | 从移动应用中提取子域名、URL 与参数 | [bevigil.com](https://bevigil.com/search) |
| **[BGP.tools](https://bgp.tools)** | 用于网络侦察的现代 BGP 工具包 | [bgp.tools](https://bgp.tools) |
| **[BinaryEdge](https://www.binaryedge.io)** | 网络风险与攻击面情报 | [binaryedge.io](https://www.binaryedge.io) |
| **[Bitquery](https://bitquery.io)** | 链上调查用的区块链数据 API | [bitquery.io](https://bitquery.io) |
| **[Black Book Online](https://www.blackbookonline.info)** | 免费全国公共记录查询目录 | [blackbookonline.info](https://www.blackbookonline.info) |
| **BlackEye** | 32+ 钓鱼模板生成器，用于凭据捕获（仅限实验环境） | `git clone https://github.com/An0nUD4Y/blackeye.git` |
| **[Brave Browser](https://brave.com)** | 隐私优先的浏览器，内置 Tor/IPFS 支持 | [brave.com](https://brave.com) |
| **[Brave Search](https://search.brave.com)** | 独立、透明、无广告的搜索引擎 | [search.brave.com](https://search.brave.com) |
| **[BreachForums Status](https://www.breachforums.cx)** | BreachForums 轮换镜像状态跟踪 | [breachforums.cx](https://www.breachforums.cx) |
| **[Breadcrumbs](https://breadcrumbs.app)** | 免费加密货币调查平台——交易流可视化 | [breadcrumbs.app](https://breadcrumbs.app) |
| **[BrightCloud Threat Intelligence](https://brightcloud.com)** | URL/IP/威胁信誉数据库 | [brightcloud.com](https://brightcloud.com) |
| **[BrightCloud URL/IP Lookup](https://brightcloud.com/tools/url-ip-lookup.php)** | URL/IP 的信誉、分类与威胁检查 | [brightcloud.com](https://brightcloud.com/tools/url-ip-lookup.php) |
| **[BscScan](https://bscscan.com)** | 币安智能链浏览器——体验同 Etherscan | [bscscan.com](https://bscscan.com) |
| **[CachedView](https://cachedview.com)** | 查看任意页面在 Google/Bing/Yandex 的缓存版本 | [cachedview.com](https://cachedview.com) |
| **[Castrick](https://castrickclues.com)** | 通过邮箱、用户名、手机号找社交媒体账号 | [castrickclues.com](https://castrickclues.com) |
| **Censys CLI** | Censys 官方 Python 封装与命令行 | `pip3 install censys` |
| **[CertKit Certificate Search](https://www.certkit.io/tools/ct-logs/)** | 快速查询公开 SSL/TLS 证书记录 | [certkit.io](https://www.certkit.io/tools/ct-logs/) |
| **[Chainabuse](https://www.chainabuse.com)** | 公开的加密货币骗局举报库 | [chainabuse.com](https://www.chainabuse.com) |
| **[Chainalysis Reactor](https://www.chainalysis.com/product/reactor/)** | 付费区块链调查平台 | [chainalysis.com](https://www.chainalysis.com/product/reactor/) |
| **[CheckUser](https://checkuser.vercel.app)** | 跨多个社交网络搜用户名 | [checkuser.vercel.app](https://checkuser.vercel.app) |
| **[CIRCL Hashlookup](https://www.circl.lu/services/hashlookup)** | 免费已知软件文件哈希查询 | [circl.lu](https://www.circl.lu/services/hashlookup) |
| **[Cisco Talos Intelligence](https://talosintelligence.com/reputation_center)** | 用于实时检测的 IP 与域名信誉中心 | [talosintelligence.com](https://talosintelligence.com/reputation_center) |
| **[Clearbit Connect](https://connect.clearbit.com)** | 带公司数据的邮箱查找浏览器扩展 | [connect.clearbit.com](https://connect.clearbit.com) |
| **[Cloudflare Radar](https://radar.cloudflare.com)** | 互联网流量模式、攻击与技术趋势 | [radar.cloudflare.com](https://radar.cloudflare.com) |
| **[Clustrmaps](https://clustrmaps.com)** | 查找人物与住址信息 | [clustrmaps.com](https://clustrmaps.com) |
| **[Commander Search](https://www.commandersearch.com)** | 面向 OSINT 调查者的布尔搜索构建器 | [commandersearch.com](https://www.commandersearch.com) |
| **[Constella Intelligence](https://constellaintelligence.com)** | 来自泄露库与暗网的身份威胁情报 | [constellaintelligence.com](https://constellaintelligence.com) |
| **[ContactOut](https://contactout.com)** | 查找 3 亿+ 职业人士的邮箱与电话 | [contactout.com](https://contactout.com) |
| **[CredenShow](https://credenshow.com)** | 赶在别人之前发现你已泄露的凭据 | [credenshow.com](https://credenshow.com) |
| **CrossLinked** | LinkedIn 枚举——从档案生成用户名清单 | `pip3 install crosslinked` |
| **[DBpedia](https://www.dbpedia.org)** | 结构化维基百科数据——SPARQL 端点 | [dbpedia.org](https://www.dbpedia.org) |
| **[Digital Footprint Check](https://www.digitalfootprintcheck.com/free-checker.html)** | 数百个网站的免费用户名查询 | [digitalfootprintcheck.com](https://www.digitalfootprintcheck.com/free-checker.html) |
| **dirsearch** | Web 路径扫描器——基于字典的高级目录爆破 | `pip3 install dirsearch` |
| **[Discord Lookup](https://discordlookup.com)** | 通过 ID 查 Discord 用户信息 | [discordlookup.com](https://discordlookup.com) |
| **[DiscordHistory](https://disboard.org)** | 搜索公开 Discord 服务器与消息 | [disboard.org](https://disboard.org) |
| **[DNS History](https://dnshistory.org)** | 历史 DNS 记录查询 | [dnshistory.org](https://dnshistory.org) |
| **[DocumentCloud](https://www.documentcloud.org)** | 文档分析、批注与发布平台 | [documentcloud.org](https://www.documentcloud.org) |
| **[DomainEye Reverse WHOIS](https://domaineye.com/reverse-whois)** | 按注册人信息搜域名 | [domaineye.com](https://domaineye.com/reverse-whois) |
| **dork-cli** | 在命令行运行 Google Dork | `git clone https://github.com/jgor/dork-cli.git` |
| **[DorkGenius](https://dorkgenius.com)** | 面向 Google、Bing、DuckDuckGo 的 AI 搜索语法生成器 | [dorkgenius.com](https://dorkgenius.com) |
| **[Dorky](https://dorky.io)** | 面向 Google/Bing/DuckDuckGo 的在线 Dork 构建器 | [dorky.io](https://dorky.io) |
| **[Dune Analytics](https://dune.com)** | 对已索引区块链数据做 SQL 查询 | [dune.com](https://dune.com) |
| **[Elliptic](https://www.elliptic.co)** | 加密货币金融犯罪检测与调查 | [elliptic.co](https://www.elliptic.co) |
| **[EmailRep.io](https://emailrep.io)** | Sublime Security 的免费邮箱信誉 API | [emailrep.io](https://emailrep.io) |
| **[Epieos Tools](https://tools.epieos.com)** | 反查邮箱/手机号对应的 Google 档案 | [tools.epieos.com](https://tools.epieos.com) |
| **[Epstein Exposed](https://epsteinexposed.com)** | 美国司法部爱泼斯坦案 200 万+ 文档与关系图的可检索库 | [epsteinexposed.com](https://epsteinexposed.com) |
| **[ETDA APT Groups](https://apt.etda.or.th/cgi-bin/listgroups.cgi)** | 搜索威胁行为组织及其工具 | [apt.etda.or.th](https://apt.etda.or.th/cgi-bin/listgroups.cgi) |
| **etherscan-py** | Etherscan API 的 Python 封装 | `pip3 install etherscan-python` |
| **[ExportData](https://www.exportdata.io)** | 历史推文、关注者与趋势导出工具 | [exportdata.io](https://www.exportdata.io) |
| **[FamilyTreeNow](https://familytreenow.com)** | 免费家谱检索——住址、电话、邮箱 | [familytreenow.com](https://familytreenow.com) |
| **ffuf** | Go 编写的快速 Web 模糊测试——目录、参数、vhost 发现 | `go install github.com/ffuf/ffuf/v2@latest` |
| **[Filesec.io](https://filesec.io)** | 恶意文件扩展名、风险与系统级缓解措施目录 | [filesec.io](https://filesec.io) |
| **Findomain** | 带监控功能的跨平台子域名枚举器 | `git clone https://github.com/Findomain/Findomain.git` |
| **[Flickr](https://www.flickr.com)** | 图片分享——地理搜索 + 许可信息 + 相机 EXIF 完整 | [flickr.com](https://www.flickr.com) |
| **[Foller.me](https://foller.me)** | Twitter 分析——简介、语言、话题标签、提及 | [foller.me](https://foller.me) |
| **[Forensically Beta](https://29a.ch/photo-forensics)** | 在线图像取证——克隆检测、电平扫描 | [29a.ch](https://29a.ch/photo-forensics) |
| **[FullContact](https://www.fullcontact.com)** | 身份归一 API 与人物信息增强 | [fullcontact.com](https://www.fullcontact.com) |
| **gau (getallurls)** | 从 AlienVault OTX、Wayback、Common Crawl、URLScan 拉取 URL | `go install github.com/lc/gau/v2/cmd/gau@latest` |
| **[Geocreepy](http://www.geocreepy.com)** | 地理定位聚合器——汇聚各网络的带位置帖子 | [geocreepy.com](http://www.geocreepy.com) |
| **[GeoHints](https://geohints.com)** | 浏览器内的卫星/街景地理定位训练与调查 | [geohints.com](https://geohints.com) |
| **[GeoSpy Pro](https://geospy.ai/pro)** | Graylark 出品的付费 AI 图像地理定位 | [geospy.ai](https://geospy.ai/pro) |
| **[Get-Metadata.com](https://www.get-metadata.com)** | 在线 EXIF 提取器——也支持 .DOCX/.PDF | [get-metadata.com](https://www.get-metadata.com) |
| **gf** | 面向漏洞赏金工作流的 grep 封装与规则库 | `go install github.com/tomnomnom/gf@latest` |
| **[Ghiro](https://www.getghiro.org)** | 数字图像取证自动化 | [getghiro.org](https://www.getghiro.org) |
| **git-hound** | 通过 GitHub 代码搜索发现暴露的敏感数据 | `go install github.com/tillson/git-hound@latest` |
| **github_monitor** | 实时追踪 GitHub 用户动态与仓库变更 | `git clone https://github.com/misiektoja/github_monitor.git` |
| **gitleaks** | 检测 git 仓库中的机密、凭据与 API key | `go install github.com/gitleaks/gitleaks/v8@latest` |
| **[Google Guide Advanced Operators](http://www.googleguide.com/advanced_operators_reference.html)** | Google 搜索运算符参考 | [googleguide.com](http://www.googleguide.com/advanced_operators_reference.html) |
| **[Google Hacking Database (GHDB)](https://www.exploit-db.com/google-hacking-database)** | 用于发现公开暴露信息的 Dork 语法索引 | [exploit-db.com](https://www.exploit-db.com/google-hacking-database) |
| **GoSpider** | Go 编写的快速网页爬虫，用于抓取/审计 | `go install github.com/jaeles-project/gospider@latest` |
| **gowitness** | Go 编写的现代网页截图工具（Aquatone 后继） | `go install github.com/sensepost/gowitness@latest` |
| **[GrayhatWarfare](https://grayhatwarfare.com)** | 开放 Amazon S3 存储桶索引——发现暴露的云数据 | [grayhatwarfare.com](https://grayhatwarfare.com) |
| **GreyNoise CLI** | GreyNoise 批量扫描器情报命令行工具 | `pip3 install greynoise` |
| **[GreyNoise Visualizer](https://viz.greynoise.io)** | 区分哪些 IP 是扫描噪声、哪些是定向威胁 | [viz.greynoise.io](https://viz.greynoise.io) |
| **hakrawler** | Go 编写的快速网页爬虫，用于端点与资产发现 | `go install github.com/hakluke/hakrawler@latest` |
| **[Hatching Triage](https://tria.ge)** | 带内核级监控的现代恶意软件沙箱 | [tria.ge](https://tria.ge) |
| **[haveibeenzuckered](https://haveibeenzuckered.com)** | 查手机号是否在 5.33 亿条 Facebook 泄露数据中 | [haveibeenzuckered.com](https://haveibeenzuckered.com) |
| **[HIB Ransomed](https://haveibeenransom.com)** | 查你的数据是否被勒索组织泄露 | [haveibeenransom.com](https://haveibeenransom.com) |
| **httprobe** | 拿域名清单探测可用的 HTTP/HTTPS | `go install github.com/tomnomnom/httprobe@latest` |
| **[Hudson Rock](https://www.hudsonrock.com/free-tools)** | 免费的信息窃取木马暴露检查（域名/邮箱/IP） | [hudsonrock.com](https://www.hudsonrock.com/free-tools) |
| **[Hybrid Analysis](https://www.hybrid-analysis.com)** | CrowdStrike 的免费高级恶意软件分析服务 | [hybrid-analysis.com](https://www.hybrid-analysis.com) |
| **[IKnowYour.Dad](https://iknowyour.dad)** | 数据泄露搜索引擎 | [iknowyour.dad](https://iknowyour.dad) |
| **[Imgur](https://imgur.com)** | 图床——梗图溯源与反向搜索 | [imgur.com](https://imgur.com) |
| **insta-dl** | 异步 Instagram 下载器，支持主页、帖子、Reels、快拍、精选、话题标签与评论 | `pip3 install instagram-dl` |
| **instagram_monitor** | 实时追踪 Instagram 用户，带邮件告警与 CSV 日志 | `git clone https://github.com/misiektoja/instagram_monitor.git` |
| **insto** | 交互式 Instagram OSINT 命令行，带快照、差异对比与 Maltego 导出 | `pip3 install insto` |
| **[Intelligence X (intelx.io)](https://intelx.io)** | 选择性存档搜索——邮箱、泄露、粘贴站、暗网 | [intelx.io](https://intelx.io) |
| **Interlace** | 把单线程命令行工具轻松变成多线程任务 | `git clone https://github.com/codingo/Interlace.git` |
| **[Joe Sandbox](https://www.joesandbox.com)** | 深度自动化恶意软件分析（有免费档） | [joesandbox.com](https://www.joesandbox.com) |
| **JSFinder** | 找出 URL 引用的 JS 文件——端点/API 路径 | `git clone https://github.com/Threezh1/JSFinder.git` |
| **[Kagi Search](https://kagi.com)** | 尊重隐私的付费搜索引擎，无广告无追踪 | [kagi.com](https://kagi.com) |
| **knock** | 域名探测——通过 DNS 做安全测试 | `git clone https://github.com/guelfoweb/knock.git` |
| **Knockpy** | 带虚拟主机发现的子域名枚举扫描 | `pip3 install knock-subdomains` |
| **linkedin2username** | 从目标公司的 LinkedIn 员工生成用户名 | `git clone https://github.com/initstring/linkedin2username.git` |
| **LinkedInDumper** | 从 LinkedIn API 导出/抓取公司员工 | `git clone https://github.com/l4rm4nd/LinkedInDumper.git` |
| **[Malpedia](https://malpedia.caad.fkie.fraunhofer.de)** | Fraunhofer 的威胁组织、恶意软件家族与分析 | [malpedia.caad.fkie.fraunhofer.de](https://malpedia.caad.fkie.fraunhofer.de) |
| **[MalShare](https://malshare.com)** | 面向研究者的免费恶意软件样本库 | [malshare.com](https://malshare.com) |
| **massdns** | 面向批量查询的高性能 DNS 存根解析器 | `git clone https://github.com/blechschmidt/massdns.git` |
| **meg** | 多主机多路径抓取且不触发告警 | `go install github.com/tomnomnom/meg@latest` |
| **[Memento Time Travel](https://timetravel.mementoweb.org)** | 跨多个网页存档的联合搜索 | [timetravel.mementoweb.org](https://timetravel.mementoweb.org) |
| **[Metadata2Go](https://www.metadata2go.com)** | 免费的在线任意文件元数据提取器 | [metadata2go.com](https://www.metadata2go.com) |
| **[MetaDefender Cloud](https://metadefender.com)** | OPSWAT 的多引擎文件/URL/IP 扫描 | [metadefender.com](https://metadefender.com) |
| **[MetaSleuth](https://metasleuth.io)** | 免费 + 付费的加密货币交易追踪工具 | [metasleuth.io](https://metasleuth.io) |
| **[MISP Galaxy](https://www.misp-galaxy.org)** | SOC/ISAC 使用的攻击组织识别 | [misp-galaxy.org](https://www.misp-galaxy.org) |
| **Mitaka** | OSINT 浏览器扩展——从选中文本提取 IoC | `git clone https://github.com/ninoseki/mitaka.git` |
| **[Mnemonic Passive DNS](https://passivedns.mnemonic.no)** | 免费被动 DNS 查询工具 | [passivedns.mnemonic.no](https://passivedns.mnemonic.no) |
| **[Mojeek](https://www.mojeek.com)** | 不追踪用户的独立搜索引擎 | [mojeek.com](https://www.mojeek.com) |
| **[Mylnikov Geolocation](https://www.mylnikov.org)** | BSSID/Wi-Fi MAC 反查坐标 | [mylnikov.org](https://www.mylnikov.org) |
| **Naabu** | ProjectDiscovery 出品的 Go 快速端口扫描器 | `go install github.com/projectdiscovery/naabu/v2/cmd/naabu@latest` |
| **[Name Checkr](https://www.namecheckr.com)** | 跨多平台查域名与用户名 | [namecheckr.com](https://www.namecheckr.com) |
| **[Name Checkup](https://namecheckup.com)** | 查用户名在各社交平台的占用情况 | [namecheckup.com](https://namecheckup.com) |
| **[NameKetchup](https://nameketchup.com)** | 在主流社交媒体查域名 + 用户名 | [nameketchup.com](https://nameketchup.com) |
| **[Naver](https://www.naver.com)** | 韩国搜索引擎——Google 搜不到的本地内容 | [naver.com](https://www.naver.com) |
| **[NerdyData](https://nerdydata.com)** | 公开网络源码搜索引擎 | [nerdydata.com](https://nerdydata.com) |
| **[Netcraft Site Report](https://sitereport.netcraft.com)** | 网站技术、托管历史与下架服务 | [sitereport.netcraft.com](https://sitereport.netcraft.com) |
| **Oblivion** | OSINT 框架 | `git clone https://github.com/loseys/Oblivion.git` |
| **[ODIN](https://search.odin.io)** | 搜主机、CVE、暴露存储桶——每天 10 次免费 | [search.odin.io](https://search.odin.io) |
| **[Offshore Leaks Database](https://offshoreleaks.icij.org)** | 巴拿马/潘多拉/天堂文件可检索数据库 | [offshoreleaks.icij.org](https://offshoreleaks.icij.org) |
| **[OnionLand Search](https://onionlandsearchengine.com)** | 暗网内容搜索引擎 | [onionlandsearchengine.com](https://onionlandsearchengine.com) |
| **[Open-Source Intelligence (Reverse Image)](https://oosint.com)** | Yandex/Bing/TinEye 聚合反向图搜 | [oosint.com](https://oosint.com) |
| **[OpenCellID](https://opencellid.org)** | 最大的公开基站 ID 数据库 | [opencellid.org](https://opencellid.org) |
| **opencorporates-cli** | OpenCorporates API 命令行客户端 | `pip3 install opencorporates` |
| **[OpenPhish](https://openphish.com)** | 实时钓鱼网址订阅源 | [openphish.com](https://openphish.com) |
| **[OpenRailwayMap](https://www.openrailwaymap.org)** | 全球铁路网地图——机车车辆、基础设施、信号 | [openrailwaymap.org](https://www.openrailwaymap.org) |
| **[OpenSanctions](https://opensanctions.org)** | 聚合 200+ 来源的制裁实体数据库 | [opensanctions.org](https://opensanctions.org) |
| **[OXT (OpenXt)](https://oxt.me)** | 带聚类分析的比特币交易图谱浏览器 | [oxt.me](https://oxt.me) |
| **[PassiveTotal (RiskIQ)](https://community.riskiq.com)** | 被动 DNS、WHOIS、SSL 证书拓展——现为 Microsoft Defender TI | [community.riskiq.com](https://community.riskiq.com) |
| **[Peekalink](https://www.peekalink.io)** | 预览任意 URL——通过 API 取标题、描述与截图 | [peekalink.io](https://www.peekalink.io) |
| **[PhishStats](https://phishstats.info)** | 实时钓鱼情报订阅与搜索 | [phishstats.info](https://phishstats.info) |
| **[PhishTank](https://phishtank.org)** | 反钓鱼社区——已验证的钓鱼网址库 | [phishtank.org](https://phishtank.org) |
| **[Picarta.ai](https://picarta.ai)** | AI 驱动的照片地理位置预测 | [picarta.ai](https://picarta.ai) |
| **[Pinterest](https://www.pinterest.com)** | 视觉搜索引擎——反向图搜备选 | [pinterest.com](https://www.pinterest.com) |
| **[PolygonScan](https://polygonscan.com)** | Polygon (Matic) 区块链浏览器 | [polygonscan.com](https://polygonscan.com) |
| **[Predicta Search](https://predictasearch.com)** | 按邮箱或手机号搜社交账号 | [predictasearch.com](https://predictasearch.com) |
| **[Public Transport Maps](https://cipher387.github.io/public_transport_maps/)** | 按国家整理的 20+ 在线公共交通地图 | [cipher387.github.io](https://cipher387.github.io/public_transport_maps/) |
| **[PublicWWW](https://publicwww.com)** | 在网页源码（HTML/JS/CSS）中搜片段、追踪器与脚本 | [publicwww.com](https://publicwww.com) |
| **[PullPush](https://pullpush.io)** | Reddit 索引/检索服务（含已删除内容） | [pullpush.io](https://pullpush.io) |
| **[Pushshift API](https://pushshift.io)** | Reddit 历史数据——帖子、评论、元数据 | [pushshift.io](https://pushshift.io) |
| **[Quake (360.cn)](https://quake.360.net)** | 中国互联网资产搜索引擎 | [quake.360.net](https://quake.360.net) |
| **[RECAP Archive](https://www.courtlistener.com/recap/)** | PACER 法院文档公共档案 | [courtlistener.com](https://www.courtlistener.com/recap/) |
| **reconFTW** | 全套域名侦察——子域名枚举、端口扫描、漏洞扫描一条流水线 | `git clone https://github.com/six2dez/reconftw.git` |
| **[RedditMetis](https://redditmetis.com)** | Reddit 用户分析——摘要、热门帖、活跃度统计 | [redditmetis.com](https://redditmetis.com) |
| **[RedditSearch.io](https://redditsearch.io)** | 通过 Pushshift 镜像检索 Reddit 存档 | [redditsearch.io](https://redditsearch.io) |
| **[Revealer.cc](https://revealer.cc)** | 基于 Discord 的账号检测与泄露查询 | [revealer.cc](https://revealer.cc) |
| **[RocketReach](https://rocketreach.co)** | 查找 7 亿+ 档案的职业邮箱/电话 | [rocketreach.co](https://rocketreach.co) |
| **RustScan** | 现代端口扫描器——先找开放端口再交给 Nmap | `git clone https://github.com/RustScan/RustScan.git` |
| **[ScamAdviser](https://www.scamadviser.com)** | 查网站可信度评分 | [scamadviser.com](https://www.scamadviser.com) |
| **[Scribd](https://www.scribd.com)** | 搜索文档、演示文稿、乐谱、电子书 | [scribd.com](https://www.scribd.com) |
| **[searchcode](https://searchcode.com)** | 搜索 GitHub/GitLab/Bitbucket 上 750 亿+ 行公开源码 | [searchcode.com](https://searchcode.com) |
| **Seeker** | 钓鱼式地理定位——通过 WebRTC + 浏览器定位收集精确 GPS | `git clone https://github.com/thewhiteh4t/seeker.git` |
| **[Shadowserver Dashboard](https://dashboard.shadowserver.org/)** | Shadowserver 基金会的全球网络威胁统计 | [dashboard.shadowserver.org](https://dashboard.shadowserver.org/) |
| **Sherloq** | 开源图像取证工具集 | `git clone https://github.com/GuidoBartoli/sherloq.git` |
| **Shodan CLI** | Shodan 官方命令行客户端 | `pip3 install shodan` |
| **[SlideShare](https://www.slideshare.net)** | 搜索公开的 PowerPoint/PDF 演示文稿 | [slideshare.net](https://www.slideshare.net) |
| **smap** | 基于 shodan.io 的 nmap 替代品 | `go install github.com/s0md3v/smap/cmd/smap@latest` |
| **[Snusbase API](https://snusbase.com/api)** | 泄露数据的 API 访问（付费） | [snusbase.com](https://snusbase.com/api) |
| **[SourceGraph](https://sourcegraph.com/search)** | 搜索数百万开源仓库的代码 | [sourcegraph.com](https://sourcegraph.com/search) |
| **[SpyCloud](https://spycloud.com)** | 账号接管防护 + 身份暴露数据 | [spycloud.com](https://spycloud.com) |
| **[Startpage](https://www.startpage.com)** | 隐私优先的搜索——无追踪的 Google 结果 | [startpage.com](https://www.startpage.com) |
| **[StealSeek](https://stealseek.io)** | 发现与分析数据泄露的搜索引擎 | [stealseek.io](https://stealseek.io) |
| **[SubredditStats](https://subredditstats.com)** | 版块用户重叠、增长与热门帖分析 | [subredditstats.com](https://subredditstats.com) |
| **[Telegago](https://cse.google.com/cse?cx=006368593537057042503:efxu7xprihg)** | 用于发现公开/私密 Telegram 频道的 Google CSE | [cse.google.com](https://cse.google.com/cse?cx=006368593537057042503:efxu7xprihg) |
| **Telegram Nearby Map** | 通过 OpenStreetMap 定位附近的 Telegram 用户 | `git clone https://github.com/tejado/telegram-nearby-map.git` |
| **[Telegram Search (lyzem.com)](https://lyzem.com)** | 搜索公开 Telegram 消息与频道 | [lyzem.com](https://lyzem.com) |
| **[Telemetr](https://telemetr.io)** | Telegram 频道/群组分析 | [telemetr.io](https://telemetr.io) |
| **Telerecon** | Telegram 调查侦察框架 | `git clone https://github.com/sockysec/Telerecon.git` |
| **[Teleteg](https://teleteg.com)** | Telegram 搜索引擎——10 条免费结果 | [teleteg.com](https://teleteg.com) |
| **[TGStat](https://tgstat.com)** | Telegram 频道分析——帖子数据、受众重叠 | [tgstat.com](https://tgstat.com) |
| **[The Hidden Wiki](https://thehiddenwiki.org)** | 暗网站点精选目录（依赖镜像） | [thehiddenwiki.org](https://thehiddenwiki.org) |
| **the-endorser** | 映射 LinkedIn 技能背书，勾勒人际关系 | `git clone https://github.com/eth0izzle/the-endorser.git` |
| **[TikTok Finder Country](https://tiktokfindercountry.xyz)** | 免费查询 TikTok 账号国家/语言 | [tiktokfindercountry.xyz](https://tiktokfindercountry.xyz) |
| **TorghostNG** | 通过 Tor 匿名化整个系统流量（Linux） | `git clone https://github.com/githacktools/TorghostNG.git` |
| **TOsint** | 从 Telegram 机器人与频道提取信息 | `git clone https://github.com/drego85/tosint.git` |
| **[Trace](https://trace.manus.space)** | 在 600+ 平台搜用户名、邮箱、电话，带风险评分 | [trace.manus.space](https://trace.manus.space) |
| **[Transit Visualisation Client](https://tracker.geops.ch)** | 700+ 城市实时公共交通 | [tracker.geops.ch](https://tracker.geops.ch) |
| **[Trends24](https://trends24.in)** | 各国 Twitter 热搜历史 | [trends24.in](https://trends24.in) |
| **[TRM Labs](https://www.trmlabs.com)** | 加密货币合规与调查平台 | [trmlabs.com](https://www.trmlabs.com) |
| **[TweetBinder](https://www.tweetbinder.com)** | Twitter/X 分析面板 | [tweetbinder.com](https://www.tweetbinder.com) |
| **[Twitch Search](https://www.twitch.tv/directory)** | 按分类、语言、观看数搜索直播 | [twitch.tv](https://www.twitch.tv/directory) |
| **[Twiteur](https://twiteur.com)** | Twitter/X 高级搜索封装——地理、日期、情感 | [twiteur.com](https://twiteur.com) |
| **[U-Find](https://u-find.com)** | Reddit 用户评论/发帖爬取器 | [u-find.com](https://u-find.com) |
| **uncover** | ProjectDiscovery——通过 Shodan/Censys/Fofa 快速发现暴露主机 | `go install github.com/projectdiscovery/uncover/cmd/uncover@latest` |
| **URLCrazy** | 生成域名误拼并检查可用性/注册情况 | `git clone https://github.com/urbanadventurer/urlcrazy.git` |
| **[URLhaus (abuse.ch)](https://urlhaus.abuse.ch)** | 恶意软件分发用恶意网址数据库 | [urlhaus.abuse.ch](https://urlhaus.abuse.ch) |
| **[User-Searcher](https://www.user-searcher.com)** | 在 2000+ 网站查用户名 | [user-searcher.com](https://www.user-searcher.com) |
| **[Vehicle Number Search Toolbox](https://cipher387.github.io/venicle_number_search_toolbox/)** | 一个页面搜 14 国车牌 | [cipher387.github.io](https://cipher387.github.io/venicle_number_search_toolbox/) |
| **[Venacus](https://venacus.com)** | 查询数据泄露并在中招时收到通知 | [venacus.com](https://venacus.com) |
| **[Vigilante.pw](https://vigilante.pw)** | 已拖库数据库索引（教育用途） | [vigilante.pw](https://vigilante.pw) |
| **[VMRay Analyzer](https://www.vmray.com)** | 恶意软件沙箱分析平台 | [vmray.com](https://www.vmray.com) |
| **[WalletExplorer](https://walletexplorer.com)** | 智能比特币区块浏览器——按实体聚类地址 | [walletexplorer.com](https://walletexplorer.com) |
| **waybackurls** | 拉取 Wayback Machine 收录的某域名全部 URL | `go install github.com/tomnomnom/waybackurls@latest` |
| **[Whoisology](https://whoisology.com)** | 反向 WHOIS——按注册人找域名 | [whoisology.com](https://whoisology.com) |
| **[Whoxy](https://www.whoxy.com)** | WHOIS 查询，带反向 WHOIS、历史记录与批量 API | [whoxy.com](https://www.whoxy.com) |
| **[Wikidata](https://www.wikidata.org)** | 维基百科结构化数据底座——SPARQL 查询 | [wikidata.org](https://www.wikidata.org) |
| **[Wikipedia](https://en.wikipedia.org)** | 免费百科全书——人物/地点调查的第一站 | [en.wikipedia.org](https://en.wikipedia.org) |
| **[WorldLicensePlates](http://www.worldlicenseplates.com)** | 按国家整理的车牌图形索引 | [worldlicenseplates.com](http://www.worldlicenseplates.com) |
| **XeuleDoc** | 无需登录获取 Google 文档/表格/幻灯片/绘图信息 | `pip3 install xeuledoc` |
| **[Yandex](https://www.yandex.com)** | 俄罗斯搜索引擎——反向图搜与西里尔文支持强 | [yandex.com](https://www.yandex.com) |
| **[YARAify](https://yaraify.abuse.ch/scan/)** | 协作式 YARA 引擎，通过文件特征匹配做开放威胁情报 | [yaraify.abuse.ch](https://yaraify.abuse.ch/scan/) |
| **[Yumpu](https://www.yumpu.com)** | 文档发布平台——有时经搜索泄露 | [yumpu.com](https://www.yumpu.com) |
| **[ZeroBounce](https://www.zerobounce.net)** | 邮箱有效性与可达性服务 | [zerobounce.net](https://www.zerobounce.net) |
| **ZoomEye CLI** | ZoomEye 网络资产搜索命令行客户端 | `pip3 install zoomeye` |

---

## 50. 🇬🇪 格鲁吉亚 OSINT 军火库（500+ 资源）

> 🇬🇪 面向格鲁吉亚（Sakartvelo）最全的 OSINT 资源合集。
>
> **28 sub-sections · 500+ verified resources** — government databases, public registries, investigative tools, open-data portals, Telegram bots & more.
>
> **实用建议：** 可搭配作者的 [Georgian-Wordlist](https://github.com/rawfilejson/Georgian-Wordlist)（76 万格鲁吉亚语词，供安全研究）与 [Wordlist-Generator](https://github.com/rawfilejson/Wordlist-Generator)。

> [!WARNING]
> **仅限教育与合法调查用途。** 请遵守格鲁吉亚《个人数据保护法》与 GDPR。作者不对任何滥用负责。

<details>
<summary><b>📋 点开查看完整格鲁吉亚 OSINT 军火库（28 个小节）</b></summary>

### 50.1 政府登记与电子政务门户

格鲁吉亚政府拥有后苏联空间里数字化程度最高的公共服务体系之一，多数服务都能通过集中式门户访问。
### 核心政府门户

| 资源 | 网址 | 说明 |
|---|---|---|
| my.gov.ge | [https://my.gov.ge](https://my.gov.ge) | 统一电子政务门户——出生/死亡证明、房产查询、工商登记、机构往来函件 |
| 格鲁吉亚政府 | [https://gov.ge](https://gov.ge) | 官方网站——新闻、部委、政策文件 |
| 格鲁吉亚议会 | [https://parliament.ge](https://parliament.ge) | 议会记录、法律、议员档案、委员会会议、投票记录 |
| 格鲁吉亚总统 | [https://president.gov.ge](https://president.gov.ge) | 总统令、赦免、人事任命、官方声明 |
| 司法部 | [https://justice.gov.ge](https://justice.gov.ge) | 司法系统信息、法律援助、公证服务 |
| 内务部（MIA） | [https://police.ge](https://police.ge) | 警方通报、通缉、犯罪统计、新闻稿 |
| 财政部 | [https://mof.gov.ge](https://mof.gov.ge) | 国家预算、财政数据、财报 |
| 外交部 | [https://mfa.gov.ge](https://mfa.gov.ge) | 外事信息、领事服务、国际协议 |
| 经济与可持续发展部 | [https://economy.ge](https://economy.ge) | 经济政策、贸易数据、投资环境 |
| 区域发展与基础设施部 | [https://mrdi.gov.ge](https://mrdi.gov.ge) | 基建项目与区域发展数据 |

### 公共登记与数据库

| 资源 | 网址 | 说明 |
|---|---|---|
| 国家公共登记局（NAPR） | [https://napr.gov.ge](https://napr.gov.ge) | 房产、工商与民事登记中枢——331 项服务 |
| Entrepreneur Registry | [https://enreg.reestri.gov.ge](https://enreg.reestri.gov.ge) | 检索任意企业——名称、注册号、注册日期、创始人、董事 |
| Property Registry | [https://napr.gov.ge/en/service/registers](https://napr.gov.ge/en/service/registers) | 按地籍码或所有人查不动产登记 |
| Civil Registry | [https://napr.gov.ge](https://napr.gov.ge) | 出生、婚姻、死亡、离婚记录（受限访问） |
| Revenue Service (RS) | [https://rs.ge](https://rs.ge) | 税号查询、海关数据、增值税门户、企业税务状态 |
| RS Taxpayer Search | [https://rs.ge/TaxPayer-en](https://rs.ge/TaxPayer-en) | 按姓名或税号查纳税人 |
| RS E-Services | [https://rs.ge/Eservices-en](https://rs.ge/Eservices-en) | 汽车/摩托税费、关税、房产税计算器 |
| Legislative Herald (Matsne) | [https://matsne.gov.ge](https://matsne.gov.ge) | 格鲁吉亚全部立法——法律、法令、法规、国际条约（全文） |
| National Archives | [https://archive.gov.ge](https://archive.gov.ge) | 历史文献、电子目录、数字化档案 |
| Service Development Agency (SDA) | [https://sda.gov.ge](https://sda.gov.ge) | 身份证、护照、居留许可、公民身份、个人数据服务 |
| Civil Service Bureau | [https://csb.gov.ge](https://csb.gov.ge) | 公职人员登记、人事政策、伦理、培训 |
| State Inspector | [https://dis.gov.ge](https://dis.gov.ge) | 个人数据保护机构、监控监督 |
| NSDI Geoportal | [https://nsdi.gov.ge](https://nsdi.gov.ge) | 国家空间数据基础设施——地块、地址、地籍图 |
| Data Exchange Agency (DEA) | [https://dea.gov.ge](https://dea.gov.ge) | 政府互联互通平台、电子公文交换 |
| National Food Agency | [https://nfa.gov.ge](https://nfa.gov.ge) | 食品安全登记、持证食品企业、检查结果 |
| National Environmental Agency | [https://nea.gov.ge](https://nea.gov.ge) | 环境监测数据、天气、地震数据 |
| Competition Agency | [https://competition.ge](https://competition.ge) | 市场集中度、并购决定、反垄断调查 |
| Insurance State Supervision | [https://insurance.gov.ge](https://insurance.gov.ge) | 持牌保险公司与监管数据 |
| National Wine Agency | [https://wine.gov.ge](https://wine.gov.ge) | 格鲁吉亚葡萄酒登记、产区数据、出口统计 |

### my.gov.ge 上对 OSINT 重要的服务

| Service | 你能查到什么 |
|---|---|
| Property Registry Search | 按地籍码查房产所有权 |
| Entrepreneur/Legal Entity Search | 工商注册状态、创始人、董事 |
| Birth/Death Certificates | （受限访问）人口档案核验 |
| 与政府机构往来的函件 | 向任意政府机构提交信息公开申请 |
| Tax Debt Information | 查个人欠税（有限开放） |
| Enforcement Cases | 查个人强制执行案件 |
| Notary Registry | 注册公证人与其业务 |

---
### 50.2 人物搜索与身份 OSINT

### 电话号码与身份查询

| 资源 | 网址 | 说明 | 免费/付费 |
|---|---|---|---|
| GetContact | [https://getcontact.com](https://getcontact.com) | 众包来电识别——看号码在别人手机里存成什么 | 免费增值 |
| TrueCaller | [https://truecaller.com](https://truecaller.com) | 来电识别与骚扰检测——格鲁吉亚号码支持好 | 免费增值 |
| Sync.me | [https://sync.me](https://sync.me) | 反向电话查询，匹配社交档案 | 免费 |
| NumBuster | [https://numbuster.com](https://numbuster.com) | 独联体国家常用的号码查询 | 免费 |
| Pipl | [https://pipl.com](https://pipl.com) | 深度人物搜索引擎，支持格鲁吉亚数据 | 付费 |
| Nomrebi (Phone Book) | [https://phonebookoftheworld.com/tbilisi/](https://phonebookoftheworld.com/tbilisi/) | Tbilisi White Pages / Yellow Pages | 免费 |
| 114 Directory | 用格鲁吉亚号码拨打 114 | 格鲁吉亚电话查号台 | 免费 |
| Eye of God（Глаз Бога 神之眼） | Telegram: @EyeOfGodBot | 面向独联体的查人：电话、姓名、车牌 | 付费 |
| Quick OSINT | Telegram: @QuickOSINT_bot | 跨独联体数据库查人 | 付费 |
| USSearcher | Telegram: @USSearcher_bot | 多数据库人物查询 | 付费 |

### 邮箱与用户名 OSINT

| 工具 | 网址 | 说明 |
|---|---|---|
| Hunter.io | [https://hunter.io](https://hunter.io) | 查找格鲁吉亚域名关联的邮箱 |
| EmailRep | [https://emailrep.io](https://emailrep.io) | 邮箱信誉与泄露暴露检查 |
| Have I Been Pwned | [https://haveibeenpwned.com](https://haveibeenpwned.com) | 查格鲁吉亚邮箱是否出现在数据泄露中 |
| Epieos | [https://epieos.com](https://epieos.com) | 邮箱 OSINT——Google ID、关联账号、头像 |
| Holehe | [https://github.com/megadose/holehe](https://github.com/megadose/holehe) | 查邮箱注册过哪些平台 |
| Sherlock | [https://github.com/sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) | 400+ 社交平台的用户名搜索 |
| Maigret | [https://github.com/soxoj/maigret](https://github.com/soxoj/maigret) | 覆盖 2500+ 网站的高级用户名搜索 |
| WhatsMyName | [https://whatsmyname.app](https://whatsmyname.app) | 数百个网站的用户名枚举 |

### 格鲁吉亚专属人物搜索

| Method | Details |
|---|---|
| Facebook（格鲁吉亚用户） | 约 250 万格鲁吉亚用户。支持格鲁吉亚文姓名搜索，不少档案直接可见电话号码 |
| VK.com | 在讲俄语的格鲁吉亚人与被占领土流行 |
| OK.ru（同学网） | 在格鲁吉亚年长人群流行 |
| Instagram | 在格鲁吉亚很流行，尤其 18-35 岁 |
| LinkedIn | 职业档案，尤其适合商业调查 |
| Google Search | `"name surname" site:facebook.com/` or `"name" "+995"` |

---
### 50.3 公司与商业情报

### 主要工商登记

| 资源 | 网址 | 说明 |
|---|---|---|
| Entrepreneur Registry (NAPR) | [https://enreg.reestri.gov.ge](https://enreg.reestri.gov.ge) | 官方企业检索——名称、注册号、组织形式、状态、创始人、董事、地址 |
| RS Taxpayer Portal | [https://rs.ge/TaxPayer-en](https://rs.ge/TaxPayer-en) | 税号查询、经营状态 |
| OpenCorporates (Georgia) | [https://opencorporates.com/companies/ge](https://opencorporates.com/companies/ge) | 含格鲁吉亚公司的国际企业检索 |
| OpenSanctions (Georgian Registry) | [https://opensanctions.org/datasets/ext_ge_company_registry/](https://opensanctions.org/datasets/ext_ge_company_registry/) | 结构化的格鲁吉亚公司数据 |

### 金融与投资数据

| 资源 | 网址 | 说明 |
|---|---|---|
| 格鲁吉亚国家银行（NBG） | [https://nbg.gov.ge](https://nbg.gov.ge) | 银行业监管、汇率、金融统计、反洗钱制裁 |
| NBG AML/CFT Sanctions | [https://nbg.gov.ge/en/supervision/aml-cft](https://nbg.gov.ge/en/supervision/aml-cft) | 金融机构反洗钱违规的罚单与制裁 |
| Financial Monitoring Service (FMS) | [https://fms.gov.ge](https://fms.gov.ge) | 格鲁吉亚金融情报机构——可疑交易报告 |
| Georgian Stock Exchange | [https://gse.ge](https://gse.ge) | 上市公司、股票数据、财务披露 |
| GITA (Innovation & Tech Agency) | [https://gita.gov.ge](https://gita.gov.ge) | 科技公司资助、创业生态数据 |

### 公司尽职调查

| 数据点 | 怎么查 |
|---|---|
| Company Name & ID | enreg.reestri.gov.ge——按姓名或 9/11 位注册号检索 |
| Directors & Founders | NAPR 提取——显示现任与历任董事 |
| Tax Status | rs.ge——查公司是否正常纳税 |
| Property Owned | NAPR 房产登记——按公司名检索 |
| Procurement Contracts | tenders.procurement.gov.ge——按供应商名检索 |
| Court Cases | ecd.court.ge——按公司名或 ID 检索 |
| Sanctions | opensanctions.org——与国际制裁名单交叉比对 |
| International Connections | OpenCorporates——跨辖区关联实体 |

---
### 50.4 法律与法院记录

### 法院数据库

| 资源 | 网址 | 说明 |
|---|---|---|
| Unified Court Decisions Database | [https://ecd.court.ge](https://ecd.court.ge) | 检索三级法院判决（注：2020 年 4 月后的判决可能不公开） |
| Court Decisions Search | [https://ecd.court.ge/Decision](https://ecd.court.ge/Decision) | 按案号、日期、法院、类别检索 |
| Court Acts / Final Documents | [https://ecd.court.ge/FinalDocument](https://ecd.court.ge/FinalDocument) | 按文书条码或案号检索 |
| Public Notifications | [https://ecd.court.ge/PublicNotification](https://ecd.court.ge/PublicNotification) | 法院公告——可用于找当事人 |
| Current Cases & Hearings | [https://ecd.court.ge/CurrentCase](https://ecd.court.ge/CurrentCase) | 在办案件，含开庭日期与法官 |
| E-Court Portal | [https://ecourt.ge](https://ecourt.ge) | 电子法院立案系统（需注册） |
| 格鲁吉亚最高法院 | [https://supremecourt.ge](https://supremecourt.ge) | 最高法院判决、实践与抗诉裁定 |
| Constitutional Court | [https://constcourt.ge](https://constcourt.ge) | 宪法法院判决与申诉 |
| CourtWatch.ge | [https://courtwatch.ge](https://courtwatch.ge) | 独立法院监督与司法分析 |

### 重要法律资源

| 资源 | 网址 | 说明 |
|---|---|---|
| Matsne (Legislative Herald) | [https://matsne.gov.ge](https://matsne.gov.ge) | 格鲁吉亚全部法律全文——可检索数据库 |
| Criminal Code of Georgia | [https://matsne.gov.ge/en/document/view/16426](https://matsne.gov.ge/en/document/view/16426) | 刑法典全文 |
| Civil Code of Georgia | [https://matsne.gov.ge/en/document/view/31702](https://matsne.gov.ge/en/document/view/31702) | 民法典全文 |
| Georgian Bar Association | [https://gba.ge](https://gba.ge) | 律师名录、纪律处分程序 |
| GYLA (Georgian Young Lawyers) | [https://gyla.ge](https://gyla.ge) | 法律分析、人权报告、选举监督 |
| Prosecutor's Office | [https://pog.gov.ge](https://pog.gov.ge) | 检察数据、要案、统计 |
| Probation Bureau | [https://probation.moj.gov.ge](https://probation.moj.gov.ge) | 缓刑数据与罪犯监管 |
| Ombudsman (Public Defender) | [https://ombudsman.ge](https://ombudsman.ge) | 人权报告、申诉、建议 |

### 法院记录检索——技巧

```
1. Go to ecd.court.ge/Decision
2. Select court instance (First Instance / Appeals / Cassation)
3. Select court name (e.g., Tbilisi City Court)
4. Select case category (Civil / Criminal / Administrative)
### 50.5 输入案号或日期范围

### 50.6 注意：公开判决中的个人数据已匿名化

### 50.7 2020 年 4 月后的案件——很多不上网公开

```
5. 房产与不动产 OSINT
### 房产登记

| 资源 | 网址 | 说明 |
|---|---|---|
| NAPR Property Registry | [https://napr.gov.ge](https://napr.gov.ge) | 官方不动产登记——所有权、抵押、权利负担 |
| NAPR Extract Service | [https://napr.gov.ge/en/service/information-services/extract-public-register](https://napr.gov.ge/en/service/information-services/extract-public-register) | 订购官方房产摘录（付费） |
| NSDI Geoportal | [https://nsdi.gov.ge](https://nsdi.gov.ge) | 带地籍边界、地块、地址的交互地图 |
| my.gov.ge 房产查询 | [https://my.gov.ge](https://my.gov.ge) | 查房产登记申请 |

### 房产门户（OSINT 金矿）

| Portal | 网址 | 说明 |
|---|---|---|
| SS.GE (Home) | [https://home.ss.ge](https://home.ss.ge) | 格鲁吉亚最大分类站——公寓、住宅、商铺（含照片、价格、业主联系方式） |
| MyHome.ge | [https://myhome.ge](https://myhome.ge) | 主要房产门户，房源详尽、含中介联系方式 |
| Livo.ge | [https://livo.ge](https://livo.ge) | 房产平台——3D 看房、拍卖、估价工具 |
| Home.ge | [https://home.ge](https://home.ge) | 买卖租房源齐全的房产门户 |
| Korter.ge | [https://korter.ge](https://korter.ge) | 新房与公寓搜索平台 |
| TbilisiHome.ge | [https://tbilisihome.ge](https://tbilisihome.ge) | 第比利斯房源 |
| HomeSearch.ge | [https://homesearch.ge](https://homesearch.ge) | 多语言房产搜索平台 |
| Gavel.ge | [https://gavel.ge](https://gavel.ge) | 聚合 Livo、eAuction.ge、第比利斯市政的房产拍卖 |

### 房产 OSINT 流程

```
1. Get person's name or company ID
2. Search NAPR (napr.gov.ge) for registered properties
3. Cross-reference with ss.ge/myhome.ge for listings (may show photos, addresses)
4. Check nsdi.gov.ge for cadastral boundaries and neighbors
5. Search eauction.ge for any auctioned/seized properties
6. Check ecd.court.ge for property-related litigation
```
6. Vehicle & Transport OSINT
### 车辆数据库

| 资源 | 网址 | 说明 |
|---|---|---|
| RS Auto/Moto Levy Calculator | [https://rs.ge/Eservices-en](https://rs.ge/Eservices-en) | 按车辆信息计算税费 |
| MyAuto.ge | [https://myauto.ge](https://myauto.ge) | 格鲁吉亚最大车辆市场——VIN 查询、Carfax 报告、发布历史 |
| MyAuto VIN Check | [https://myauto.ge/en/vin](https://myauto.ge/en/vin) | 按 VIN 查车辆历史（Carfax 与 ClearVin） |
| AutoPapa.ge | [https://autopapa.ge](https://autopapa.ge) | 美国拍卖进口车——车辆历史、照片、损伤报告 |
| Myparts.ge | [https://myparts.ge](https://myparts.ge) | 汽配市场——可用于识别车辆 |
| SS.GE (Auto) | [https://auto.ss.ge](https://auto.ss.ge) | 车辆分类信息，规格详尽、含车主联系方式 |
| EverCar.ge | [https://evercar.ge](https://evercar.ge) | 带进口历史的车辆市场 |

### 交通管理部门数据

| 资源 | 网址 | 说明 |
|---|---|---|
| Service Development Agency (SDA) | [https://sda.gov.ge](https://sda.gov.ge) | 车辆登记、驾照、年检数据 |
| Tbilisi City Hall Transport | [https://tbilisi.gov.ge](https://tbilisi.gov.ge) | 城市交通数据、停车、路况 |
| Georgian Railway | [https://railway.ge](https://railway.ge) | 铁路运输数据与时刻表 |


| Georgian Airports | https://tbilisiairport.com | 航班数据与旅客统计 |
|---|---|---|
| MIA Traffic Police | [https://patrol.gov.ge](https://patrol.gov.ge) | 交通违法数据与事故报告 |

### 格鲁吉亚车牌格式

```
### 格鲁吉亚车牌遵循以下格式：

- Standard: AA-123-AA (two letters, three numbers, two letters)
- Government: GOV followed by numbers
- Diplomatic: D followed by numbers
- Military: GEO followed by numbers
- Regional codes vary by area

### 注意：格鲁吉亚车牌使用拉丁字母

```
7. Financial Intelligence & Banking
### 国家银行与金融监管机构

| 资源 | 网址 | 说明 |
|---|---|---|
| 格鲁吉亚国家银行（NBG） | [https://nbg.gov.ge](https://nbg.gov.ge) | 央行——汇率、银行统计、监管数据 |
| NBG Exchange Rates | [https://nbg.gov.ge/en/monetary-policy/currency](https://nbg.gov.ge/en/monetary-policy/currency) | 官方拉里汇率（含历史数据） |
| NBG Banking Supervision | [https://nbg.gov.ge/en/supervision](https://nbg.gov.ge/en/supervision) | 银行财务数据、监管措施、持牌机构 |
| NBG AML Sanctions | [https://nbg.gov.ge/en/supervision/aml-cft](https://nbg.gov.ge/en/supervision/aml-cft) | 银行/机构反洗钱违规罚款（名单、金额、原因） |
| Financial Monitoring Service | [https://fms.gov.ge](https://fms.gov.ge) | 格鲁吉亚金融情报机构——反洗钱情报 |
| Competition & Consumer Protection | [https://competition.ge](https://competition.ge) | 市场集中度、并购、消费者投诉 |

### 银行与金融机构

| Institution | 网址 | 说明 |
|---|---|---|
| Bank of Georgia | [https://bankofgeorgia.ge](https://bankofgeorgia.ge) | 最大银行——财报、股东数据 |
| TBC Bank | [https://tbcbank.ge](https://tbcbank.ge) | 第二大银行——公开财务披露 |
| Liberty Bank | [https://libertybank.ge](https://libertybank.ge) | 零售银行 |
| Basis Bank | [https://basisbank.ge](https://basisbank.ge) | 投资银行 |
| Credo Bank | [https://credobank.ge](https://credobank.ge) | 区域性银行 |
| ProCredit Bank | [https://procreditbank.ge](https://procreditbank.ge) | 中小企业银行 |
| Finca Bank | [https://finca.ge](https://finca.ge) | 小微金融银行 |
| Crystal | [https://crystal.ge](https://crystal.ge) | 小额信贷机构 |

### 金融 OSINT 检索

| Query | 你能查到什么 |
|---|---|
| 公司名 + rs.ge 税务 | 税务状态、注册信息、欠税 |
| 人名 + 央行制裁库 | 是否列入反洗钱制裁 |
| 公司名 + opensanctions.org | 国际制裁交叉比对 |
| 公司名 + 离岸泄露库 | ICIJ 离岸泄露数据库——格鲁吉亚实体 |
| 公司名 + 采购平台 | 中标政府合同 |

---
### 50.8 选举与政治数据

### 中央选举委员会（CEC）

| 资源 | 网址 | 说明 |
|---|---|---|
| CEC of Georgia (CESKO) | [https://cesko.ge](https://cesko.ge) | 官方选举机构——选民数据、结果、法规 |
| CEC Election Results | [https://cesko.ge](https://cesko.ge) (results section) | 选区、地区、党派细分结果——2008 年以来全部选举 |
| CEC Voter Information | [https://cesko.ge/en/amomrchevlebi](https://cesko.ge/en/amomrchevlebi) | 选民登记核验门户 |
| CEC Annual Reports | [https://cesko.ge](https://cesko.ge) (publications) | 年度报告，含详细选举统计 |

### 政治数据来源

| 资源 | 网址 | 说明 |
|---|---|---|
| 格鲁吉亚议会 | [https://parliament.ge](https://parliament.ge) | 议员档案、投票记录、委员会职务、法案追踪 |
| Political Party Registry | [https://cesko.ge](https://cesko.ge) (parties section) | 注册政党、财务披露、领导层 |
| ISFED (Election Monitoring) | [https://isfed.ge](https://isfed.ge) | 独立选举观察报告与违规数据库 |
| Transparency International Georgia | [https://transparency.ge](https://transparency.ge) | 政治献金监控与腐败调查 |
| Civil Georgia | [https://civil.ge](https://civil.ge) | 独立新闻，政治分析深入 |
| CRRC Georgia | [https://crrc.ge](https://crrc.ge) | 高加索研究资源中心——民意调查与政治民调 |
| IPU Georgia | [https://data.ipu.org/parliament/GE](https://data.ipu.org/parliament/GE) | 各国议会联盟——格鲁吉亚议会数据 |
| NDI Georgia | [https://ndi.org/georgia](https://ndi.org/georgia) | 美国全国民主研究所——政治项目数据 |

2024 年格鲁吉亚议会选举数据
| 数据点 | Source |
|---|---|
| Official Results | cesko.ge——完整选区级数据 |
| Analysis & Claims | civil.ge/archives/631386 |
| ISFED Reports | isfed.ge——实时平行计票 |
| International Observers | 欧安组织/民主制度与人权办公室报告 |
| Wikipedia Overview | en.wikipedia.org/wiki/2024_Georgian_parliamentary_election |

---
### 50.9 地图与地理空间情报

### 格鲁吉亚地图服务

| 资源 | 网址 | 说明 |
|---|---|---|
| NSDI Geoportal | [https://nsdi.gov.ge](https://nsdi.gov.ge) | 国家空间数据基础设施——地籍图、地块、地址 |
| Google Maps (Georgia) | [https://maps.google.com](https://maps.google.com) | 格鲁吉亚街景覆盖、卫星影像、商户信息 |
| Yandex Maps (Georgia) | [https://yandex.com/maps/?ll=44.78,41.69](https://yandex.com/maps/?ll=44.78,41.69) | 替代地图服务，卫星影像不同，带俄语数据 |
| OpenStreetMap Georgia | [https://www.openstreetmap.org/#map=8/42.0/43.5](https://www.openstreetmap.org/#map=8/42.0/43.5) | 社区维护地图，格鲁吉亚测绘详尽 |
| Wikimapia | [https://wikimapia.org/#lang=en&lat=41.7&lon=44.8](https://wikimapia.org/#lang=en&lat=41.7&lon=44.8) | 用户标注卫星影像——识别无标注建筑有用 |
| Sentinel Hub (Copernicus) | [https://scihub.copernicus.eu](https://scihub.copernicus.eu) | 格鲁吉亚免费卫星影像（欧盟哥白尼计划） |
| Google Earth | [https://earth.google.com](https://earth.google.com) | 可回溯到 2000 年代初的格鲁吉亚历史卫星影像 |
| Mapillary | [https://www.mapillary.com](https://www.mapillary.com) | 众包街景——格鲁吉亚部分覆盖 |

### GIS 数据源

| 资源 | 网址 | 说明 |
|---|---|---|
| NAPR GIS | [https://nsdi.gov.ge](https://nsdi.gov.ge) | 地籍数据、行政边界、地址登记 |
| NEA (Environmental Agency) | [https://nea.gov.ge](https://nea.gov.ge) | 环境监测站、地震数据、气象站 |
| Geostat GIS Data | [https://geostat.ge](https://geostat.ge) | 普查地图、分地区人口分布 |
| Tbilisi Municipality GIS | [https://tbilisi.gov.ge](https://tbilisi.gov.ge) | 城市规划、分区、基础设施地图 |

### 格鲁吉亚地理定位技巧

```
### 格鲁吉亚影像地理定位的关键视觉标识：

- Georgian script (mkhedruli) on signs -- unique alphabet
- Mountain terrain (Caucasus) with distinctive tower-houses in Svaneti/Tusheti
- Soviet-era apartment blocks (khrushchyovka) in cities
- Distinctive church architecture (Georgian Orthodox cross-dome style)
- License plates: AA-123-AA format
- Phone prefix: +995
- Currency: GEL (Georgian Lari) -- prices on signs
- Bilingual signs (Georgian + English) in Tbilisi
- Unique tower-houses in mountainous regions (Svaneti, Tusheti, Khevsureti)
```
### 50.10 媒体版图与新闻 OSINT

### 格鲁吉亚主要新闻来源

| Source | 网址 | Language | Orientation |
|---|---|---|---|
| Civil Georgia | [https://civil.ge](https://civil.ge) | EN/GE | 独立、亲西方 |
| Interpressnews | [https://interpressnews.ge](https://interpressnews.ge) | GE/EN | 通讯社 |
| Agenda.ge | [https://agenda.ge](https://agenda.ge) | EN | 官方背景（政府出资） |
| Georgia Today | [https://georgiatoday.ge](https://georgiatoday.ge) | EN | 独立英文媒体 |
| OC Media | [https://oc-media.org](https://oc-media.org) | EN | 独立的高加索全区域媒体 |
| JAM News | [https://jam-news.net](https://jam-news.net) | EN/GE/RU/AZ/AM | 地方通讯社 |
| Netgazeti | [https://netgazeti.ge](https://netgazeti.ge) | GE | 独立数字媒体 |
| Publika | [https://publika.ge](https://publika.ge) | GE | Independent |
| Tabula | [https://tabula.ge](https://tabula.ge) | GE | Liberal |
| Liberali | [https://liberali.ge](https://liberali.ge) | GE | Liberal |
| BMG (Business Media Georgia) | [https://bm.ge](https://bm.ge) | GE/EN | 商业新闻 |
| Forbes Georgia | [https://forbes.ge](https://forbes.ge) | GE/EN | Business |
| Commersant.ge | [https://commersant.ge](https://commersant.ge) | GE | Business |

### Television & Radio

| Channel | 网址 | Notes |
|---|---|---|
| Georgian Public Broadcaster (GPB) | [https://1tv.ge](https://1tv.ge) | 国家公共广播机构 |
| Rustavi 2 | [https://rustavi2.ge](https://rustavi2.ge) | 亲政府（所有权已变更） |
| Imedi TV | [https://imedinews.ge](https://imedinews.ge) | 亲政府 |
| Mtavari Arkhi | [https://mtavari.tv](https://mtavari.tv) | 倾向反对派 |
| TV Pirveli | [https://tvpirveli.ge](https://tvpirveli.ge) | Independent |
| Formula TV | [https://formulanews.ge](https://formulanews.ge) | Independent |
| Kavkasia TV | [https://kavkasia.ge](https://kavkasia.ge) | Independent |
| Radio Tavisupleba (RFE/RL) | [https://radiotavisupleba.ge](https://radiotavisupleba.ge) | 自由电台格鲁吉亚语服务 |
| 美国之音格鲁吉亚语频道 | [https://amerikiskhma.com](https://amerikiskhma.com) | 美国之音格鲁吉亚语服务 |

### 调查报道

| Organization | 网址 | 说明 |
|---|---|---|
| Transparency International Georgia | [https://transparency.ge](https://transparency.ge) | 反腐调查、资产监控、政治献金 |
| IDFI | [https://idfi.ge](https://idfi.ge) | 信息自由、公共数据获取、信息公开申请 |
| Studio Monitor | [https://studiomonitori.ge](https://studiomonitori.ge) | 调查报道 |
| Batumelebi | [https://batumelebi.netgazeti.ge](https://batumelebi.netgazeti.ge) | 阿扎尔专题调查 |
| CATAGI | [https://catagi.ge](https://catagi.ge) | 分析研究与权力结构调查 |
| Who Owned Georgia (TI) | [https://transparency.ge](https://transparency.ge) | 商业与媒体所有权研究 |

---
### 50.11 数据泄露库

### 格鲁吉亚重大数据泄露事件

| Incident | Year | Records | Details | Sources |
|---|---|---|---|---|
| 4.9 Million Citizens Leak | 2020 | 4,934,863 | 全名、生日、性别、身份证号、手机号——发布于黑客论坛的 1.04GB Microsoft Access 文件 | ZDNet |
| Ghost Database (Cybernews) | 2025 | 约 700 万 | 个人记录出现在德国云服务商——未设防后消失。含全名、生日、性别、身份证号、手机号 | Cybernews |
| CEC Voter Database | 2020 | 约 350 万 | 与 2020 年泄露事件关联的选民登记数据 | OC Media |

### 泄露查询工具（查格鲁吉亚数据）

| 工具 | 网址 | 说明 | 免费/付费 |
|---|---|---|---|
| Have I Been Pwned | [https://haveibeenpwned.com](https://haveibeenpwned.com) | 查邮箱在已知泄露中的暴露 | 免费 |
| LeakCheck | [https://leakcheck.io](https://leakcheck.io) | 按邮箱、电话、用户名搜——含独联体数据 | 免费增值 |
| DeHashed | [https://dehashed.com](https://dehashed.com) | 按姓名、邮箱、电话、IP 搜泄露库 | 付费 |
| IntelX | [https://intelx.io](https://intelx.io) | 情报搜索引擎——粘贴站、泄露、暗网 | 免费增值 |
| Snusbase | [https://snusbase.com](https://snusbase.com) | 泄露数据库查询 | 付费 |
| BreachDirectory | [https://breachdirectory.org](https://breachdirectory.org) | 密码哈希部分查询 | 免费 |
| Hudson Rock Cavalier | [https://cavalier.hudsonrock.com](https://cavalier.hudsonrock.com) | 信息窃取木马数据——已泄露凭据 | 有免费档 |
| CheckLeaked | [https://checkleaked.cc](https://checkleaked.cc) | 泄露数据查询，含 WhatsApp 泄露 | 付费 |
| Leak-Lookup | [https://leak-lookup.com](https://leak-lookup.com) | 多数据库泄露查询 | 付费 |
| h8mail | [https://github.com/khast3x/h8mail](https://github.com/khast3x/h8mail) | 邮箱泄露狩猎命令行工具 | Free (OSS) |

### 重要背景

```
The 2020 Georgian data leak is one of the largest per-capita data breaches ever:
- 4.9 million records from a country of ~3.7 million living citizens
- Includes deceased citizens' records
- Originally suspected to be a CEC voter database leak
- Data was published on a hacking forum over a weekend
- Georgian authorities investigated but never publicly identified the source
- The 2025 "ghost database" on a German cloud provider may be related

### 影响：格鲁吉亚个人数据（姓名、生日、身份证号、电话）

circulates on multiple forums and breach databases.
```
### 50.12 电话与电信 OSINT

### 格鲁吉亚移动运营商

| Operator | 网址 | Market Share | Network |
|---|---|---|---|
| MagtiCom | [https://magticom.ge](https://magticom.ge) | ~40% | 2G/3G/4G/5G——覆盖最好 |
| Silknet（原 Geocell） | [https://silknet.com](https://silknet.com) | ~35% | 2G/3G/4G/5G |
| Cellfie（原 Beeline） | [https://cellfie.ge](https://cellfie.ge) | ~25% | 2G/3G/4G/5G |

### 格鲁吉亚手机号格式

```
### 国家区号：+995

### 格式：+995 XXX XXX XXX（国家码后 9 位）


### 手机号段：

- 5XX: Mobile numbers (all operators)
  - 555, 557, 558: MagtiCom
  - 551, 571, 574, 577, 578: Silknet
  - 568, 591, 592, 593, 595, 596, 597, 598, 599: Various

### 固话区号：

- 32: Tbilisi
- 422: Batumi (Ajara)
- 431: Kutaisi (Imereti)
- 352: Rustavi
- 370: Gori
- 495: Zugdidi (Samegrelo)

### 紧急电话：112（通用）

### Directory: 114

```
### 格鲁吉亚号码的电话 OSINT 技巧

| Technique | Tool/Method | 说明 |
|---|---|---|
| Caller ID Lookup | GetContact / TrueCaller | 看号码在别人手机里存成什么 |
| WhatsApp Check | WhatsApp 应用 | 查号码是否注册 WhatsApp——头像、签名、最后在线 |
| Telegram Check | Telegram 应用 | 按手机号搜——用户名、头像、简介 |
| Viber Check | Viber 应用 | 格鲁吉亚很流行——记得查档案信息 |
| Google Search | `"+995XXXXXXXXX"` | 查号码在网上出现的位置（广告、论坛、社媒） |
| Facebook Reverse | 按手机号搜 Facebook | 找手机号关联的 Facebook 账号 |
| HIBP / LeakCheck | haveibeenpwned.com / leakcheck.io | 查手机号是否出现在泄露库 |

---
### 50.13 社交媒体与平台 OSINT

### 格鲁吉亚社交媒体版图

| Platform | 格鲁吉亚用户数（估） | OSINT Value | Notes |
|---|---|---|---|
| Facebook | 约 250 万 | Very High | 格鲁吉亚第一大社交平台。大量档案公开，电话号码直接可见 |
| Instagram | 约 150 万 | High | 18-35 岁主流，第比利斯尤甚 |
| TikTok | 约 100 万 | Medium | 增长迅速，尤其年轻用户 |
| YouTube | 约 200 万 | High | 格鲁吉亚内容创作者、新闻频道、调查节目 |
| Telegram | 约 150 万 | Very High | 新闻频道、政治群组、爆料频道、机器人 |
| Twitter/X | ~200K | Medium | 记者、政界、NGO 在用 |
| LinkedIn | ~300K | Medium | 职业档案、商业情报 |
| VK.com | ~150K | Medium | 讲俄语的格鲁吉亚人、阿布哈兹/南奥塞梯 |
| OK.ru | ~100K | Low | 偏年长用户 |
| Reddit r/Sakartvelo | ~100K | Low | 讲英语的格鲁吉亚社区 |

### 格鲁吉亚 Facebook OSINT

```
Facebook is the #1 OSINT source for Georgian individuals:

### 搜索技巧：

1. Search by name in Georgian script: "გიორგი" "ბერიძე"
2. Search by phone: Enter +995XXXXXXXXX in Facebook search
3. Search by workplace: "Bank of Georgia" employees
4. Search by school: "Tbilisi State University" graduates
5. Search by location: People in "Tbilisi"
6. Use Facebook Graph Search remnants via Google:
   site:facebook.com "name" "lives in Tbilisi"
7. Check "People You May Know" from a Georgian account
8. Many Georgian users have public profiles with:
   - Phone numbers in About section
   - Workplace history
   - Education history
   - Family relationships
   - Check-in locations
```
### 平台专用工具

| 工具 | 网址 | 说明 |
|---|---|---|
| Facebook Search | [https://facebook.com/search](https://facebook.com/search) | 自带过滤的原生搜索 |
| Who Posted What | [https://whopostedwhat.com](https://whopostedwhat.com) | 按日期的 Facebook 关键词搜索 |
| Social Searcher | [https://social-searcher.com](https://social-searcher.com) | 免费社交媒体搜索引擎 |
| SocialBlade | [https://socialblade.com](https://socialblade.com) | YouTube/Instagram/Twitter 账号数据统计 |
| Twint | [https://github.com/twintproject/twint](https://github.com/twintproject/twint) | Twitter 爬虫（已归档） |
| Instaloader | [https://github.com/instaloader/instaloader](https://github.com/instaloader/instaloader) | Instagram 主页与帖子下载器 |
| TikTok Scraper | [https://github.com/drawrowfly/tiktok-scraper](https://github.com/drawrowfly/tiktok-scraper) | TikTok 数据提取 |

---
### 50.14 开放数据与统计门户

### 国家统计

| 资源 | 网址 | 说明 |
|---|---|---|
| GeoStat (National Statistics Office) | [https://geostat.ge](https://geostat.ge) | 格鲁吉亚官方统计——人口、经济、贸易、犯罪、卫生、教育 |
| GeoStat Database | [https://geostat.ge/ka/modules/categories/858/monatsemta-baza](https://geostat.ge/ka/modules/categories/858/monatsemta-baza) | 可下载的统计数据库 |
| Census 2024 | [https://census2024.geostat.ge](https://census2024.geostat.ge) | 2024 年人口与农业普查数据 |
| Census 2014 Results | [https://geostat.ge/en/modules/categories/735/population-census](https://geostat.ge/en/modules/categories/735/population-census) | 历次普查结果，人口结构细分 |

### 开放数据门户

| 资源 | 网址 | 说明 |
|---|---|---|
| data.gov.ge | [https://data.gov.ge](https://data.gov.ge) | 格鲁吉亚开放数据门户——机器可读的政府数据集 |
| OpenData SPA | [https://opendata.spa.ge](https://opendata.spa.ge) | OCDS 格式开放采购数据（2011 至今） |
| OGP Georgia | [https://ogpgeorgia.gov.ge](https://ogpgeorgia.gov.ge) | 开放政府伙伴关系——透明度承诺与进展 |
| IDFI Public Information Database | [https://idfi.ge](https://idfi.ge) | 信息公开申请与答复数据库 |
| World Bank Georgia | [https://data.worldbank.org/country/georgia](https://data.worldbank.org/country/georgia) | 世界银行格鲁吉亚发展指标 |
| UN Data Georgia | [https://data.un.org](https://data.un.org) | 联合国格鲁吉亚统计 |
| OECD Georgia | [https://data.oecd.org](https://data.oecd.org) (search Georgia) | 经济与社会指标 |
| IMF Georgia | [https://imf.org/en/Countries/GEO](https://imf.org/en/Countries/GEO) | IMF 经济评估与数据 |

### 重点统计数据集

| Dataset | URL/Source | Contents |
|---|---|---|
| 分地区人口 | geostat.ge | 按市镇、年龄、性别的人口数 |
| Crime Statistics | geostat.ge | 按类型、地区、年份的犯罪数据 |
| Economic Data | geostat.ge | GDP、通胀、贸易、就业 |
| Education Statistics | geostat.ge | 分地区学校、学生、大学数据 |
| Health Statistics | geostat.ge + ncdc.ge | 发病率、死亡率、医疗机构 |
| Tourism Statistics | gnta.ge | 分国家游客量与消费数据 |

---
### 50.15 政府采购与公共支出

### 采购平台

| 资源 | 网址 | 说明 |
|---|---|---|
| State Procurement Agency (SPA) | [https://procurement.gov.ge](https://procurement.gov.ge) | 格鲁吉亚统一电子采购系统 |
| Tenders Portal | [https://tenders.procurement.gov.ge](https://tenders.procurement.gov.ge) | 检索浏览全部政府招标——在招与历史 |
| OpenData SPA (OCDS) | [https://opendata.spa.ge](https://opendata.spa.ge) | 2011 年以来全部采购数据，开放签约数据标准（OCDS）格式 |
| OCDS API | [https://odapi.spa.ge](https://odapi.spa.ge) | 采购数据的 API 访问 |
| Global Public Procurement (Georgia) | [https://globalpublicprocurementdata.org/gppd/country_profile/GE](https://globalpublicprocurementdata.org/gppd/country_profile/GE) | 格鲁吉亚采购的全球视角画像 |

### 你能查到什么

```
Georgia's procurement system is considered one of the most transparent in Europe/Central Asia:

### Searchable by:

- Contracting organization name
- Supplier/vendor name
- Tender number
- Contract value range
- Procurement type (electronic tender, simplified, consolidated)
- Date range
- CPV code (product/service category)

### 可用数据：

- Full tender documents
- Bid submissions and bidder names
- Contract awards with prices
- Subcontractor information
- Procurement plans
- Complaint/dispute records
```
### 预算透明

| 资源 | 网址 | 说明 |
|---|---|---|
| 财政部预算 | [https://mof.gov.ge](https://mof.gov.ge) | 国家预算文件与执行报告 |
| Budget.ge | [https://budget.ge](https://budget.ge) | 交互式预算可视化工具 |
| BOOST Georgia (World Bank) | [https://boost.worldbank.org](https://boost.worldbank.org) | 详细预算支出数据 |
| State Audit Office | [https://sao.ge](https://sao.ge) | 政府审计报告、财务合规 |

---
### 50.16 域名、IP 与网络情报

.GE Domain Intelligence
| 资源 | 网址 | 说明 |
|---|---|---|
| NIC.GE (Registry) | [https://nic.ge](https://nic.ge) | 格鲁吉亚域名注册局——.ge 顶级域管理 |
| NIC.GE WHOIS | [https://nic.ge/en/domains/whois](https://nic.ge/en/domains/whois) | .ge 域名官方 WHOIS 查询 |
| DomainTools .GE | [https://research.domaintools.com/statistics/tldpedia/ge](https://research.domaintools.com/statistics/tldpedia/ge) | .GE 顶级域统计数据 |
| SecurityTrails | [https://securitytrails.com](https://securitytrails.com) | .ge 站点的 DNS 历史、子域名、关联域名 |
| crt.sh | [https://crt.sh](https://crt.sh) | 证书透明度日志——发现 .ge 站点子域名 |
| DNSDumpster | [https://dnsdumpster.com](https://dnsdumpster.com) | .ge 域名 DNS 侦察 |
| ViewDNS | [https://viewdns.info](https://viewdns.info) | 反向 IP、WHOIS、DNS 记录、端口扫描 |
| Shodan | [https://shodan.io](https://shodan.io) | 搜索格鲁吉亚联网设备 |

### 格鲁吉亚 ASN 与网络数据

| 资源 | 网址 | 说明 |
|---|---|---|
| BGP.he.net 格鲁吉亚 | [https://bgp.he.net/country/GE](https://bgp.he.net/country/GE) | 全部格鲁吉亚 AS 号与网络（138 个 ASN） |
| IPinfo.io 格鲁吉亚 | [https://ipinfo.io/countries/ge](https://ipinfo.io/countries/ge) | 格鲁吉亚 IP 段、ISP 与地理定位数据 |
| NirSoft Georgia IPs | [https://nirsoft.net/countryip/ge_total.html](https://nirsoft.net/countryip/ge_total.html) | 分配给格鲁吉亚的全部 IP 段清单 |
| IPIP.NET Georgia | [https://whois.ipip.net/iso/GE](https://whois.ipip.net/iso/GE) | 格鲁吉亚 ASN 目录 |

### 格鲁吉亚主要 ISP 的 ASN

| ISP | ASN | 说明 |
|---|---|---|
| MagtiCom | AS16010, AS28751 | 最大移动/宽带运营商 |
| Silknet | AS35805 | 第二大运营商，DSL/光纤/移动 |
| Caucasus Online | AS20771 | 主要光纤骨干运营商 |
| GRENA | AS20545 | 格鲁吉亚科研教育网 |
| SIACOM | AS198150 | Business ISP |
| Delta Net | AS56844 | Regional ISP |
| Akhali Kselebi | AS44569 | Regional ISP |
| Caucasus Digital Network | AS57516 | CDN/托管服务商 |

### 格鲁吉亚适用的 Shodan/Censys 检索式

```
### Shodan:

- country:GE                          (all devices in Georgia)
- country:GE port:80                  (web servers)
- country:GE port:22                  (SSH servers)
- country:GE port:3389                (RDP servers)
- country:GE port:21                  (FTP servers)
- country:GE screenshot.label:webcam  (webcams)
- country:GE org:"Magticom"           (MagtiCom devices)
- country:GE org:"Silknet"            (Silknet devices)
- country:GE has_screenshot:true      (devices with screenshots)

### Censys:

- location.country_code:GE
- location.city:Tbilisi
```
### 50.17 教育与学术数据库

### 教育门户

| 资源 | 网址 | 说明 |
|---|---|---|
| 教育部 | [https://mes.gov.ge](https://mes.gov.ge) | 教育政策、学校数据、考试信息 |
| EMIS (Education Management) | [https://emis.ge](https://emis.ge) | 教育管理信息系统——学校数据、教师注册 |
| Schools Portal | [https://skolebi.emis.ge](https://skolebi.emis.ge) | 按名称、地区、类型搜格鲁吉亚学校——交互地图 |
| Student Portal | [https://students.emis.ge](https://students.emis.ge) | 大学生注册门户 |
| E-Library (MES) | [https://elibrary.emis.ge](https://elibrary.emis.ge) | 教材与教育资料 |
| EQE (Quality Enhancement) | [https://eqe.ge](https://eqe.ge) | 认证项目、机构评估、质量标准 |
| National Exam Center | [https://naec.ge](https://naec.ge) | 全国统考数据、大学录取统计 |

### 大学（主要）

| University | 网址 | OSINT Value |
|---|---|---|
| Tbilisi State University (TSU) | [https://tsu.ge](https://tsu.ge) | 院系名录、研究数据库、学位论文 |
| Georgian Technical University (GTU) | [https://gtu.ge](https://gtu.ge) | 师资、研究、出版物 |
| Ilia State University | [https://iliauni.edu.ge](https://iliauni.edu.ge) | 研究与图书馆数据库 |
| 第比利斯自由大学 | [https://freeuni.edu.ge](https://freeuni.edu.ge) | 教职员名录与项目 |
| Caucasus University | [https://cu.edu.ge](https://cu.edu.ge) | 师资与出版物 |
| 格鲁吉亚大学（UG） | [https://ug.edu.ge](https://ug.edu.ge) | 项目与师资 |
| 商业与技术大学（BTU） | [https://btu.edu.ge](https://btu.edu.ge) | 技术项目与师资 |
| Agricultural University | [https://agruni.edu.ge](https://agruni.edu.ge) | 农业研究数据 |

### 学术搜索

| 资源 | 网址 | 说明 |
|---|---|---|
| 格鲁吉亚国家图书馆 | [https://nplg.gov.ge](https://nplg.gov.ge) | 数字图书馆、历史文献、期刊档案 |
| OpenLibrary.ge | [https://openlibrary.ge](https://openlibrary.ge) | 格鲁吉亚学术出版物、学位论文 |
| Ilia University Library | [https://library.iliauni.edu.ge](https://library.iliauni.edu.ge) | 科学数据库访问 |
| TSU Digital Library | [https://digitallibrary.tsu.ge](https://digitallibrary.tsu.ge) | 学术论文与学位论文 |

---
### 50.18 卫生与医疗数据库

### 卫生部门

| 资源 | 网址 | 说明 |
|---|---|---|
| NCDC (Disease Control) | [https://ncdc.ge](https://ncdc.ge) | 国家疾病控制中心——流行病学数据、疾病监测、统计 |
| 卫生部 | [https://moh.gov.ge](https://moh.gov.ge) | 卫生政策、医院数据、医护人力 |
| Health Regulation Agency | [https://hra.gov.ge](https://hra.gov.ge) | 持证医疗机构与药品登记 |
| Social Service Agency | [https://ssa.gov.ge](https://ssa.gov.ge) | 社会救助数据、残障统计、医保覆盖 |

### 医疗 OSINT

| 资源 | 你能查到什么 |
|---|---|
| ncdc.ge/statistics | 分地区发病率、死亡数据、接种率 |
| Hospital Registry | 持证医院与诊所，含地址和专科 |
| Pharmacy Registry | 全格鲁吉亚持证药房 |
| Doctor Licensing | 医护执业注册（经卫生部） |
| GeoStat Health Data | [https://geostat.ge](https://geostat.ge) -- health statistics section |

---
### 50.19 NGO、公民社会与监督组织

### 格鲁吉亚重点 NGO（OSINT 资源）

| Organization | 网址 | Focus Area | OSINT Value |
|---|---|---|---|
| Transparency International Georgia | [https://transparency.ge](https://transparency.ge) | 反腐与资产监控 | 资产申报、政治献金、所有权调查 |
| IDFI | [https://idfi.ge](https://idfi.ge) | 信息自由、开放数据 | 信息公开申请、政府透明度监测 |
| GYLA | [https://gyla.ge](https://gyla.ge) | 法律改革与人权 | 法院监督、法律分析、选举观察 |
| ISFED | [https://isfed.ge](https://isfed.ge) | 选举观察 | 实时选举监督、违规数据库 |
| TI Georgia - Who Owns Georgia | [https://transparency.ge](https://transparency.ge) | 媒体所有权 | 深挖格鲁吉亚媒体控制者 |
| Social Justice Center | [https://socialjustice.org.ge](https://socialjustice.org.ge) | 社会权利、经济正义 | 劳动力、住房、经济数据 |
| Media Development Foundation | [https://mdfgeorgia.ge](https://mdfgeorgia.ge) | 新闻自由 | 媒体监测与媒体财务透明 |
| CRRC Georgia | [https://crrc.ge](https://crrc.ge) | 研究与民调 | 民意调查与研究数据集 |
| 人权伙伴组织 | [https://phr.ge](https://phr.ge) | 人权监测 | 人权报告 |
| Democracy Research Institute | [https://democracyresearch.ge](https://democracyresearch.ge) | 民主状况监测 | 民主指标与政治分析 |
| CATAGI | [https://catagi.ge](https://catagi.ge) | 权力结构分析 | 非正式权力网络调查 |

---
### 50.20 事实核查与虚假信息追踪

### 事实核查组织

| Organization | 网址 | 说明 |
|---|---|---|
| Myth Detector | [https://mythdetector.com](https://mythdetector.com) | 媒体发展基金会核查门户——虚假信息数据库 |
| FactCheck.ge | [https://factcheck.ge](https://factcheck.ge) | GRASS 计划——评估公职人员言论准确率 |
| GeoFacts | [https://geofacts.ge](https://geofacts.ge) | 事实核查平台 |
| MythDetector Database | [https://mythdetector.com/en/factchecker-db/](https://mythdetector.com/en/factchecker-db/) | 已核查论断的可检索库 |

### 虚假信息监测

| 资源 | 网址 | 说明 |
|---|---|---|
| ISFED Social Media Monitoring | [https://isfed.ge](https://isfed.ge) | 监测格鲁吉亚社媒上的俄罗斯信息操作 |
| MDF Annual Reports | [https://mdfgeorgia.ge](https://mdfgeorgia.ge) | 细致的媒体监测与虚假信息分析 |
| DFRLab (Atlantic Council) | [https://atlanticcouncil.org/programs/digital-forensic-research-lab/](https://atlanticcouncil.org/programs/digital-forensic-research-lab/) | 数字取证分析，含格鲁吉亚相关虚假信息 |
| EU vs Disinfo | [https://euvsdisinfo.eu](https://euvsdisinfo.eu) | 欧盟亲克里姆林宫虚假信息库——含格鲁吉亚 |
| Hamilton 2.0（保障民主联盟） | [https://securingdemocracy.gmfus.org/hamilton-dashboard/](https://securingdemocracy.gmfus.org/hamilton-dashboard/) | 追踪俄/中国家媒体对格鲁吉亚的叙事 |

---
### 50.21 档案与历史数据库

### 国家档案与图书馆

| 资源 | 网址 | 说明 |
|---|---|---|
| 格鲁吉亚国家档案馆 | [https://archive.gov.ge](https://archive.gov.ge) | 历史文献、电子目录、数字化资料、阅览室预约 |
| National Archives Electronic Catalogues | [https://archive.gov.ge](https://archive.gov.ge) (catalogues section) | 档案文件可检索索引 |
| 格鲁吉亚国家图书馆 | [https://nplg.gov.ge](https://nplg.gov.ge) | 国家图书馆——数字馆藏、珍本、期刊档案 |
| National Parliamentary Library | [https://nplg.gov.ge](https://nplg.gov.ge) | 立法史与议会辩论档案 |
| Internet Archive (Georgia) | [https://archive.org/details/1989-tbilisi-1_202408](https://archive.org/details/1989-tbilisi-1_202408) | Internet Archive 上的 Sakartvelo（格鲁吉亚）合集存档 |
| Wayback Machine（.ge 站点） | [https://web.archive.org/web/*/*.ge](https://web.archive.org/web/*/*.ge) | 格鲁吉亚网站的缓存版本——历史快照 |

### 历史与文化数据库

| 资源 | 网址 | 说明 |
|---|---|---|
| Georgian National Museum | [https://museum.ge](https://museum.ge) | 馆藏、考古数据、文物 |
| 文化遗产保护局 | [https://heritage.gov.ge](https://heritage.gov.ge) | 文化遗产古迹与保护地数据库 |
| Georgian Cinema Database | [https://georgiancinema.ge](https://georgiancinema.ge) | 格鲁吉亚电影史、导演、演员 |
| OpenLibrary.ge | [https://openlibrary.ge](https://openlibrary.ge) | 学术出版物、学位论文、历史文献 |

### 档案类 OSINT 技巧

```
### 格鲁吉亚站点的 Wayback Machine 查询：

- https://web.archive.org/web/*/napr.gov.ge     (old property data)
- https://web.archive.org/web/*/rs.ge            (old tax data)
- https://web.archive.org/web/*/cesko.ge         (old election data)
- https://web.archive.org/web/*/parliament.ge    (old MP profiles)

Use these to find information that may have been removed from current sites.
```
### 50.22 拍卖与罚没资产

### 政府拍卖平台

| 资源 | 网址 | 说明 |
|---|---|---|
| eAuction.ge | [https://eauction.ge](https://eauction.ge) | 官方国有资产拍卖平台——罚没资产、政府 surplus、房产、车辆 |
| Gavel.ge | [https://gavel.ge](https://gavel.ge) | 聚合 Livo、eAuction.ge 与第比利斯市政拍卖（11000+ 件） |
| Livo Auctions | [https://livo.ge](https://livo.ge) (auction section) | 带 3D 看房的房产拍卖 |
| Tbilisi Municipality Auctions | [https://tbilisi.gov.ge](https://tbilisi.gov.ge) | 市政资产出售 |
| 国家执行局（LEPL） | [https://nbe.gov.ge](https://nbe.gov.ge) | 强制执行/罚没资产拍卖 |

### 拍卖数据里能查到什么

```
eAuction.ge reveals:
- Seized properties of individuals/companies (with owner names)
- Government surplus equipment
- Bank foreclosure properties
- Court-ordered asset sales
- Detailed property descriptions with photos
- Starting prices and bid history
- Buyer information (in completed auctions)

### OSINT 价值：显示谁失去了房产及原因（欠债、犯罪、逃税）

```
### 50.23 招聘市场与分类信息

### 招聘门户

| Portal | 网址 | 说明 |
|---|---|---|
| Jobs.ge | [https://jobs.ge](https://jobs.ge) | 格鲁吉亚最大招聘站——雇主名、薪资、职位 |
| HR.ge | [https://hr.ge](https://hr.ge) | 带简历库的专业招聘门户 |
| LinkedIn (Georgia) | [https://linkedin.com](https://linkedin.com) (filter by Georgia) | 职场社交、公司主页 |
| Myjobs.ge | [https://myjobs.ge](https://myjobs.ge) | 补充招聘信息 |
| CV.ge | [https://cv.ge](https://cv.ge) | 简历平台 |

### 分类信息（综合）

| Portal | 网址 | 说明 |
|---|---|---|
| SS.GE | [https://ss.ge](https://ss.ge) | 格鲁吉亚最大分类站——房产、车辆、数码、招聘、服务（OSINT 金矿） |
| MyMarket.ge | [https://mymarket.ge](https://mymarket.ge) | 二手市场——卖家档案、位置、电话 |
| MyAuto.ge | [https://myauto.ge](https://myauto.ge) | 车辆分类信息 |
| MyHome.ge | [https://myhome.ge](https://myhome.ge) | 房产分类信息 |
| MyParts.ge | [https://myparts.ge](https://myparts.ge) | 汽车配件市场 |
| Extra.ge | [https://extra.ge](https://extra.ge) | 综合分类信息与集市 |
| Makler.ge | [https://makler.ge](https://makler.ge) | 服务平台市场 |

### 分类信息的 OSINT 价值

```
### 格鲁吉亚分类信息常见暴露：

- Real phone numbers of sellers
- Physical addresses
- Photos of properties/vehicles (with metadata)
- Business names and registration details
- Price history (for repeated listings)
- Location data from listings

SS.GE in particular is a treasure trove:
- Most Georgians have used SS.GE at some point
- Old listings are often still accessible
- Google cache: site:ss.ge "phone number" "name"
```
### 50.24 资产申报与反腐

### 公职人员资产申报

| 资源 | 网址 | 说明 |
|---|---|---|
| Civil Service Bureau Declarations | [https://csb.gov.ge](https://csb.gov.ge) | 公职人员资产申报——收入、房产、证券、负债 |
| Anti-Corruption Bureau | [https://acb.gov.ge](https://acb.gov.ge) | 资产申报监控部门 |
| OpenSanctions (Georgia Declarations) | [https://opensanctions.org/datasets/ge_declarations/](https://opensanctions.org/datasets/ge_declarations/) | 格鲁吉亚官方资产申报的结构化数据 |
| Transparency International Georgia | [https://transparency.ge](https://transparency.ge) | 官方资产申报的分析与监控 |

### 资产申报里有什么

```
### 格鲁吉亚公职人员必须每年申报：

- Real estate (addresses, values)
- Vehicles (make, model, year)
- Securities (company shares, stock holdings)
- Bank deposits and cash
- Income sources (salary, business income, gifts)
- Debts and liabilities
- Family members' assets
- Gifts over 1,000 GEL

### 适用对象：议员、部长、法官、检察官、市长、高官

civil servants, and their family members.

OpenSanctions.org provides this data in machine-readable format.
```
### 50.25 格鲁吉亚语字典与密码工具

### 格鲁吉亚语词典

| 资源 | 说明 | Use Case |
|---|---|---|
| 格鲁吉亚语词典（geowordlist.txt） | 11.9 MB 格鲁吉亚语词汇与常见密码字典 | 密码破解与安全审计 |
| make_wordlist.py | 按规则生成自定义格鲁吉亚语字典的 Python 脚本 | 为格鲁吉亚目标生成自定义字典 |
| Georgian Keyboard Layout Patterns | 格鲁吉亚键盘布局常见按键模式 | 密码生成 |
| Georgian Name Combinations | 格鲁吉亚常见的名+姓+年份组合模式 | 定向密码清单 |

### 格鲁吉亚常见密码模式

```
### 格鲁吉亚最常见的密码结构：

- Name + birth year: giorgi1990, nino1985
- Georgian words in Latin: tbilisi, sakartvelo, gamarjoba
- Phone number as password: 555123456, 577987654
- ID number as password: 01001012345
- Georgian words in Georgian script: პაროლი, თბილისი
- Common substitutions: @ for a, 3 for e, 0 for o
- Name + 123: giorgi123, nino123
- Football teams: dinamo, torpedo
- Georgian places: batumi, kutaisi, borjomi

### 密码破解工具：

- Hashcat: hashcat -m 0 hash.txt geowordlist.txt
- John the Ripper: john --wordlist=geowordlist.txt hash.txt
```
### 生成格鲁吉亚语字典

```bash
# 用 make_wordlist.py（来自上传工具）
python3 make_wordlist.py --language georgian --output geo_custom.txt

# 用 crunch 生成格鲁吉亚模式
crunch 8 12 abcdefghijklmnopqrstuvwxyz0123456789 -t @@@@%%%% -o patterns.txt

# 格鲁吉亚姓名与年份组合
for name in giorgi nino dato mari luka ana; do
  for year in $(seq 1980 2005); do
    echo "${name}${year}"
  done
done > georgian_names_years.txt
```
### 50.26 面向格鲁吉亚的 Telegram OSINT

### 格鲁吉亚新闻与政治频道

| Channel | Handle | 说明 |
|---|---|---|
| Formula News | @formulanewstv | 独立电视新闻频道 |
| Mtavari Arkhi | @mtavariarkhi | 倾向反对派的电视频道 |
| Netgazeti | @netgazeti | 独立网络新闻 |
| Tabula | @tabormagazine | 自由派新闻/分析 |
| Civil Georgia | @CivilGe | 独立英文新闻 |
| Radio Tavisupleba | @radiotavisupleba | 自由欧洲/自由电台格鲁吉亚语服务 |
| Various Political Groups | 搜索 "Georgia politics" | 政治讨论群组 |

### OSINT Telegram 机器人（支持格鲁吉亚数据）

| Bot | Handle | 说明 | 免费/付费 |
|---|---|---|---|
| Eye of God（神之眼） | @EyeOfGodBot | 按电话、姓名、车辆查人——独联体 + 格鲁吉亚数据 | 付费 |
| Quick OSINT | @QuickOSINT_bot | 多数据库人物查询 | 付费 |
| GetContact Bot | @getcontact_bot | 来电识别查询 | 免费增值 |
| Phone Number Search | @PhoneNumber_SearchBot | 电话号码 OSINT | 免费增值 |
| Email Search | @mailsearchbot | 邮箱泄露查询 | 免费增值 |
| Leak OSINT | @leak_osint_bot | 泄露数据查询 | 付费 |
| Search4Faces | @search4aboringface_bot | 人脸识别搜索 | 免费增值 |

### 俄语 OSINT 频道（与格鲁吉亚相关）

| Channel | Handle | 说明 |
|---|---|---|
| overbafer1 | @overbafer1 | OSINT 工具与技术 |
| overlamer1 | @overlamer1 | 黑客与安全 |
| Social Engineering | @Social_engineering | 社会工程技术 |
| Cyberbezopasno | @cyberbezopasno | 网络安全新闻 |

### 格鲁吉亚 Telegram OSINT 技巧

```
1. Search by phone number: Enter +995XXXXXXXXX in Telegram search
   - Find if the person has Telegram
   - See their username, profile photo, bio

2. Search Georgian groups/channels:
   - Use tgstat.com to search for Georgian channels
   - Search for Georgian keywords in channel search

3. Forward message analysis:
   - Check "forwarded from" headers to trace information flow

4. Telegram Scraping Tools:
   - telegram-scraper (GitHub)
   - Telethon (Python library)
   - tg-archive for archiving channels
```
### 50.27 调查框架与社区

### 覆盖格鲁吉亚的 OSINT 框架

| Framework | 网址 | 说明 |
|---|---|---|
| OSINT Framework | [https://osintframework.com](https://osintframework.com) | 网页版 OSINT 工具目录 |
| Bellingcat OSINT Toolkit | [https://docs.google.com/spreadsheets/d/18rtqh8EG2q1xBo2cLNyhIDuK9jrPGwYr9DI2UncoqJQ](https://docs.google.com/spreadsheets/d/18rtqh8EG2q1xBo2cLNyhIDuK9jrPGwYr9DI2UncoqJQ) | 综合 OSINT 工具表 |
| UNISHKA Georgia OSINT Guide | [https://unishka.substack.com/p/osint-of-georgia](https://unishka.substack.com/p/osint-of-georgia) | 格鲁吉亚专属 OSINT 方法论指南 |
| Start.me OSINT 页集 | [https://start.me](https://start.me) | OSINT 资源精选合集 |
| Awesome OSINT (GitHub) | [https://github.com/jivoi/awesome-osint](https://github.com/jivoi/awesome-osint) | OSINT 工具精选清单 |
| OSINT Dojo | [https://www.osintdojo.com](https://www.osintdojo.com) | OSINT 学习平台 |

### 调查者社区

| Community | Platform | 说明 |
|---|---|---|
| Bellingcat | [https://bellingcat.com](https://bellingcat.com) | 开源调查——做过格鲁吉亚选题 |
| OCCRP | [https://occrp.org](https://occrp.org) | 有组织犯罪与腐败报道项目——格鲁吉亚调查 |
| ICIJ | [https://icij.org](https://icij.org) | 国际调查报道——潘多拉文件、巴拿马文件（格鲁吉亚条目） |
| GIJN | [https://gijn.org](https://gijn.org) | 全球调查记者网络 |

### ICIJ 数据库（格鲁吉亚条目）

| Database | 网址 | 说明 |
|---|---|---|
| Offshore Leaks Database | [https://offshoreleaks.icij.org](https://offshoreleaks.icij.org) | 在巴拿马、天堂、潘多拉文件中搜格鲁吉亚个人/公司 |
| ICIJ Data | [https://icij.org/investigations/](https://icij.org/investigations/) | 完整调查档案，带可检索数据库 |

---
### 50.28 面向格鲁吉亚的 Google Dork

### 政府与官方网站

```
site:gov.ge filetype:pdf
site:gov.ge filetype:xlsx
site:gov.ge filetype:docx
site:gov.ge filetype:csv
site:napr.gov.ge
site:rs.ge
site:parliament.ge
site:cesko.ge
site:geostat.ge filetype:xlsx
site:matsne.gov.ge
```
### 个人信息发现

```
"+995" site:facebook.com
"+995" site:linkedin.com
"@gmail.com" site:gov.ge
"@yahoo.com" site:.ge
intext:"+995" filetype:xlsx
intext:"+995" filetype:csv
allintext:"tbilisi" "phone" "email" filetype:xlsx
"პირადი ნომერი" filetype:pdf site:gov.ge
"საიდენტიფიკაციო" filetype:xlsx
```
### 商业与企业情报

```
site:enreg.reestri.gov.ge
site:rs.ge "taxpayer"
"შპს" filetype:pdf site:gov.ge
"სს" OR "შპს" "+995" filetype:xlsx
site:tenders.procurement.gov.ge
"ხელშეკრულება" filetype:pdf site:gov.ge
```
### 凭据与敏感数据发现

```
allintext:"@gmail.com" "password" filetype:xlsx site:.ge
allintext:"username" "password" filetype:csv site:.ge
inurl:admin site:.ge
inurl:login site:.ge
inurl:wp-admin site:.ge
inurl:cpanel site:.ge
intitle:"index of" site:.ge
intitle:"index of" "parent directory" site:.ge
inurl:".env" site:.ge
inurl:"wp-config.php" site:.ge
site:.ge filetype:sql
site:.ge filetype:log
site:.ge filetype:bak
```
### Educational & Academic

```
site:tsu.ge filetype:pdf
site:gtu.ge filetype:pdf
site:iliauni.edu.ge filetype:pdf
site:emis.ge
"student" OR "სტუდენტი" filetype:xlsx site:.ge
"dissertation" OR "სადისერტაციო" site:.ge filetype:pdf
```
### Media & Social

```
site:civil.ge "investigation"
site:transparency.ge "report"
site:idfi.ge "public information"
site:interpressnews.ge
"tbilisi" OR "თბილისი" site:instagram.com
"sakartvelo" site:youtube.com
```
### 摄像头与 IoT 发现

```
inurl:/view/index.shtml site:.ge
inurl:/live/cam.html site:.ge
intitle:"webcam" site:.ge
inurl:"view/viewer_index.shtml" country:ge
inurl:/mjpg/video.mjpg site:.ge
"Server: yawcam" site:.ge
```
### Infrastructure & Network

```
site:.ge inurl:phpMyAdmin
site:.ge intitle:"Apache2 Ubuntu Default Page"
site:.ge intitle:"Welcome to nginx"
site:.ge "powered by WordPress"
site:.ge "Joomla"
"*.ge" site:crt.sh
"*.gov.ge" site:shodan.io
```
### 高级组合

```
# 找暴露的数据库
site:.ge filetype:sql "INSERT INTO" "VALUES"

# 找暴露的配置文件
site:.ge filetype:xml "password"
site:.ge filetype:ini "password"
site:.ge filetype:conf "server"

# 找暴露的目录
intitle:"index of" "parent directory" site:.ge filetype:pdf

# 找暴露的邮件列表
"@" filetype:csv site:.ge
"email" "phone" filetype:xlsx site:.ge

# 查找带数据的格鲁吉亚政府报告
site:gov.ge "report" "2024" filetype:pdf
site:gov.ge "statistics" filetype:xlsx
```
### 附录 A：格鲁吉亚字母速查

```
### 格鲁吉亚文字（姆赫德鲁利）——33 个字母：


ა ბ გ დ ე ვ ზ თ ი კ ლ მ ნ ო პ ჟ რ ს ტ უ ფ ქ ღ ყ შ ჩ ც ძ წ ჭ ხ ჯ ჰ

### Transliteration:

a b g d e v z t' i k l m n o p zh r s t u p' k' gh q' sh ch ts dz ts' ch' kh j h

### 研究时用拉丁转写搜格鲁吉亚姓名很有用

Georgian individuals in international databases.
```
### 附录 B：格鲁吉亚 OSINT 调查流程

```
STEP 1: IDENTIFY THE TARGET
  - Name (Georgian + Latin spelling)
  - Personal ID number (11 digits)
  - Phone number (+995 XXX XXX XXX)
  - Email address
  - Date of birth
  - Company name/ID

### 第 2 步：政府数据库

  [ ] NAPR (napr.gov.ge) -- property, business, civil registry
  [ ] RS (rs.ge) -- tax status, business activity
  [ ] Entrepreneur Registry -- company details, directors
  [ ] ecd.court.ge -- court cases
  [ ] cesko.ge -- voter registration
  [ ] csb.gov.ge -- if public official, check asset declarations

### 第 3 步：社交媒体与网络足迹

  [ ] Facebook (Georgian name + Latin name)
  [ ] Instagram
  [ ] LinkedIn
  [ ] Telegram (search by phone number)
  [ ] Google search: "name" "+995" / "name" "tbilisi"
  [ ] SS.GE (classifieds -- may have phone number, property listings)

### STEP 4: FINANCIAL & BUSINESS

  [ ] enreg.reestri.gov.ge -- company ownership/directorship
  [ ] tenders.procurement.gov.ge -- government contracts
  [ ] nbg.gov.ge -- banking/AML sanctions
  [ ] offshoreleaks.icij.org -- offshore connections
  [ ] opensanctions.org -- sanctions cross-reference

### 第 5 步：泄露与拖库数据

  [ ] haveibeenpwned.com -- email breaches
  [ ] leakcheck.io -- email/phone breach search
  [ ] dehashed.com -- comprehensive breach search
  [ ] Known Georgian data leaks (4.9M citizen leak)

### 第 6 步：电话 OSINT

  [ ] GetContact -- caller ID lookup
  [ ] TrueCaller -- caller ID
  [ ] WhatsApp profile check
  [ ] Viber profile check
  [ ] Telegram profile check
  [ ] Google: "+995XXXXXXXXX"

### STEP 7: PROPERTY & VEHICLES

  [ ] NAPR property registry
  [ ] nsdi.gov.ge -- cadastral map lookup
  [ ] SS.GE / MyHome.ge -- property listings
  [ ] MyAuto.ge -- vehicle listings
  [ ] eauction.ge -- seized property

### STEP 8: ADVANCED

  [ ] Google dorking: site:.ge "target name"
  [ ] Wayback Machine: web.archive.org/web/*/.ge
  [ ] Shodan: country:GE
  [ ] Certificate Transparency: crt.sh
  [ ] OSINT Telegram bots (Eye of God, Quick OSINT)
```
### 附录 C：关键网址速查

| Category | 网址 |
|---|---|
| E-Government Portal | [https://my.gov.ge](https://my.gov.ge) |
| Property Registry | [https://napr.gov.ge](https://napr.gov.ge) |
| Business Registry | [https://enreg.reestri.gov.ge](https://enreg.reestri.gov.ge) |
| Tax Authority | [https://rs.ge](https://rs.ge) |
| Court Decisions | [https://ecd.court.ge](https://ecd.court.ge) |
| Legislation | [https://matsne.gov.ge](https://matsne.gov.ge) |
| Elections | [https://cesko.ge](https://cesko.ge) |
| Statistics | [https://geostat.ge](https://geostat.ge) |
| Procurement | [https://tenders.procurement.gov.ge](https://tenders.procurement.gov.ge) |
| Open Data | [https://data.gov.ge](https://data.gov.ge) |
| Domain WHOIS | [https://nic.ge/en/domains/whois](https://nic.ge/en/domains/whois) |
| Geoportal | [https://nsdi.gov.ge](https://nsdi.gov.ge) |
| Education | [https://emis.ge](https://emis.ge) |
| Health | [https://ncdc.ge](https://ncdc.ge) |
| National Archives | [https://archive.gov.ge](https://archive.gov.ge) |
| National Library | [https://nplg.gov.ge](https://nplg.gov.ge) |
| Classifieds | [https://ss.ge](https://ss.ge) |
| Vehicles | [https://myauto.ge](https://myauto.ge) |
| Real Estate | [https://myhome.ge](https://myhome.ge) |
| Auctions | [https://eauction.ge](https://eauction.ge) |
| Jobs | [https://jobs.ge](https://jobs.ge) |
| Asset Declarations | [https://csb.gov.ge](https://csb.gov.ge) |
| Fact-Checking | [https://factcheck.ge](https://factcheck.ge) |
| Anti-Disinfo | [https://mythdetector.com](https://mythdetector.com) |
| Investigative | [https://transparency.ge](https://transparency.ge) |
| Open Data Procurement | [https://opendata.spa.ge](https://opendata.spa.ge) |

---
![OSINT Arsenal Logo](https://raw.githubusercontent.com/rawfilejson/awesome-osint-arsenal/main/assets/logo.jpg)
🔍 AWESOME OSINT ARSENAL
终极开源情报工具箱

---



</details>

---
## 🤝 贡献与问题反馈

发现死链？有该收录的工具？直接提 issue 或 PR。

- **发现问题** → [提 issue](https://github.com/rawfilejson/awesome-osint-arsenal/issues/new)
- **想添加工具** → fork，按字母序加进正确分类，提 PR
- **没时间提 PR？** → 在 issue 里留下工具名 + 网址，我来补

提交前请在干净的 Kali 虚机上验证安装命令。

---

## ⚖️ 法律免责声明

本仓库仅用于**教育与授权的安全研究目的**。

**✅ Legal uses:**
- 对自有系统的安全研究
- 持书面授权的渗透测试
- 新闻调查或寻人 OSINT
- 规定范围内的漏洞赏金项目
- Security awareness training

**❌ Illegal uses (never do these):**
- 未经授权访问系统或账号
- Stalking or harassment
- Credential theft
- DDoS 或攻击非自有系统
- Privacy violations

**适用法律：** GDPR（欧盟）、CCPA（加州）、CFAA（美国）、Computer Misuse Act（英国）及当地对应法规。**行动前先弄清你所在地的法律。**

> 本仓库维护者对所列信息或工具的任何滥用**不承担责任**。

---

<div align="center">

<br/>

*为 OSINT 与安全研究社区而建。*

*知识就是力量，请负责任地使用。*

<a href="https://www.buymeacoffee.com/rawfilejson" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me a Coffee" style="height: 60px !important;width: 217px !important;" ></a>

<br/>

**⭐ 觉得有用就点个 Star！**

[![GitHub stars](https://img.shields.io/github/stars/rawfilejson/awesome-osint-arsenal?style=social)](https://github.com/rawfilejson/awesome-osint-arsenal/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/rawfilejson/awesome-osint-arsenal?style=social)](https://github.com/rawfilejson/awesome-osint-arsenal/network/members)

<br/>

</div>
