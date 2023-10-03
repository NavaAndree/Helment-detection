# Description: Viola-Jones algorithm for face detection
# Author: Andree Nava || Date: 2023-08-17

import cv2 as cv
import os, random

os.system('cls') # Clear the terminal

def detectFaceI(img):
    """Detect faces in images"""
    frontal_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml') 
    profile_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_profileface.xml') 

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ffaces = frontal_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30,30)) # 1.1 = scale factor, 4 = min neighbors
    pfaces = profile_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30,30)) 

    for (x, y, w, h) in ffaces:
        cv.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2) # 255, 0, 0 = color, 3 = thickness

    for (x, y, w, h) in pfaces:
        cv.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)

    return ffaces, pfaces

def names(cont):
    path = 'C:/Users/navan/OneDrive/Escritorio/database/test/a/'      # Path of the folder where the images are located
    files_names = os.listdir(path)         # List of the names of the images
    name = path + '/' + files_names[cont]  # Complete name of the image
    short_name = files_names[cont]         # Short name of the image
    length = len(files_names)              # Number of images in the folder
    return name, short_name, length

def resize_img(image, height):
    """Resize an image propotional to the given height"""
    ratio = height / image.shape[0]
    img = cv.resize(image, (int(image.shape[1]*ratio), height), interpolation=cv.INTER_AREA)
    return img

def main():
    print('Processing...')
    cont = 0                            # Counter to iterate over the list of images
    faces = 0                           # Counter for the number of images with faces detected

    while True:
        img = cv.imread(names(cont)[0])
        img = resize_img(img, 299)
        ffaces, pfaces = detectFaceI(img)

        if len(ffaces) > 0 or len(pfaces) > 0:
            faces += 1
        cont += 1

        if cont == names(cont)[2]-1:
            break
        
        print(f"Frame: {cont}/{names(cont)[2]}", end="\r")


    length = names(cont)[2]
    print('Faces detected in {} of {} images.'.format(faces, length))
    

if __name__ == '__main__':
    main()