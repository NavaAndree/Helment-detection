import cv2 as cv
import os, random

def resize_img(image, height):
    """Resize an image propotional to the given height"""
    ratio = height / image.shape[0]
    img = cv.resize(image, (int(image.shape[1]*ratio), height), interpolation=cv.INTER_AREA)
    return img

def random_image(path, n_img):
    files = os.listdir(path)
    frandom = random.sample(files, n_img)

    for file in frandom:
        #img = resize_img(cv.imread(path + file), 299)
        img = cv.imread(path + file)
        # Save the image
        cv.imwrite('C:/Users/navan/OneDrive/Escritorio/database/test/a/' + file, img)

        # cv.imshow('img', img)
        # cv.waitKey(0)

def main():
    path = 'C:/Users/navan/OneDrive/Escritorio/database/train/sin_casco/'
    random_image(path, 100)

if __name__ == '__main__':
    main()