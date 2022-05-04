import os 

def install_tools():
    os.system("pkg install root-repo")
    os.system("pkg install aircrack-ng")
    os.system("pkg install iw")
    os.system("pkg install xterm")
    os.system("pkg install ip")
    os.system("pkg install lspci")
    os.system("pkg install ps")
    os.system("pkg install bettercap")
    os.system("pkg install ettercap")
    os.system("pkg install dnsmasq")
    os.system("pkg install hostapd-wpe")
    os.system("pkg install iptables")
    os.system("pkg install bully")
    os.system("pkg install pixiewps")
    os.system("pkg install isc-dhcp-server")
    os.system("pkg install asleap")
    os.system("pkg install packetforge-ng")


def main():
    print("hi from genesis lol")
    choice = input('would you like to install the requirements? (y/n) ')
    if choice y:
        install_tools()
    if choice n:
        print("ok bye")
        breakpoint()
        
try:
    while True:
        main()
except keyboardInterrupt:
    print("\n\nbye")