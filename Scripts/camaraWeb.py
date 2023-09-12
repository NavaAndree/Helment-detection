# Open the camara web and show the image in a window

import cv2

def main():
    cap = cv2.VideoCapture(0)

    while True:
        _, img = cap.read()
        cv2.imshow('img', img)
        k = cv2.waitKey(30) & 0xff
        if k==27:
            break

    cap.release()

if __name__ == '__main__':
    main()
