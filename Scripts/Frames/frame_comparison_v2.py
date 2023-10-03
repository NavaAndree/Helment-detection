import cv2, shutil, os, random
import numpy as np

def calcular_areas_objetos(imagen_segmentada):
    # Encontrar contornos de los objetos en la imagen segmentada
    contornos, _ = cv2.findContours(imagen_segmentada, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Inicializar lista para almacenar áreas de objetos
    areas_objetos = []
    # Calcular el área de cada objeto y agregarlo a la lista
    for contorno in contornos:
        area = cv2.contourArea(contorno)
        areas_objetos.append(area)

    return areas_objetos

def move_file(origin, destination):
    try:
        shutil.move(origin, destination)
        #print("File copied successfully.")
    except shutil.SameFileError:
        print("Source and destination represents the same file.")
    except PermissionError:
        print("Permission denied.")
    except Exception as aa:
        print(f"Error occurred while copying file: {aa}")

path = 'frames'

ruta1 = 'frames/0.jpg'
ruta2 = 'frames/13.jpg'

img1 = cv2.imread(ruta1, cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(ruta2, cv2.IMREAD_GRAYSCALE)
#print(img1.shape)

diff = cv2.subtract(img1, img2)
result = not np.any(diff)

if result is True:
    print('The images are equal')
else:
    cv2.imwrite('diff.jpg', diff)
    print('The images are different')

_, thresh = cv2.threshold(diff,80,255,cv2.THRESH_BINARY)

areas_objetos = calcular_areas_objetos(thresh) # Calcular las áreas de los objetos en la imagen segmentada
total_areas = sum(areas_objetos)               # Calcular el total de áreas sumando todas las áreas

porcentage = (total_areas * 100) / (img1.shape[0] * img1.shape[1])
porcentage = 100 - porcentage

if porcentage < 99.0:
    # Move the content of source to destination
    source = ruta2
    destination = "prueba"
    move_file(source, destination)

print(f"Total de áreas: {total_areas:.2f} píxeles")
print(f"Similitud: {porcentage:.2f}%")

cv2.imshow('diff',thresh)
cv2.waitKey(0)
