import psutil
import time
import os

try:
    while True:
        cpu_usage = psutil.cpu_percent()
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')

        print(f"CPU: {cpu_usage}%\n"
              f"RAM: {memory.percent}% ({memory.used//1024//1024}MB / {memory.total//1024//1024}MB)\n"
              f"Disk: {disk.percent}%")
        time.sleep(0.5)
        os.system('cls')
except KeyboardInterrupt:
    print("\nМониторинг остановлен.")
