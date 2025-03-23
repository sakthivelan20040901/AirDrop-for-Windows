import qrcode
import socket

def generate_qr():
    """Generate a QR code for Windows to scan."""
    ip = socket.gethostbyname(socket.gethostname())  # Get Mobile IP
    qr = qrcode.make(f"http://{ip}:5000")
    qr.show()  # Display QR code

generate_qr()
