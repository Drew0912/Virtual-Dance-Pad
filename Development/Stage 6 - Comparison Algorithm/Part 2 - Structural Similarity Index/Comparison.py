import numpy as np #Additional maths functions
import cv2 #OpenCV

from skimage.metrics import structural_similarity

def mse(x, y): #Mean Squared Error
    return np.linalg.norm(x - y)

def ssim(x, y):
    return structural_similarity(x, y, multichannel=True)    

def main():
    im1 = cv2.imread('Control_picture.jpg') #Read first image.
    im2 = cv2.imread('Control_picture1.jpg') #Read second image.

    print(ssim(im1, im2))

if __name__ == "__main__":
    main()        