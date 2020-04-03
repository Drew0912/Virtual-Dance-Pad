#-------------------------------------------
#Andrew Lee
#File name: Comparison.py
#-------------------------------------------
#
#
#Imports
import numpy as np #Additional maths functions
import cv2 #OpenCV
from skimage.metrics import structural_similarity

#Mean Squared Error
def mse(x, y):
    return np.linalg.norm(x - y)

#Structural Similarity Measure    
def ssim(x, y):
    return structural_similarity(x, y, multichannel=True)    


def main():
    im1 = cv2.imread('Control_picture.jpg')
    im2 = cv2.imread('Control_picture1.jpg')
    print(mse(im1, im2))

if __name__ == "__main__":
    main() 
           