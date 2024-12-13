+++
title = "一些常用的 rust 命令行工具"
date = 2024-12-13
description = "cargo tools"
+++

## 简单介绍下
`duf`: 一个现代化的磁盘使用情况查看工具

`zellij`: 一个强大的终端窗口管理器

`starship`: 一个高度可定制的命令行提示符

`eza`: 一个现代化的替换 `ls` 的工具

`bottom`: 一个多功能的系统监控工具

## 一键安装
```bash
cargo install duf zellij starship eza bottom
```

但在这之前, 需要安装如下依赖:
``` bash
cmake
```

## 简单配置下
写入 `~/.bashrc` :

### starship
```bash
eval "$(starship init bash)"
```

### eza
```bash
alias ls='eza --icons'
alias ll='eza --icons -l'
alias la='eza --icons -la'
alias tree='eza --icons --tree'
```