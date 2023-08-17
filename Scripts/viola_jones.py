# Description: Viola-Jones algorithm for face detection
# Author: Andree Nava || Date: 2023-08-17

import cv2

def detectFace():
     # Read the cascade
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    ########################### For images use this:
    img = cv2.imread('test.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4) # 1.1 = scale factor, 4 = min neighbors


    for (x, y, w, h) in faces:
         cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2) # 255, 0, 0 = color, 3 = thickness

    cv2.imshow('img', img) # Show the image
    cv2.waitKey(0)

    ########################### For videos use this:
    #cap = cv2.VideoCapture(0)
    #cap = cv2.VideoCapture('C:\\Users\\navan\\OneDrive\\Escritorio\\database\\videos_cc\\p1.mp4')

    # while True:
    #     _, img = cap.read()
    #     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #     faces = face_cascade.detectMultiScale(gray, 1.1, 4) # 1.1 = scale factor, 4 = min neighbors

    #     for (x, y, w, h) in faces:
    #         cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2) # 255, 0, 0 = color, 3 = thickness

    #     cv2.imshow('img', img)
    #     k = cv2.waitKey(30) & 0xff
    #     if k==27:
    #         break

    # cap.release()

def main():
    detectFace()

if __name__ == '__main__':
    main()