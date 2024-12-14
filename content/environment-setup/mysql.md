+++
title = "一行命令速通mysql"
date = 2024-12-15
description = "mysql"
+++

## 安装 mysql
```bash
scoop install mysql
```

没错 这就已经装好了

## 启动 mysql

在其他教程中可能让你开启 mysql 服务, 但是我并不推荐你这么做, 因为这样他会一直在后台运行, 并且开机自启, 实际上你只需要在命令行中输入 `mysql` 回车就可以了

就像这样, 什么输出都没有, 没有消息就是最好的消息

```bash
PS C:\Users\LiYang> mysql

```

## 连接 mysql

这里我推荐使用 [beekeeper](https://github.com/beekeeper-studio/beekeeper-studio/releases), 社区版本开源免费, 包含了大部分功能, 大部分情况下, 你应该下载 `Beekeeper-Studio-Setup-x.x.x.exe
`

默认下账号 root 密码空, 端口 3306