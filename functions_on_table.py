
# Functions which add details to the table.
# In the end, we print the table.

import functions as f
import socket
import platform
from prettytable import PrettyTable
import psutil

# Global variables
table = PrettyTable(['Parameter', 'Value'])

def print_computer_hardware_details():
    add_operation_system_data()

    add_CPU_data()

    add_RAM_data()

    # List of all disks and their usage
    partitions = psutil.disk_partitions()
    add_disks_data(partitions)

    add_IP_data()

    print(table)

def add_operation_system_data():
    global table
    operating_system = platform.system()
    # Adding to table
    table.add_row(['operating system', operating_system])

def add_CPU_data():
    global table
    processor = platform.processor()
    number_of_physical_cores = psutil.cpu_count(logical=False)
    number_of_logical_cores = psutil.cpu_count(logical=True)
    cpu_usage = [str(i) + "%" for i in psutil.cpu_percent(interval=1, percpu=True)]
    cpu_frequency = f"{psutil.cpu_freq().current:.2f}Mhz"

    # Adding to table
    table.add_rows(
        [
            ['Processor', processor],
            ['Physical CPU cores', number_of_physical_cores],
            ['Total CPU cores', number_of_logical_cores],
            ['CPU usage per core', cpu_usage],
            ['CPU frequency', cpu_frequency]
        ]
    )

def add_RAM_data():
    global table
    total, available, percent, used, free = psutil.virtual_memory()
    used_size_format = f.size_format(used)
    total_size_format = f.size_format(total)
    text_color = f.get_font_color(percent)
    ram_usage = text_color + f"{used_size_format} / {total_size_format} ({percent}%)" + f.DEFAULT
    ram_free_space = f.size_format(free)

    # Adding to table
    table.add_rows(
        [
            ['RAM usage', ram_usage],
            ['Free memory in RAM', ram_free_space]
        ]
    )

def add_disks_data(partitions):
    # inserts disks' data into indexes and table for printing a data frame.
    global table
    for partition in partitions:
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            # this can be caught due to the disk that isn't ready
            continue
        used = f.size_format(partition_usage.used)
        free = f.size_format(partition_usage.free)
        usage_percentage = partition_usage.percent
        text_color = f.get_font_color(usage_percentage)
        # Adding to table
        table.add_row([f"Device {partition.device} usage", text_color + f"{used} / {free} ({usage_percentage}%)" + f.DEFAULT])

def add_IP_data():
    IP_address = socket.gethostbyname(socket.gethostname())
    # Adding to table
    table.add_row(['IP address', IP_address])

