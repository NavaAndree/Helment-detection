# Description: Viola-Jones algorithm for face detection
# Author: Andree Nava || Date: 2023-08-17

import cv2, os

def detectFace(cont):
     # Read the cascade
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    img = cv2.imread(names(cont)[0])
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4) # 1.1 = scale factor, 4 = min neighbors

    tfd = 0 # Total of faces detected
    if len(faces) > 0: # If there are faces detected more than 0
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2) # 255, 0, 0 = color, 3 = thickness

        output = 'C:/Users/navan/OneDrive/Escritorio/database/sc_detected_faces' # Path of the folder where the images are located
        cv2.imwrite(os.path.join(output , names(cont)[1]), img) # Save the image

        tfd = counter() # Call the counter function

        #cv2.imshow('img', img) # Show the image
        #cv2.waitKey(0)

    return tfd

def counter():
    if not hasattr(counter, 'counter'):
        counter.counter = 0 # Counter for the number of images with faces detected
    counter.counter += 1
    #print(counter.counter)
    return counter.counter  

def precision(real_val, pred_val):
    pres = (pred_val * 100) / real_val
    print(f"Presicion: ", pres, f"%")

def names(cont):
    path = 'C:/Users/navan/OneDrive/Escritorio/database/sc'      # Path of the folder where the images are located
    files_names = os.listdir(path)         # List of the names of the images
    name = path + '/' + files_names[cont]  # Complete name of the image
    short_name = files_names[cont]         # Short name of the image
    length = len(files_names)              # Number of images in the folder
    return name, short_name, length

def main():
    cont = 0                             # Initialize the counter for the elements on the list of images, by the function names()  
    
    while True:
        #print(cont)
        cont_tfd = detectFace(cont)
        cont += 1
        if cont == names(cont)[2]-1:
            break

    print('Total images:', names(cont)[2])
    print('Total images with faces detected:', cont_tfd)
    precision(names(cont)[2], cont_tfd)

if __name__ == '__main__':
    main()