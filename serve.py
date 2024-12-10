import subprocess

def run_command(command):
    process = subprocess.Popen(command, shell=True)
    return process

tailwind_process = run_command("tailwindcss -i ./static/styles/main.css -o ./static/styles/tailwind.css --watch")
zola_process = run_command("zola serve")

tailwind_process.wait()
zola_process.wait()