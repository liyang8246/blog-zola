import subprocess

def run_command(command):
    process = subprocess.Popen(command, shell=True)
    return process

# 运行 tailwindcss 命令
tailwind_process = run_command("tailwindcss -i ./static/styles/main.css -o ./static/styles/tailwind.css --watch")

# 运行 zola serve 命令
zola_process = run_command("zola serve")

# 等待两个进程结束
tailwind_process.wait()
zola_process.wait()
