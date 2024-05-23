import cv2
import socket
import base64
from threading import Thread

ServerIPAddr = '192.168.68.118'

def StreamVid():
    camera = cv2.VideoCapture(0)  # Use 0 for the default camera
    while True:
        ret, frame = camera.read()  #
        if not ret:
            print("Failed to grab frame")
            break
 
        _, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 80])
        message = base64.b64encode(buffer)
        UdpVidOut.sendto(message, (ServerIPAddr, 5000))

if __name__ == "__main__":
    VID_BUFF_SIZE = 65536
    UdpVidOut = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    UdpVidOut.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, VID_BUFF_SIZE)

    TStreamVid = Thread(target=StreamVid, daemon=True)
    TStreamVid.start()
    TStreamVid.join()
