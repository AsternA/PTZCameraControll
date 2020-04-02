import cv2
import numpy as np

cap = cv2.VideoCapture(src="rtsp://admin:afeka2016@192.168.1.67:554/Streaming/Channels/101/")
FRAME_WIDTH = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
FRAME_HIGTH = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print('Frame Size: ', FRAME_WIDTH, 'x', FRAME_HIGTH)

if cap.isOpened():
    ret, frame = cap.read()
else:
    ret = False

while ret:
    ret, frame = cap.read()
    cv2.imshow('Camera', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()