NameDrop - Peer-to-Peer File Sharing

NameDrop is a peer-to-peer file-sharing system that allows seamless file transfers between Windows and Mobile devices over Wi-Fi. The system is inspired by Apple's AirDrop and includes gesture-based file sharing.

Features

Peer-to-peer file sharing over Wi-Fi

NameDrop functionality for Windows ↔ Mobile

Gesture-based file transfer

Secure & fast file transmission

Prerequisites

For Windows:

Python 3.8+

Flask (pip install flask)

OpenCV (pip install opencv-python)

tqdm (pip install tqdm)

Git (optional, for cloning the repo)

For Mobile (Android):

Termux (or Pydroid 3 for running Python scripts)

Python 3

Flask (pip install flask)

tqdm (pip install tqdm)

Installation

1️⃣ Clone the Repository

 git clone https://github.com/yourusername/NameDrop.git
 cd NameDrop

2️⃣ Setup Windows Server

 cd NameDrop/windows
 python server.py

📌 Windows should display:

 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)

3️⃣ Setup Mobile Server (Android - Termux/Pydroid)

 cd NameDrop/mobile
 python app.py

📌 Mobile should display:

 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)

Usage

Windows to Mobile File Transfer

Ensure both devices are connected to the same Wi-Fi network.

Find the Mobile IP address (ifconfig on Termux or check Wi-Fi settings).

On Windows, enter the mobile's IP address.

Select the file and send.

Mobile to Windows File Transfer

On Mobile, enter the Windows IP address (ipconfig in CMD).

Select the file and send.

Gesture-Based File Sharing

Open the gesture recognition app on Windows.

Perform the predefined hand gesture (e.g., swipe to send).

The file is transferred automatically.

Troubleshooting

Server not starting? Ensure Python and dependencies are installed.

File not transferring? Ensure devices are on the same network.

Gesture not detected? Check your camera permissions.

Contributing

Feel free to fork and contribute! Submit a PR for improvements.

License

This project is licensed under the MIT License.

