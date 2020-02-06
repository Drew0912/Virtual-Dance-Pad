import numpy as np #Additional maths functions
import cv2 #OpenCV

def mse(x, y):
    return np.linalg.norm(x - y)

def main():
    im1 = cv2.imread('Control_picture.jpg')
    im2 = cv2.imread('Control_picture1.jpg')

if __name__ == "__main__":
    main()        