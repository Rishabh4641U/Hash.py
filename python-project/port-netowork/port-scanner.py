import socket
import threading
from datetime import datetime


#----------------config ------------------------------------------

TARGET = input("Please enter your ip address: ")
START_PORT = 1
END_PORT = 1024
TIMEOUT = 1
THREADS = 100

open_ports = []
lock = threading.Lock()


# --------------------banner brabbing ---------------------------
def grab_banner(sock):
    try:
        sock.send(b"HEAD / HTTP/1.0\r\n\r\n")
    except:
        return None

# -------------Port Scanner ------------------------------------

def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(TIMEOUT)
        result = sock.connect_ex((host, port))
        if result == 0:
            banner = grab_banner(sock)
            with lock:
                open_ports.append(port)
                service = get_service(port)
                print(f"[+] Port {port:5d}/tcp open {service}")
                if banner:
                    print(f"     bannner: {banner[:60]}")
        sock.close()
    except:
        pass

# ---------------------------Comman Serivces-------------------
def get_service(port):
    service = {
        21: "FTB", 22: "SSH", 23: "Telnet", 25: "SMTP",
        53: "DNS", 80: "HTTP", 110: "POP3", 143: "IMAP",
        443: "HTTPS", 445: "SMB", 3306: "MySQL", 
        3389: "RDP", 8080: "HTTP-Alt", 8443: "HTPPS-Alt"
    }
    return service.get(port, "Unknown")
# --------------Thread Manager---------------------------------
def threaded_scan(host, ports):
    threads = []
    for port in ports:
        t = threading.Thread(target=scan_port, args=(host, port))
        threads.append(t)
        t.start()

        # limit active threads
        if len(threads) >= THREADS:
            for t in threads:
                t.join()
            threads = []


# ---------------------main -------------------------------------
if __name__ == "__main__":
    print(f"""
        ===========================================================
        ||                                                        ||
        ||       Python port Scanner by abhishek_mishra209        ||
        ||                                                        ||
        =========================================================== 
          Target 🎯 : {TARGET}      
          Ports    : {START_PORT}  -  {END_PORT}
          Threads  : {THREADS}
          Time     : {datetime.now().strftime('%H:%M:%S')}
""")
    try:
        ip = socket.gethostbyname(TARGET)
        print(f"      REsolved:  {ip}\n")
    except socket.gaierror:
        print("  [!] Could not resolve host.")
        exit()

    start = datetime.now()
    ports = range(START_PORT,END_PORT + 1)
    threaded_scan(TARGET, ports)

    end = datetime.now()
    print(f"""
    ___________________________________________________________
          Open ports : {sorted(open_ports)}
          Scan Time  : {end - start}
    ___________________________________________________________

""")

