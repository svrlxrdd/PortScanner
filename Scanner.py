#if you skid this shit - gay, give credz to sv!
import socket
import threading
import concurrent.futures
import subprocess
import platform
import colorama
from colorama import Fore
colorama.init()

print_lock = threading.Lock()

ip = input('IP: ')

operating_sys = platform.system()
nas = ip

def ping(ip):
    ping_command = ['ping', ip, '-n', '1'] if operating_sys == 'Windows' else ['ping', ip, '-c 1 -w 3000 -l 64']
    shell_needed = True if operating_sys == 'Windows' else False

    ping_output = subprocess.run(ping_command,shell=shell_needed,stdout=subprocess.PIPE)
    success = ping_output.returncode
    return True if success == 0 else False

out = ping(nas)
print(Fore.WHITE + 'ICMP: ' + Fore.GREEN + f'{out}')

def scan(ip, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)
    try:
        scanner.connect((ip, port))
        scanner.close()
        with print_lock:
            print(Fore.WHITE + 'TCP: ' + Fore.GREEN + f'{port}')
    except:
        pass

with concurrent.futures.ThreadPoolExecutor(max_workers=2048) as executer:
    for port in range(65535):
        executer.submit(scan, ip, port + 0)

print(Fore.WHITE + 'Finished Scanning.')
input()
