from sklearn.metrics import classification_report, confusion_matrix
import cv2 as cv
import os
import numpy as np

os.system('cls') # Clear the terminal

def names(cont):
    path = 'C:/Users/navan/OneDrive/Escritorio/database/vj/' # Folder with the videos
    fnames = os.listdir(path)         # List of the names of the videos
    name = path + '/' + fnames[cont]  # Complete name of the video
    short_name = fnames[cont]         # Short name of the video
    length = len(fnames)              # Number of videos in the folder
    return name, short_name, length

def resize_img(image, height):
    """Resize an image propotional to the given height"""
    ratio = height / image.shape[0]
    img = cv.resize(image, (int(image.shape[1]*ratio), height), interpolation=cv.INTER_AREA)
    return img

def detectFace(cont):
    tfaces = 0
    current_frame = 0
    name_video = names(cont)[1]
    cap = cv.VideoCapture('C:/Users/navan/OneDrive/Escritorio/database/vj/' + name_video)
    
    face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
    profile_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_profileface.xml')

    while True:
        _, img = cap.read()

        if not _:
            break

        num_frames = int(cap.get(cv.CAP_PROP_FRAME_COUNT))
        img = resize_img(img, 299)
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30,30))
        profiles = profile_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30,30))

        for (x, y, w, h) in faces:
            cv.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
        for (x, y, w, h) in profiles:
            cv.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)

        #cv.imshow('img', img)

        if len(faces) > 0 or len(profiles) > 0:
            tfaces += 1
        else:
            tfaces += 0

        current_frame += 1
        print(f'Frame: {current_frame}/{num_frames}', end='\r')

        k = cv.waitKey(30) & 0xff
        if k==27:
            break

    print('Faces detected in {} on {} frames.'.format(tfaces, num_frames))
    cap.release()

    return tfaces, num_frames


def main():
    cont = 0
    cm = np.zeros((2, 2))

    while True:
        try:
            face, noFace = detectFace(cont)
            cm[cont] = [face, noFace-face]
            print('Faces: {face}, noFaces: {noFace}'.format(face=face, noFace=noFace))
            cont += 1
        except IndexError:
            print('Confusion Matrix: \n', cm)
            print('Done!')	
            break

    report = classification_report(cm[:,0], cm[:,1])

if __name__ == '__main__':
    main()