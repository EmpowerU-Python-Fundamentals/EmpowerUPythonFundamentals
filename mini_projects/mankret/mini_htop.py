import psutil
import time
import os
from rich.console import Console
from rich.table import Table

console = Console()


def clear_screen():
    """Cleaning the console """
    os.system('cls' if os.name == 'nt' else 'clear')


def get_size(bytes, suffix="B"):
    """Byte formatting"""
    factor = 1024
    for unit in ["", "K", "M", "G", "T"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


def draw_dashboard():
    # CPU
    cpu_percent = psutil.cpu_percent(interval=0.5)
    cpu_freq = psutil.cpu_freq().current if psutil.cpu_freq() else 0
    cpu_cores = psutil.cpu_count(logical=True)

    # RAM
    svmem = psutil.virtual_memory()

    # Disk
    partitions = psutil.disk_partitions()

    # Processes (top 5 by CPU usage)
    processes = []
    for p in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        try:
            processes.append(p.info)
        except psutil.NoSuchProcess:
            pass
    processes = sorted(
        processes,
        key=lambda p: p['cpu_percent'] or 0.0,
        reverse=True
    )[:5]

    clear_screen()

    console.rule("[bold blue]📊 System Monitor[/bold blue]")

    # CPU info
    table_cpu = Table(title="CPU Info", style="cyan")
    table_cpu.add_column("Cores")
    table_cpu.add_column("Frequency (MHz)")
    table_cpu.add_column("Usage (%)")
    table_cpu.add_row(str(cpu_cores), f"{cpu_freq:.2f}", str(cpu_percent))
    console.print(table_cpu)

    # RAM info
    table_ram = Table(title="Memory", style="green")
    table_ram.add_column("Total")
    table_ram.add_column("Used")
    table_ram.add_column("Available")
    table_ram.add_column("Usage (%)")
    table_ram.add_row(
        get_size(svmem.total),
        get_size(svmem.used),
        get_size(svmem.available),
        str(svmem.percent)
    )
    console.print(table_ram)

    # Disk info
    table_disk = Table(title="Disk Usage", style="magenta")
    table_disk.add_column("Device")
    table_disk.add_column("Mount")
    table_disk.add_column("Total")
    table_disk.add_column("Used")
    table_disk.add_column("Free")
    table_disk.add_column("Usage (%)")

    for partition in partitions:
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            table_disk.add_row(
                partition.device,
                partition.mountpoint,
                get_size(usage.total),
                get_size(usage.used),
                get_size(usage.free),
                str(usage.percent)
            )
        except PermissionError:
            continue
    console.print(table_disk)

    # Processes info
    table_proc = Table(title="Top Processes (CPU)", style="yellow")
    table_proc.add_column("PID")
    table_proc.add_column("Name")
    table_proc.add_column("CPU %")

    for proc in processes:
        table_proc.add_row(str(proc['pid']), proc['name'], str(proc['cpu_percent']))

    console.print(table_proc)
    console.print("Press CTRL+C to exit")


if __name__ == "__main__":
    try:
        while True:
            draw_dashboard()
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nExiting...")