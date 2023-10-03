import os, shutil
import cv2 as cv
import numpy as np

os.system('cls')               # Clear the terminal

# Resize function to 299x299
def resize_img(image, height):
    """Resize an image propotional to the given height"""
    ratio = height / image.shape[0]
    img = cv.resize(image, (int(image.shape[1]*ratio), height), interpolation=cv.INTER_AREA)
    img1 = img[:, 116:415]
    return img1
# Function to create a folder
def create_folder(path):
    if os.path.exists(path):
        shutil.rmtree(path)                # Remove the folder if it already exists
        os.mkdir(path)                     # Create the folder
    else:
        os.mkdir(path)                     # Create the folder

path = 'C:/Users/navan/OneDrive/Escritorio/database/cropped/test/con_casco' # Folder where the images will be saved
create_folder(path)                        # Create the folder

def names_images(cont):
    path = 'C:/Users/navan/OneDrive/Escritorio/database/test/con_casco/'  # Folder where the images are located
    files_names = os.listdir(path)         # List of the names of the videos
    name = path + '/' + files_names[cont]  # Complete name of the video
    short_name = files_names[cont]         # Short name of the video
    length = len(files_names)              # Number of videos in the folder
    return name, short_name, length

# Read images from a folder
#

def main():
    cont = 0

    while True:
        try:
            img_name = cv.imread(names_images(cont)[0])
            img = resize_img(img_name, 299)
            cv.imwrite(path + '/' + names_images(cont)[1], img)
        except IndexError:
            break
        
        print(f'Image {cont}/{names_images(cont)[2]} saved, shape: {img.shape}', end='\r')
        cont += 1
        
if __name__ == '__main__':
    main()      

