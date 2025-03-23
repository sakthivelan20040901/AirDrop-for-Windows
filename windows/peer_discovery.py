import socket

PORT = 50001
DISCOVERY_MSG = "NAMEDROP_DISCOVERY"

def find_mobile():
    """Find mobile devices on the network."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    print("Searching for mobile devices...")
    sock.sendto(DISCOVERY_MSG.encode(), ('<broadcast>', PORT))

    sock.settimeout(5)  # Wait for response
    try:
        data, addr = sock.recvfrom(1024)
        if data.decode() == "MOBILE_FOUND":
            print(f"📱 Mobile found: {addr[0]}")
            return addr[0]
    except socket.timeout:
        print("❌ No mobile device found.")
        return None
