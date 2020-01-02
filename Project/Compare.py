import numpy as np #Additional maths functions. 
import cv2
import time #For Testing

from skimage.metrics import structural_similarity


def mse(x, y):
    return np.linalg.norm(x - y)

def ssim(x, y):
    return structural_similarity(x, y, multichannel=True)    




def main():
    im1 = cv2.imread('Control_picture.jpg')
    im2 = cv2.imread('Control_picture1.jpg')

    start = time.time()

    #print(mse(im1,im2))
    print(ssim(im1,im2))
    end = time.time()
    print(end - start)

    #print(ssim(im1,im2))


if __name__ == "__main__":
    main()