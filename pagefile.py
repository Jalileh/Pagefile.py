import psutil
 
import time
import os
import sys as sys


def monitor_overall():
 
    mem_info = psutil.virtual_memory()
 
    swap_info = psutil.swap_memory()

 
    return f"Total RAM: {mem_info.total / (1024**3):.2f} GB | Used RAM: {mem_info.used / (1024**3):.2f} GB | Pagefile (Swap) Usage: {swap_info.percent:.2f}%"


def monitor_app(app_name):
 
    for proc in psutil.process_iter(["pid", "name", "memory_info"]):
        try:
            if app_name.lower() in proc.info["name"].lower():
                mem_usage = proc.info["memory_info"].rss / (1024**2)  # Memory in MB
                return f"{app_name} (PID: {proc.info['pid']}) Memory Usage: {mem_usage:.2f} MB"

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    print(f"Application '{app_name}' not found.")


def clear_console():
    # Clear the console
    os.system("cls" if os.name == "nt" else "clear")


class Monitor_Apps:
    pass
    length = 0
    _list = []


apps = Monitor_Apps()

if __name__ == "__main__":
    try:
        ARGS = sys.argv
        apps.length = len(ARGS) - 0
        apps._list = ARGS
        apps._list.pop(0)

        print(f"ARGS size = {apps.length}")

    except:
        print("No specified App To monitor")

    # print(f" size of args {args.length}")

    clear_console()
    try:
        while True:
          
            clear_console()

            print(f"\n")   
            base_strings = []
            base_strings = monitor_overall() + "\n\n\n"
    

 

            print(base_strings, end=" ")
            if apps.length >= 1:
                for applications in apps._list:
                    data = monitor_app(applications) + "\n"
                    print(data, end=" ")

            print("\n")
            time.sleep(1)  # Refresh every 2 seconds

    except KeyboardInterrupt:
        print("\nMonitoring stopped.")
