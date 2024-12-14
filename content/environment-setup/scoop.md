+++
title = "在 windows 中使用 scoop 管理软件包"
date = 2024-12-14
description = "scoop"
+++

在手机上我们用应用商店安装软件, 在电脑上我们可以用 steam 下载游戏, 但为什么没有一款软件可以方便的安装/卸载编程所需的环境呢?

其实是有的:

- [win-get](https://github.com/microsoft/winget-cli) Windows下自带的包管理器 不太好用
- [chocolatey](https://chocolatey.org) Windows下的第三方包管理器 我没用过
- [scoop](https://scoop.sh) Windows下的第三方包管理器 好用 也是本文主题

## 安装 scoop

进入[scoop](https://scoop.sh)官网, 我们可以看到两行命令:

```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
```

我们将其一行一行复制到 powershell 中, 回车运行即可安装, 注意不要用管理员启动 powershell, 期间可能让你确认权限, 输入 A 回车即可

此时你的终端看起来类似这样:

运行 `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

```bash
PS C:\Users\LiYang> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
执行策略更改
执行策略可帮助你防止执行不信任的脚本。更改执行策略可能会产生安全风险，如 https:/go.microsoft.com/fwlink/?LinkID=135170
中的 about_Execution_Policies 帮助主题所述。是否要更改执行策略?
[Y] 是(Y)  [A] 全是(A)  [N] 否(N)  [L] 全否(L)  [S] 暂停(S)  [?] 帮助 (默认值为“N”): A <-在这里输入A
```

运行 `Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression`

```bash
PS C:\Users\LiYang> Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
Initializing...
Downloading...
Extracting...
Creating shim...
Adding ~\scoop\shims to your path.
Scoop was installed successfully!
Type 'scoop help' for instructions.
```

我们可以运行 `scoop --version` 检查是否安装成功, 如果失败了, 请检查网络连接再重试

```bash
PS C:\Users\LiYang> scoop --version
Current Scoop version:
v0.5.2 - Released at 2024-07-26
```

## scoop 常用命令

- `scoop search xxx` 搜索名为xxx的软件
- `scoop install xxx` 安装名为xxx的软件
- `scoop uninstall xxx` 卸载名为xxx的软件
- `scoop bucket add xxx` 添加软件源

## 添加常用源

软件被包括在源中, 默认的 main 源中有大部分的常用软件, 但这还不够, 我们需要添加一些常用的第三方源, 以下是一些官方维护的源:

- `main` Scoop 的默认软件仓库，提供了大量常用和稳定的软件包
- `extras` 提供额外的软件包，种类更丰富
- `versions` 允许安装不同版本的软件包
- `nirsoft` 收集了NirSoft提供的免费实用工具
- `sysinternals` 微软提供的系统工具集
- `php` PHP语言及其相关工具的软件包
- `nerd-fonts` 收集了带有编程符号的字体
- `java` 包含Java开发相关的软件包
- `games` 提供各类游戏软件包

我们要用到的是 `extras` 和 `java`

先安装 git, 如果之前安装过了, 建议先卸载, 用 scoop 统一管理

运行 `scoop install git` 看起来像这样:

```bash
PS C:\Users\LiYang> scoop install git
Installing '7zip' (24.09) [64bit] from 'main' bucket
7z2409-x64.msi (1.9 MB) [====================================================================================] 100%
Checking hash of 7z2409-x64.msi ... ok.
Extracting 7z2409-x64.msi ... done.
Linking ~\scoop\apps\7zip\current => ~\scoop\apps\7zip\24.09
Creating shim for '7z'.
Creating shim for '7zFM'.
Making C:\Users\LiYang\scoop\shims\7zfm.exe a GUI binary.
Creating shim for '7zG'.
Making C:\Users\LiYang\scoop\shims\7zg.exe a GUI binary.
Creating shortcut for 7-Zip (7zFM.exe)
Persisting Codecs
Persisting Formats
Running post_install script...done.
'7zip' (24.09) was installed successfully!
Notes
-----
Add 7-Zip as a context menu option by running: "C:\Users\LiYang\scoop\apps\7zip\current\install-context.reg"
Installing 'git' (2.47.1) [64bit] from 'main' bucket
PortableGit-2.47.1-64-bit.7z.exe (60.0 MB) [=================================================================] 100%
Checking hash of PortableGit-2.47.1-64-bit.7z.exe ... ok.
Extracting PortableGit-2.47.1-64-bit.7z.exe ... done.
Linking ~\scoop\apps\git\current => ~\scoop\apps\git\2.47.1
Creating shim for 'sh'.
Creating shim for 'bash'.
Creating shim for 'git'.
Creating shim for 'gitk'.
Making C:\Users\LiYang\scoop\shims\gitk.exe a GUI binary.
Creating shim for 'git-gui'.
Making C:\Users\LiYang\scoop\shims\git-gui.exe a GUI binary.
Creating shim for 'scalar'.
Creating shim for 'tig'.
Creating shim for 'git-bash'.
Making C:\Users\LiYang\scoop\shims\git-bash.exe a GUI binary.
Creating shortcut for Git Bash (git-bash.exe)
Creating shortcut for Git GUI (git-gui.exe)
Running post_install script...done.
'git' (2.47.1) was installed successfully!
Notes
-----
Set Git Credential Manager Core by running: "git config --global credential.helper manager"

To add context menu entries, run 'C:\Users\LiYang\scoop\apps\git\current\install-context.reg'

To create file-associations for .git* and .sh files, run
'C:\Users\LiYang\scoop\apps\git\current\install-file-associations.reg'
```

添加源:

- `scoop bucket add extras`
- `scoop bucket add java`

```bash
PS C:\Users\LiYang> scoop bucket add extras
Checking repo... OK
The extras bucket was added successfully.
PS C:\Users\LiYang> scoop bucket add java
Checking repo... OK
The java bucket was added successfully.
```

scoop 中有大量的软件包, 大家可以自由探索
