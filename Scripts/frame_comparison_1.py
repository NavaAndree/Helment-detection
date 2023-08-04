import cv2
import numpy as np

# calculate the difference between two images
def calculateDiff(img1, img2):
    difference = cv2.absdiff(img1, img2)
    mse = np.mean(difference**2) # mean squared error, used to calculate the difference
    diffPercentage = mse / 255.0 ** 2
    return diffPercentage * 100

ruta1 = 'frames/0.jpg'
ruta2 = 'frames/0c.jpg'

img1 = cv2.imread(ruta1, cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(ruta2, cv2.IMREAD_GRAYSCALE)

diff = cv2.subtract(img1, img2)

result = not np.any(diff)

if result is True:
    print('The images are equal')
else:
    cv2.imwrite('diff.jpg', diff)
    print('The images are different')

# diff = calculateDiff(img1, img2)
# print(f"Different percentage {diff:.2f}%")