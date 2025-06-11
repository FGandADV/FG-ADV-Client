import sys
import time
from pathlib import Path

class SystemMonitor:
    def __init__(self):
        self.start_time = time.time()

    def get_system_info(self):
        try:
            import psutil
            cpu_percent = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            disk = psutil.disk_usage('/')

            return {
                "cpu_usage": cpu_percent,
                "memory_total": memory.total,
                "memory_available": memory.available,
                "disk_total": disk.total,
                "disk_free": disk.free
            }
        except:
            return {"status": "monitoring_disabled"}

    def log_system_activity(self):
        uptime = time.time() - self.start_time
        print(f"System uptime: {uptime:.2f} seconds")

        info = self.get_system_info()
        for key, value in info.items():
            print(f"{key}: {value}")

def start_monitoring():
    monitor = SystemMonitor()
    monitor.log_system_activity()

if __name__ == "__main__":
    start_monitoring()
