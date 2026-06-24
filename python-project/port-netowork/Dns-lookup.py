
import socket


def hostname_to_ip(hostname):
    """Convert a website name (hostname) to its IP address."""
    try:
        ip = socket.gethostbyname(hostname)
        return ip
    except socket.gaierror as e:
        return f"Error: Could not resolve'{hostname}' - {e}"
    

def ip_to_hostname(ip):
    """"Convert an IP address to its hostname (recverse DNS lookup)."""
    try:
        hostname = socket.gethostbyaddr(ip)[0]
        return hostname
    except socket.herror as e:
        return f"Error: no hostname found for '{ip}' - {e}"
    except socket.gaierror as e:
        return f"Error: Invalid IP address '{ip}' - {e}"
def main():
    print("=" * 45)
    print("          DNS lookup tool by Abhishek")
    print("=" * 45)
    print("Options:")   
    print("  1. Website Name ➡️ IP Address")
    print("  2. IP Address   ➡️ Website Name")
    print("  3. Exit")
    print("=" * 45)

    while True:
        choice = input("\n Enter choice (1/2/3): ").strip()

        if choice == "1":
            hostname = input("Enter Website name (e.g=> google.com): ").strip()
            ip = hostname_to_ip(hostname)
            print(f"\n  {hostname}  ➡️  {ip}")

        elif choice == "2":
            ip = input("Enter IP address (e.g. 8.8.8.8)").strip()
            hostname = ip_to_hostname(ip)
            print(f"  {ip}  ➡️  {hostname}")

        elif choice == "3":
            print("\n Exiting. see you later")
            break

        else:
            print("Invalid choice. Enter 1, 2, or 3.")

if __name__ == "__main__":
    main()

