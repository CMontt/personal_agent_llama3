import psutil
import time

def pc_status(status: None) -> str: 
    try:
        cpu = psutil.cpu_percent(interval=1)

        memory = psutil.virtual_memory()
        ram_used = round(memory.used / (1024**3), 2)
        ram_total = round(memory.total / (1024**3), 2)
        ram_percent = memory.percent

        disk = psutil.disk_usage("/")
        disk_used = round(disk.used / (1024**3), 2)
        disk_total = round(disk.total / (1024**3), 2)
        disk_percent = disk.percent

        uptime_seconds = time.time() - psutil.boot_time()
        uptime_hours = round(uptime_seconds / 3600, 1)

        processes = len(psutil.pids())

        temps = psutil.sensors_temperatures()
        cpu_temp = "Indispónivel"

        if temps:
            for name, entries in temps.items():
                if entries:
                    cpu_temp = round(entries[0].current, 1)
                    break

        return (
                f"CPU: {cpu}%\n"
                f"RAM: {ram_used}GB / {ram_total}GB ({ram_percent}%)\n"
                f"Disk: {disk_used}GB / {disk_total}GB ({disk_percent}%)\n"
                f"Uptime: {uptime_hours} hours\n"
                f"Processes: {processes}"
        )
    except Exception as e:
        return f"Falha ao tentar obter informações do sistema: {e}"