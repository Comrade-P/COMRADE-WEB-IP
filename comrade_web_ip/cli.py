# comrade_web_ip/cli.py

import socket
import argparse
import re
import pyfiglet
from colorama import Fore, Style

def main():
    parser = argparse.ArgumentParser(description="COMRADE_WEB_IP")
    parser.add_argument("--u", required=True, help="URL to fetch IPs for")
    args = parser.parse_args()
    url = args.u

    hi = pyfiglet.figlet_format("COMRADE__WEB__IP__FINDER", font="slant")
    print(Fore.WHITE + hi + Style.RESET_ALL)
    print(Fore.RED + "*" * 50 + Style.RESET_ALL)

    try:
        address_info = socket.getaddrinfo(url, None, socket.AF_UNSPEC)
        ipv4 = set()
        ipv6 = set()

        print(Fore.WHITE + "\n<----- IPv4 Addresses ----->" + Style.RESET_ALL)
        for info in address_info:
            ip_address = info[4][0]
            family = info[0]

            if family == socket.AF_INET:
                if ip_address in ipv4:
                    continue
                ipv4.add(ip_address)
                print(Fore.RED + f"🌐 IPv4: {ip_address}" + Style.RESET_ALL)

                private_ip = re.compile(r'^(127\.)|(192\.168\.)|(10\.)|(172\.(1[6-9]|2[0-9]|3[0-1]))')
                if private_ip.match(ip_address):
                    print("⚠️ Hidden IP Detected (Private IPv4)")
                else:
                    print(Fore.WHITE + "[✅ Public IPv4]" + Style.RESET_ALL)

        print(Fore.WHITE + "\n<----- IPv6 Addresses ----->" + Style.RESET_ALL)
        for info in address_info:
            ip_address = info[4][0]
            family = info[0]

            if family == socket.AF_INET6:
                if ip_address in ipv6:
                    continue
                ipv6.add(ip_address)
                print(Fore.RED + f"🌐 IPv6: {ip_address}" + Style.RESET_ALL)
                print(Fore.WHITE + "[✅ Public IPv6]" + Style.RESET_ALL)

    except Exception:
        print(f"Could not find the IP address for {url}.")
