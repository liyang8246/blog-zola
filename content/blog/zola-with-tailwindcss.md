+++
title = "使用zola + tailwindcss构建博客"
date = 2024-12-10
description = "zola tailwindcss blog"
+++

## 安装依赖

```bash
scoop install zola tailwindcss
```

## 初始化zola

```bash
zola init blog
```

详见 [zola](https://www.getzola.org/documentation/getting-started/overview/)

## 配置tailwindcss

根目录创建 `tailwind.config.js` 文件

```js
module.exports = {
  content: ['./templates/**/*.html'],
  theme: {
    extend: {},
  },
  variants: {},
  plugins: [],
};
```

在static中创建 `styles/main.css` 文件

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

在`base.html`中引入 `tailwindcss.css`(tailwindcss编译后产物) 复制时删除反斜杠

```html
<link
  href="{\{get_url(path='styles/tailwind.css',cachebust=true)}}"
  rel="stylesheet"
/>
```

## 启动serve

可以直接在两个终端分别运行

```bash
tailwindcss -i ./static/styles/main.css -o ./static/styles/tailwind.css --watch
```

```bash
zola serve
```

或者创建 `serve.py` 文件

```python
import subprocess

def run_command(command):
    process = subprocess.Popen(command, shell=True)
    return process

tailwind_process = run_command("tailwindcss -i ./static/styles/main.css -o ./static/styles/tailwind.css --watch")
zola_process = run_command("zola serve")

tailwind_process.wait()
zola_process.wait()
```

运行 `python serve.py`

## 构建

```bash
tailwindcss -i ./static/styles/main.css -o ./static/styles/tailwind.css
zola build
```

## 部署到vercel

根目录创建 `vercel.json` 文件

```json
{
  "framework": null,
  "installCommand": "REPO=\"getzola/zola\"; curl -fsS https://api.github.com/repos/${REPO}/releases/latest | grep -oP '\"browser_download_url\": ?\"\\K(.+linux-gnu.tar.gz)' | xargs -n 1 curl -fsSL -o zola.tar.gz && tar -xzvf zola.tar.gz && npm install tailwindcss",
  "buildCommand": "npx tailwindcss -i ./static/styles/main.css -o ./static/styles/tailwind.css && ./zola build",
  "outputDirectory": "public"
}
```

## gitignore 参考

```
node_modules
public
tailwind.css
```
