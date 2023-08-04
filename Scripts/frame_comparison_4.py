# Description: This program compares two images and determines if they are similar or not. The functions
# used here will be used in the program frame_comparison_3.py, so we can finally extract the frames and 
# compare them in the same program. NEXT PROGRAM exfps_comp.py

import cv2, shutil, os, random
import numpy as np

#============================================FUNCTIONS==================================================#

def cal_object_area(imagen_segmentada):
    # Find contours of objects in the segmented image
    contours, _ = cv2.findContours(imagen_segmentada, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    object_area = []                    # initialize list to store areas of objects
    for contour in contours:            # Calculate the area of each object and add it to the list
        area = cv2.contourArea(contour)
        object_area.append(area)

    return object_area

def copy_file(origin, destination):
    try:
        shutil.copy(origin, destination)   # Copy the content of source to destination
        #print("File copied successfully.")
    except FileNotFoundError:              # If source and destination are same
        print(f"File {origin} not found.")
    except PermissionError:                # If destination is write protected
        print("Permission denied.")
    except Exception as aa:                # For other errors
        print(f"Error occurred while copying file: {aa}")

def names(cont):
    path = 'C:/Users/navan/Videos/sc'      # Path of the folder where the images are located
    files_names = os.listdir(path)         # List of the names of the images
    name = path + '/' + files_names[cont]  # Complete name of the image
    short_name = files_names[cont]         # Short name of the image
    length = len(files_names)              # Number of images in the folder
    return name, short_name, length
        
#===========================================MAIN=FUNCTION===============================================#

def main():
    cont=0
    print(names(cont)[2])
    while True:
        # Read two frames
        img1 = cv2.imread(names(cont)[0], cv2.IMREAD_GRAYSCALE)
        img2 = cv2.imread(names(cont+1)[0], cv2.IMREAD_GRAYSCALE)
        diff = cv2.subtract(img1, img2)   # Difference between images
        result = not np.any(diff)         # Compare the difference between images

        if result is True:
            print('The images are equal')
        else:
            cv2.imwrite('diff.jpg', diff)
            print('The images are different')

        _, thresh = cv2.threshold(diff,80,255,cv2.THRESH_BINARY) # Thresholding, to segment the image
        object_area = cal_object_area(thresh)    # Calculate the area of the objects in the segmented image
        total_areas = sum(object_area)           # Calculate the total of areas by adding all the areas
        
        percentage = (total_areas * 100) / (img1.shape[0] * img1.shape[1]) # Calculate the percentage of similarity
        percentage = 100 - percentage

        if percentage < 99.0:
            # Copy the content of source to destination
            source = names(cont+1)[0]
            destination = "C:/Users/navan/OneDrive/Documentos/TESIS/Scripts/prueba"
            copy_file(source, destination)

        cont += 1

        if cont == names(cont)[2]-1:
            break

        print(f"Total area: {total_areas:.2f} pixels")
        print(f"Similarity: {percentage:.2f}%")
        print(f"Frame: {cont}")

        # cv2.imshow('diff',thresh)
        # cv2.waitKey(0)

#========================================CALL=MAIN=FUNCTION=============================================#

if __name__ == '__main__': # 
    main()
