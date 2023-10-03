# Description: Viola-Jones algorithm for face detection
# Author: Andree Nava || Date: 2023-08-17

import cv2

def detectFaceI():
    """Detect faces in images"""
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    img = cv2.imread('test_vj1.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4) # 1.1 = scale factor, 4 = min neighbors

    for (x, y, w, h) in faces:
         cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2) # 255, 0, 0 = color, 3 = thickness

    print(f"Faces detected: {len(faces)}")
    cv2.imshow('img', img)
    cv2.waitKey(0)

def resize_img(image, height):
    """Resize an image propotional to the given height"""
    ratio = height / image.shape[0]
    img = cv2.resize(image, (int(image.shape[1]*ratio), height), interpolation=cv2.INTER_AREA)
    return img

def detectFaceV():
    """Detect faces in videos"""
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') # Read the cascade
    profile_cascade = cv2.CascadeClassifier('haarcascade_profileface.xml')
    cap = cv2.VideoCapture(0)
    #cap = cv2.VideoCapture('C:/Users/navan/OneDrive/Escritorio/database/v_test/vsc/p1.mp4')

    while True:
        _, img = cap.read()
        img = resize_img(img, 299)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30,30)) # 1.1 = scale factor, 4 = min neighbors
        profile = profile_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30,30))

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2) # 255, 0, 0 = color, 3 = thickness

        for (x, y, w, h) in profile:
            cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)

        cv2.imshow('img', img)

        k = cv2.waitKey(30) & 0xff
        if k==27:
            break

    cap.release()

def main():
    detectFaceV()

if __name__ == '__main__':
    main()