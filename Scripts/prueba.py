import cv2

# Abre el video
cap = cv2.VideoCapture('C:\\Users\\navan\\OneDrive\\Escritorio\\database\\unclassified\\GOPR3300.MP4') 

# Obtiene la tasa de cuadros por segundo
fps = cap.get(cv2.CAP_PROP_FPS)

# Obtiene la cantidad total de fotogramas en el video
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Calcula la duración total del video en segundos
video_duration = frame_count / fps

print(f"Tasa de cuadros por segundo: {fps}")
print(f"Duración total del video: {video_duration:.2f} segundos")
print(f"Cantidad total de fotogramas: {frame_count}")

# Cierra el video
cap.release()
