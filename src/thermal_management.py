# thermal_management.py

import time
import os
import psutil

def get_cpu_temperature():
    """Get the current CPU temperature in Celsius."""
    with open('/sys/class/thermal/thermal_zone0/temp', 'r') as f:
        temp = float(f.read()) / 1000
    return temp

def get_cpu_usage():
    """Get the current CPU usage percentage."""
    return psutil.cpu_percent()

def log_thermal_data(log_file):
    """Log CPU temperature and usage data to a file."""
    while True:
        temp = get_cpu_temperature()
        usage = get_cpu_usage()
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        log_entry = f'{timestamp},{temp},{usage}\n'
        with open(log_file, 'a') as f:
            f.write(log_entry)
        time.sleep(60)  # Log data every minute

if __name__ == '__main__':
    log_file = 'thermal_data.log'
    if not os.path.exists(log_file):
        with open(log_file, 'w') as f:
            f.write('timestamp,temperature,cpu_usage\n')
    log_thermal_data(log_file)
