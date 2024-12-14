+++
title = "在 Windows 上速通 Python 环境配置"
date = 2024-12-14
description = "Python Windows"
+++

## 在开始之前

请确保你完成了以下步骤:

- [一切的前提](/environment-setup/prerequisites)
- [安装Scoop](/environment-setup/scoop)
- [vscode的基本使用](/environment-setup/vscode)

## 卸载 Python

如果你之前安装了 Python, 请卸载它, 包括 Python 本体和任何有关 Python 的环境变量

如果你没有安装, 那么我们继续:)

## 直接安装 Python

如果你并不需要使用 Anaconda 管理多个版本多个环境的 Python, 那么你可以直接使用 Scoop 安装 Python

```bash
scoop install python
```
没错, 仅需一个命令就安装好了! 不需要任何其他操作

如果你需要安装依赖, 可以在终端中直接使用 pip 安装

```bash
PS C:\Users\LiYang> pip install numpy pandas matplotlib
```

然后你可以直接在终端运行 python 文件

```bash
PS C:\Users\LiYang> python main.py
```

## 使用 Anaconda 安装 Python

如果你需要使用 Anaconda 管理多个 Python 版本

运行 `scoop install miniconda3` 安装 miniconda (相当于精简版的Anaconda)

``` bash
PS C:\Users\LiYang> scoop install miniconda3
Installing 'miniconda3' (24.9.2-0) [64bit] from 'extras' bucket
Miniconda3-py312_24.9.2-0-Windows-x86_64.exe (85.7 MB) [=====================================================] 100%
Checking hash of Miniconda3-py312_24.9.2-0-Windows-x86_64.exe ... ok.
Running pre_install script...done.
Running installer script...done.
Linking ~\scoop\apps\miniconda3\current => ~\scoop\apps\miniconda3\24.9.2-0
Creating shim for 'python'.
Creating shim for 'pythonw'.
Making C:\Users\LiYang\scoop\shims\pythonw.exe a GUI binary.
Creating shim for 'python3'.
Adding ~\scoop\apps\miniconda3\current\scripts to your path.
Adding ~\scoop\apps\miniconda3\current\Library\bin to your path.
Persisting envs
Running post_install script...done.
'miniconda3' (24.9.2-0) was installed successfully!
Notes
-----
From 4.6.0, conda has built the support for Cmd, Powershell or other shells.
Use "conda init powershell" or "conda init __your_favorite_shell__"

Miniconda3 drops support for 32-bit CPUs from v22.9.0. If you are running a 32-bit system, please install
miniconda3-4.12.0 from the Versions bucket.
```

安装成功后, 在 powershell 中初始化 conda

``` bash
conda init powershell
```

此时重新开启一个终端, 可以看到提示符前已经有了一个 `base`
```bash
(base) PS C:\Users\LiYang>
```
在任何情况下都不推荐对 base 环境进行任何操作, 你需要新建一个环境
```bash
conda create -n env_name python=3.xx
```

比如:
```bash
(base) PS C:\Users\LiYang> conda create -n scicomp python=3.11       # 创建名为 scicomp python版本为 3.11 的环境
... 创建过程
(base) PS C:\Users\LiYang> conda activate scicomp                    # 切换到 scicomp 环境 注意下一行括号里的 base 变成了 scicomp
(scicomp) PS C:\Users\LiYang> pip install numpy pandas matplotlib    # 使用 pip 安装依赖
... 安装过程
(scicomp) PS C:\Users\LiYang> python main.py                         # 运行程序
```

## 配置 VSCode

在 vscode 的插件中搜索 Python, 并安装

现在你可以直接在 vscode 中打开一个文件夹, 然后在这个文件夹下创建 xxx.py 文件, 即可编写代码

然后点击右下角的 `选择解释器` (或者默认选择了Python版本) 选择你想使用的环境

使用 `ctrl + ~` 打开终端, 此时 vscode 应该会自动在终端中激活你刚刚选择的环境, 此时你可以直接使用 `python xxx.py` 运行代码