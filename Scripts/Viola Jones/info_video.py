import cv2

# Importamos el video
cap = cv2.VideoCapture("C:/Users/navan/OneDrive/Escritorio/database/vj/p1a.mp4")
num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print("El video tiene {} frames".format(num_frames))
cap = cv2.VideoCapture("C:/Users/navan/OneDrive/Escritorio/database/vj/p1b.mp4")
num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print("El video tiene {} frames".format(num_frames))
cap.release()


