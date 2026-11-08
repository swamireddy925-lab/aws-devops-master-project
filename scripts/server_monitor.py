import time
import shutil

def get_cpu_usage():
    with open("/proc/stat", "r") as file:
        cpu = list(map(int, file.readline().split()[1:]))

    idle1 = cpu[3] + cpu[4]
    total1 = sum(cpu)

    time.sleep(1)

    with open("/proc/stat", "r") as file:
        cpu = list(map(int, file.readline().split()[1:]))

    idle2 = cpu[3] + cpu[4]
    total2 = sum(cpu)

    total_diff = total2 - total1
    idle_diff = idle2 - idle1

    return round((1 - idle_diff / total_diff) * 100, 2)


def get_memory_usage():
    memory = {}

    with open("/proc/meminfo", "r") as file:
        for line in file:
            key, value = line.split(":")
            memory[key] = int(value.strip().split()[0])

    total = memory["MemTotal"]
    available = memory["MemAvailable"]

    return round((total - available) / total * 100, 2)


def get_disk_usage():
    disk = shutil.disk_usage("/")
    return round((disk.used / disk.total) * 100, 2)


cpu = get_cpu_usage()
ram = get_memory_usage()
disk = get_disk_usage()

print("AWS EC2 SERVER MONITORING")
print("-------------------------")

print("CPU Usage:", cpu, "%")
print("RAM Usage:", ram, "%")
print("Disk Usage:", disk, "%")

if cpu > 80:
    print("WARNING: High CPU usage!")

if ram > 80:
    print("WARNING: High RAM usage!")

if disk > 80:
    print("WARNING: Low disk space!")
