import socket
import tqdm
import os

PORT = 60000
BUFFER_SIZE = 4096

def send_file(file_path, mobile_ip):
    """Send a file to the mobile device."""
    file_size = os.path.getsize(file_path)

    # Connect to mobile
    s = socket.socket()
    s.connect((mobile_ip, PORT))

    # Send filename & size
    s.send(f"{os.path.basename(file_path)}|{file_size}".encode())

    # Send the file
    progress = tqdm.tqdm(range(file_size), f"Sending {file_path}", unit="B", unit_scale=True)
    with open(file_path, "rb") as f:
        while (bytes_read := f.read(BUFFER_SIZE)):
            s.sendall(bytes_read)
            progress.update(len(bytes_read))

    s.close()
