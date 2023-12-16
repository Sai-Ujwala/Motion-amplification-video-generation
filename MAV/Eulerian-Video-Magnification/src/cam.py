import cv2
import time
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = None
chunk_duration = 10  # 10 seconds

while True:
    out = cv2.VideoWriter(f'output_chunk_{int(time.time())}.avi', fourcc, 20.0, (640, 480))
    start_time = cv2.getTickCount()
    while (cv2.getTickCount() - start_time) / cv2.getTickFrequency() < chunk_duration:
        ret, frame = cap.read()
        out.write(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1000) & 0xFF == ord('q'):
            break
    out.release()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()